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
