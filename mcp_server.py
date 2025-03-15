#!/usr/bin/env python
"""
MCP Server for Picrawler SSH Connection
This script provides a simple interface to connect to the Picrawler device via SSH.
It stores connection details and provides a convenient way to establish SSH connections.
"""

import os
import sys
import subprocess
import platform
import json
import paramiko
import time
from pathlib import Path

class MCPServer:
    def __init__(self, config_file=None):
        self.config_file = config_file or str(Path.home() / "picrawler_mcp_config.json")
        self.config = {
            "device_ip": "192.168.1.248",
            "username": "spider",
            "password": "21076991",
            "ssh_port": 22,
            "putty_path": self._find_putty()
        }
        self.load_config()
    
    def _find_putty(self):
        """Find PuTTY executable on Windows systems"""
        if platform.system() != "Windows":
            return None
            
        common_paths = [
            r"C:\Program Files\PuTTY\putty.exe",
            r"C:\Program Files (x86)\PuTTY\putty.exe",
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
        
        return None
    
    def load_config(self):
        """Load configuration from file if it exists"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    saved_config = json.load(f)
                    self.config.update(saved_config)
        except Exception as e:
            print(f"Error loading config: {e}")
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            print(f"Configuration saved to {self.config_file}")
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def update_config(self, **kwargs):
        """Update configuration with new values"""
        self.config.update(kwargs)
        self.save_config()
    
    def connect_with_putty(self):
        """Launch PuTTY with the saved connection details"""
        if platform.system() != "Windows":
            print("PuTTY launch is only supported on Windows.")
            return False
        
        putty_path = self.config.get("putty_path")
        if not putty_path or not os.path.exists(putty_path):
            print("PuTTY not found. Please specify the correct path in the configuration.")
            return False
        
        # Construct PuTTY command line
        cmd = [
            putty_path,
            "-ssh",
            f"{self.config['username']}@{self.config['device_ip']}",
            "-P", str(self.config['ssh_port']),
            "-pw", self.config['password']
        ]
        
        try:
            # Start PuTTY process
            subprocess.Popen(cmd)
            print(f"Connecting to {self.config['username']}@{self.config['device_ip']} using PuTTY...")
            return True
        except Exception as e:
            print(f"Error launching PuTTY: {e}")
            return False
    
    def connect_with_paramiko(self):
        """Establish SSH connection using Paramiko library"""
        print(f"Connecting to {self.config['username']}@{self.config['device_ip']} via SSH...")
        
        try:
            # Create SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connect to the device
            client.connect(
                hostname=self.config['device_ip'],
                port=self.config['ssh_port'],
                username=self.config['username'],
                password=self.config['password'],
                timeout=10
            )
            
            # Create interactive shell
            channel = client.invoke_shell()
            print("Connected! Interactive SSH session established.")
            print("Press Ctrl+C to exit.")
            
            # Interactive session loop
            while True:
                if channel.recv_ready():
                    output = channel.recv(1024).decode('utf-8')
                    sys.stdout.write(output)
                    sys.stdout.flush()
                
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    user_input = sys.stdin.read(1)
                    channel.send(user_input)
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\nConnection terminated by user.")
        except Exception as e:
            print(f"Error connecting via SSH: {e}")
        finally:
            if 'client' in locals():
                client.close()
                print("SSH connection closed.")
    
    def test_connection(self):
        """Test SSH connection to the device"""
        print(f"Testing connection to {self.config['username']}@{self.config['device_ip']}...")
        
        try:
            # Create SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connect to the device
            client.connect(
                hostname=self.config['device_ip'],
                port=self.config['ssh_port'],
                username=self.config['username'],
                password=self.config['password'],
                timeout=10
            )
            
            # Execute a simple command
            stdin, stdout, stderr = client.exec_command('hostname')
            hostname = stdout.read().decode('utf-8').strip()
            
            print(f"Connection successful! Device hostname: {hostname}")
            client.close()
            return True
            
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def show_menu(self):
        """Display interactive menu"""
        while True:
            print("\n===== Picrawler MCP Server =====")
            print(f"Device: {self.config['username']}@{self.config['device_ip']}")
            print("1. Connect using PuTTY")
            print("2. Test connection")
            print("3. Update connection settings")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ")
            
            if choice == "1":
                self.connect_with_putty()
            elif choice == "2":
                self.test_connection()
            elif choice == "3":
                self.update_settings()
            elif choice == "4":
                print("Exiting MCP Server.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def update_settings(self):
        """Interactive menu to update connection settings"""
        print("\n=== Update Connection Settings ===")
        print("Leave field empty to keep current value")
        
        ip = input(f"Device IP [{self.config['device_ip']}]: ")
        if ip:
            self.config['device_ip'] = ip
            
        username = input(f"Username [{self.config['username']}]: ")
        if username:
            self.config['username'] = username
            
        password = input(f"Password [********]: ")
        if password:
            self.config['password'] = password
            
        port = input(f"SSH Port [{self.config['ssh_port']}]: ")
        if port:
            try:
                self.config['ssh_port'] = int(port)
            except ValueError:
                print("Invalid port number. Keeping current value.")
        
        if platform.system() == "Windows":
            putty_path = input(f"PuTTY Path [{self.config.get('putty_path', 'Not set')}]: ")
            if putty_path:
                if os.path.exists(putty_path):
                    self.config['putty_path'] = putty_path
                else:
                    print("Path does not exist. Keeping current value.")
        
        self.save_config()

if __name__ == "__main__":
    # Check for required modules
    try:
        import select
        import paramiko
    except ImportError:
        print("Required modules not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "paramiko"])
        import select
        import paramiko

    # Start MCP Server
    server = MCPServer()
    server.show_menu() 