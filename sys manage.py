# First method: Use the systemctl command 

# Script 1: Restarting a service using systemctl 

import subprocess

service_name = "nginx" # Define the service name

output = subprocess.run(["systemctl", "status", service_name], capture_output=True) # Check the status of the service
status = output.stdout.decode().strip()
print(status)

if "inactive" in status: # Restart the service if it is in a stopped state
  subprocess.run(["systemctl", "restart", service_name])
  print(f"{service_name} service has been restarted")
else:
  print(f"{service_name} service is running")

# OR: stop the service
subprocess.run(["systemctl", "stop", service_name])
print(f"{service_name} service has been stopped")

# OR: start the service
subprocess.run(["systemctl", "start", service_name])
print(f"{service_name} service has been started")

# OR: 

import subprocess

# Run systemctl command and capture output
output = subprocess.check_output("systemctl list-units --type=service --all --no-pager", shell=True).decode()

lines = output.splitlines()

cell_data = []
for line in lines:
    # Skip empty lines or lines that don't contain ".service"
    if ".service" not in line:
        continue
    
    # Split line into cells (assuming cells are separated by multiple spaces)
    cells = line.split()
    
    # Extract cell values
    unit_name = cells[0] if cells[0].endswith(".service") else cells[0] + " " + cells[1]
    load_state = cells[1] if cells[0].endswith(".service") else cells[2]
    active_state = cells[2] if cells[0].endswith(".service") else cells[3]
    sub_state = cells[3] if cells[0].endswith(".service") else cells[4]
    description = ' '.join(cells[4:]) if cells[0].endswith(".service") else ' '.join(cells[5:])
    
    # Append extracted values as a tuple
    cell_data.append((unit_name, load_state, active_state, sub_state, description))

# Example output: 
# Assuming the output of systemctl list-units --type=service --all --no-pager is:

#  UNIT                            LOAD      ACTIVE   SUB     DESCRIPTION
# ● accounts-daemon.service         loaded    active   running Accounts Service
#  alsa-restore.service            loaded    inactive dead    Save/Restore Sound Card State
#  apparmor.service                loaded    active   exited  Load AppArmor profiles

# The cell_data list will be populated as follows:

# cell_data = [
#    ("accounts-daemon.service", "loaded", "active", "running", "Accounts Service"),
#    ("alsa-restore.service", "loaded", "inactive", "dead", "Save/Restore Sound Card State"),
#    ("apparmor.service", "loaded", "active", "exited", "Load AppArmor profiles")
# ]

# Second method: Use the psutil library 

import psutil 

service_name = "nginx"

for proc in psutil.process_iter(): # Check the status of the service
  try:
    if proc.name() == service_name:
      print(f"{service_name} service is running")
  except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    pass

# Restarting a service using psutil 

import psutil
import subprocess

service_name = "nginx"

for proc in psutil.process_iter():
  try:
    if proc_name() == service_name:
      proc.terminate()
      print(f"{service_name} service has been stopped")
      subprocess.run(["systemctl", "start", service_name])
      print(f"{service_name} service has been started")
  except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    pass
