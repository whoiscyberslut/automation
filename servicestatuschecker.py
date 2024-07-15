import os
import subprocess

def check_service_status(services, log_file):
    with open(log_file, 'w') as log:
        for service in services:
            result = subprocess.run(['systemctl', 'is-active', service], capture_output=True, text=True)
            status = result.stdout.strip()
            log.write(f"{service}: {status}\n")
            print(f"{service}: {status}")

services = ['nginx', 'mysql', 'ssh']
log_file = '/path/to/service_status.log'

check_service_status(services, log_file)
