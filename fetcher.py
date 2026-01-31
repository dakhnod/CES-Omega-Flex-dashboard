import firebird.driver as driver
import requests
import time
import sys

driver.load_api(r'C:\Program Files\CEStronics Suite 4\server\firebirdsql\fb30x64\fbclient.dll')

connection = driver.connect(
    r'localhost/9632:C:\Program Files\CEStronics Suite 4\server\database\SUITE_SERVER_DATABASE.FB30',
    user='sysdba',
    password='masterkey'
)

cursor = connection.cursor()
cursor.execute('''
SELECT
    td.ID,
	td.FQN_NAME, 
	tdp.BATTERY_STATUS, 
	tds.LAST_ONLINE_TIME,
	tds.LAST_BATTERY_CHANGE
FROM TB_DEVICES td  
LEFT JOIN TB_DEVICE_PROP tdp 
	ON td.ID = tdp.DEVICE_FK 
LEFT JOIN TB_DEVICE_STATISTIC tds 
	ON td.ID = tds.DEVICE_FK
WHERE
	tdp.BATTERY_STATUS IS NOT NULL
''')

for row in cursor.fetchall():
    print(device_id)
    try:
        last_online = row[3].timestamp()
    except:
        last_online = 0
        
    try:
        last_battery_change = row[4].timestamp()
    except:
        last_battery_change = 0
        
    response = requests.post(
        f'https://structure.nullco.de/api/nodes/multiple/attributes',
        params={
            'token': sys.argv[1], # API token
            'id': '697d221eb003c1f2b9366827', # 'Devices' root node ID,
            'include': 'children', # recursively iterate through tree
            'filter.attributes.device_id': row[0] # Make server find the right node mapped by the hidden attribute 'device_id'
        },
        json={
            'battery': row[2],
            'last_online': last_online,
            'last_battery_change': last_battery_change
        }
    )
    print(response.text)

connection.close()
