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
