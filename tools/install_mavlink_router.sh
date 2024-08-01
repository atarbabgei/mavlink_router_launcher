#!/bin/bash

# Function to determine the system architecture
get_architecture() {
    local arch
    arch=$(uname -m)
    case "$arch" in
        x86_64)
            echo "x86_64"
            ;;
        aarch64)
            echo "aarch64"
            ;;
        armv7l|armhf)
            echo "armhf"
            ;;
        i686|i386)
            echo "i686"
            ;;
        *)
            echo "Unsupported architecture: $arch"
            exit 1
            ;;
    esac
}

# Check if mavlink-routerd is already installed
if command -v mavlink-routerd >/dev/null 2>&1; then
    echo "Mavlink Router is already installed. There's no need to install it again"
    exit 0
fi

# Base URL for downloading the executables
base_url="https://github.com/mavlink-router/mavlink-router/releases/download/v4"

# Determine the system architecture
arch=$(get_architecture)

# Define the file to download based on architecture
case "$arch" in
    x86_64)
        filename="mavlink-routerd-glibc-x86_64"
        ;;
    aarch64)
        filename="mavlink-routerd-glibc-aarch64"
        ;;
    armhf)
        filename="mavlink-routerd-glibc-armhf"
        ;;
    i686)
        filename="mavlink-routerd-glibc-i686"
        ;;
    *)
        echo "Unsupported architecture: $arch"
        exit 1
        ;;
esac

# Download the appropriate file
url="${base_url}/${filename}"
echo "Downloading ${filename} from ${url}..."
wget -O /usr/local/bin/mavlink-routerd "$url"

# Make the file executable
chmod +x /usr/local/bin/mavlink-routerd

# Verify installation
if command -v mavlink-routerd >/dev/null 2>&1; then
    echo "Mavlink Router installed successfully."
else
    echo "Failed to install Mavlink Router."
fi
