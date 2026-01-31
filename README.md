# CES-Omega-Flex-dashboard
This serves as a demo for [my platform](https://github.com/dakhnod/Structure-thing) project using data from CES electric door locks.

## What to do

- Visit [the data platform](https://habitat.nullco.de)
- Click through the tree
- Be amazed at the presentation of the data (the logic, not the graphical beauty...)
- Do a right click on one of the first device, click on the pencil icon next to the attributes
- Check out [the script](fetcher.py), try to understand how the data gets uploaded to the right node

## Summary

the python script fetches the data via SQL from some database, prepares the data into primitive data types and sends it to the platform.
Instead of using the specific device node's id, it uses the ID `multiple` together with the get parameter `id`, pointing at the `Devices` root node.
This by itself would send the same dataset to all child nodes. As such, a `filter` parameter is added in order to target only the node containing the `id` of the actual device.

On the server side, there is a `validation` rule set in order to trigger an alarm whenever the battery attribute changes to `1`.
Also, there are `display transformation` rules set in order to properly display the timestamps set.

## Contact

If you want to have a chat about the platform, just shoot me a mail to dakhnod@gmail.com
