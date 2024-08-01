
# Mavlink Router Lancher

## Overview
`mavlink_router_launcher` is a ROS 2 package that provides a thin wrapper around the `mavlink-routerd` command.

## Requirements
- ROS 2 (tested on Humble)
- `mavlink-routerd`

## Installation

### Option 1. Install `mavlink-routerd` from source
Follow instalation in [mavlink router repository](https://github.com/mavlink-router/mavlink-router.git) 

After installing 'mavlink-routerd', then clone and build this ROS 2 package.

### Option 2. Install `mavlink-routerd` from Pre-built Binaries

To install `mavlink-routerd`, you can use the provided script in the repository. Follow these steps:

1. Clone the repository (if you haven't already):

   ```bash
   git clone https://github.com/atarbabgei/mavlink_router_launcher.git
   cd mavlink_router_launcher
   ```

2. Make the script executable:

   ```bash
   chmod +x tools/install_mavlink_router.sh
   ```

3. Run the script with superuser privileges:

   ```bash
   sudo ./tools/install_mavlink_router.sh
   ```

This script will automatically detect your system architecture, download the appropriate `mavlink-routerd` executable, and install it in the `/usr/local/bin` directory.


## Example usage

```bash
ros2 launch mavlink_router_launcher mavlink_router.launch.py endpoint:=192.168.0.7:14550 device:=/dev/ttyACM0 baudrate:=115200
```
