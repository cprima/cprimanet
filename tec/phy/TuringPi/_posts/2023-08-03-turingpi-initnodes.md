---
layout: post
title: TuringPi init-nodes.sh
component: TA_PTC_051
date:   2023-08-03 12:00:00 +0100
abstract: "I've released a new utility script for the Turing Pi 2 on my GitHub Gist. The script allows users to initialize and configure multiple CM4 nodes in an automated way."
---

## TuringPi init-nodes.sh ⚙️🖥️🔄

I've released a new utility script for the Turing Pi 2 on my GitHub Gist. The script allows users to initialize and configure multiple CM4 nodes in an automated way. By specifying node numbers or ranges, it streamlines tasks like copying configurations and power cycling. If you're working with the Turing Pi 2, this might be a useful tool for you. Check out the script and its detailed usage instructions on [my Gist](https://gist.github.com/cprima/e09a5d2f4151f38cc98f2b2a196a0ee1).

### Usage

```bash
# ./init-nodes.sh [NUM_NODES] [HOSTNAME_PREFIX] [IMAGE_FILE]
# # For a single integer input for NUM_NODES:
# ./init-nodes.sh 3 tpi-node your_image_file.img
# # For a range input for NUM_NODES:
# ./init-nodes.sh 2..4 tpi-node your_image_file.img
```

#### Arguments:

- `NUM_NODES`: A parameter to define nodes for the script's operation. (Mandatory, up to 4 nodes).
  - If a single integer, such as 3, is specified, the script will run actions on nodes from 1 through to NUM_NODES.
  - When given a range (like 2..4), the script begins at the first specified node and ends with the last one in the range.
  
- `HOSTNAME_PREFIX`: The prefix for the hostname. A zero-padded node number will be appended to this prefix to form the full hostname (Optional, default: `node`).

- `IMAGE_FILE`: Name of the image file you want to flash. Provide just the filename. The script expects it to be located in `/mnt/sdcard` (Optional).