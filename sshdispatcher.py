#!/usr/bin/env python3

import subprocess

"""
A SSH-based command dispatch system
"""

machines = ["10.0.1.40", "10.0.1.50", "10.0.1.51", "10.0.1.60", "10.0.1.80"]
cmd = "uname" # or cmd = "python /src/fingerprint.py"

for machine in machines:
    try:
        subprocess.check_call(f"ssh root@{machine} {cmd}", shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command on {machine}: {e}")
    except Exception as e:
        print(f"An error occurred with {machine}: {e}")

# OR: 

#!/usr/bin/env python3

import subprocess
import configparser

"""
A SSH-based command dispatch system
"""

def read_config(file="config.ini"):
    """
    Extract IP addresses and commands from the config file and return them as a tuple.
    """
    ips = []
    cmds = []
    config = configparser.ConfigParser()
    config.read(file)
    
    if 'MACHINES' in config and 'COMMANDS' in config:
        machines = config.items("MACHINES")
        commands = config.items("COMMANDS")
        for _, ip in machines:
            ips.append(ip)
        for _, cmd in commands:
            cmds.append(cmd)
    else:
        raise ValueError("Config file must contain 'MACHINES' and 'COMMANDS' sections")

    return ips, cmds

def execute_commands(ips, cmds):
    """
    For every IP address, run all commands.
    """
    for ip in ips:
        for cmd in cmds:
            try:
                result = subprocess.run(["ssh", f"root@{ip}", cmd], check=True, capture_output=True, text=True)
                print(f"Output from {ip}:\n{result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"Command '{cmd}' failed on {ip} with error:\n{e.stderr}")
            except Exception as e:
                print(f"An error occurred with {ip}: {e}")

if __name__ == "__main__":
    try:
        ips, cmds = read_config()
        execute_commands(ips, cmds)
    except Exception as e:
        print(f"An error occurred: {e}")
