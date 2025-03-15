#!/bin/bash
# setup_dependencies.sh - Script to install and configure dependencies for PiCrawler
# Run with: sudo bash setup_dependencies.sh

echo "PiCrawler Dependencies Setup"
echo "============================"
echo "This script will install and configure all required packages for PiCrawler."
echo

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

echo "Step 1: Updating package lists..."
apt update

echo
echo "Step 2: Installing system dependencies..."
apt install -y python3-picamera2 python3-opencv python3-pip python3-venv python3-flask alsa-utils sox libsox-fmt-all

echo
echo "Step 3: Configuring ALSA..."
# Create a better ALSA configuration
cat > /etc/asound.conf << 'EOL'
pcm.!default {
    type hw
    card 0
    device 0
}

ctl.!default {
    type hw
    card 0
}

# Define a better software mixer
pcm.dmix_48000 {
    type dmix
    ipc_key 5678293
    ipc_perm 0666
    slave {
        pcm "hw:0,0"
        period_time 0
        period_size 1024
        buffer_size 8192
        channels 2
        rate 48000
    }
    bindings {
        0 0
        1 1
    }
}

# Define an alternate naming scheme that works
pcm.front {
    type plug
    slave.pcm "dmix_48000"
}

pcm.rear {
    type plug
    slave.pcm "dmix_48000"
}

pcm.center_lfe {
    type plug
    slave.pcm "dmix_48000"
}

pcm.side {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround21 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround40 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround41 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround50 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround51 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.surround71 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.iec958 {
    type plug
    slave.pcm "dmix_48000"
}

pcm.spdif {
    type plug
    slave.pcm "dmix_48000"
}

pcm.hdmi {
    type plug
    slave.pcm "dmix_48000"
}

# For microphone input
pcm.dsnoop_48000 {
    type dsnoop
    ipc_key 5778293
    ipc_perm 0666
    slave {
        pcm "hw:3,0"  # USB microphone (usually card 3)
        period_time 0
        period_size 1024
        buffer_size 8192
        channels 2
        rate 48000
    }
    bindings {
        0 0
        1 1
    }
}

# Combined playback and capture
pcm.duplex {
    type asym
    playback.pcm "dmix_48000"
    capture.pcm "dsnoop_48000"
}

# Compatibility with older applications
pcm.dsp {
    type plug
    slave.pcm "duplex"
}

# Additional aliases
pcm.modem {
    type plug
    slave.pcm "dmix_48000"
}

pcm.phoneline {
    type plug
    slave.pcm "dmix_48000"
}
EOL

echo "Restarting ALSA..."
alsactl kill quit
alsactl start

echo
echo "Step 4: Checking virtual environment..."
if [ -d /home/spider/my_venv ]; then
    echo "Found existing virtual environment at /home/spider/my_venv"
    
    # Install Flask into the existing venv
    /home/spider/my_venv/bin/pip install flask

    # Try to fix vilib installation in the existing venv
    echo "Trying to install vilib correctly..."
    /home/spider/my_venv/bin/pip install vilib --upgrade
else
    echo "No virtual environment found at /home/spider/my_venv"
    echo "This script assumes PiCrawler is installed for user 'spider'"
    echo "If using a different user, please install Flask manually:"
    echo "~/my_venv/bin/pip install flask"
fi

echo
echo "Step 5: Setting up camera configuration..."
if [ -f /boot/config.txt ]; then
    # Check if camera support is enabled
    if ! grep -q "^start_x=1" /boot/config.txt; then
        echo "Adding camera support to /boot/config.txt"
        echo "start_x=1" >> /boot/config.txt
    else
        echo "Camera support already enabled in config.txt"
    fi
    
    # Check if camera auto detection is enabled
    if ! grep -q "^camera_auto_detect=1" /boot/config.txt; then
        echo "Adding camera auto detection to /boot/config.txt"
        echo "camera_auto_detect=1" >> /boot/config.txt
    else
        echo "Camera auto detection already enabled in config.txt"
    fi
fi

echo
echo "Setup complete! A reboot is STRONGLY RECOMMENDED to apply all changes."
echo "Please run: sudo reboot"
echo
echo "After reboot, you can start the PiCrawler with:"
echo "cd ~/picrawler/gpt_examples/"
echo "sudo ~/my_venv/bin/python3 gpt_spider.py"
echo 