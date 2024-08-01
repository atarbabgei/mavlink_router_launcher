#!/bin/bash

# List of possible installation paths
possible_paths=(
    "/usr/local/bin/mavlink-routerd"
    "/usr/bin/mavlink-routerd"
    "/opt/mavlink-router/mavlink-routerd"
    "/usr/local/sbin/mavlink-routerd"
    "/usr/sbin/mavlink-routerd"
    "$HOME/bin/mavlink-routerd"
)

# Function to check and remove mavlink-routerd
uninstall_mavlink_routerd() {
    local path="$1"
    if [ -f "$path" ]; then
        echo "Removing mavlink-routerd from $path..."
        sudo rm -f "$path"
        if [ ! -f "$path" ]; then
            echo "mavlink-routerd successfully uninstalled from $path."
        else
            echo "Failed to uninstall mavlink-routerd from $path. Please check permissions."
        fi
    else
        echo "mavlink-routerd not found in $path."
    fi
}

# Check each possible path
for path in "${possible_paths[@]}"; do
    uninstall_mavlink_routerd "$path"
done
