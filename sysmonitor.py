# Using Python's psutil library to access information about CPU usage, memory consumption, disk usage, and network statistics.

import psutil 

# Get CPU information 
cpu_percent = psutil.cpu_percent() 
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()

# Get memory information 
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
# Print memory usage %
print(f"Memory usage: {virtual_memory.percent}")

# Get disk usage information
disk_usage = psutil.disk_usage('/')
# Print disk usage %
print(f"Disk usage: {disk_usage.percent}")

# Get network information
net_io = psutil.net_io_counters()

# Get process information
proceses = psutil.process_iter(['pid', 'name', 'username'])
print("Running processes: ")
for process in processes:
  print(f"PID: {process.info['pid'], Name: {process.info['name']), User: {process.info['username']}")
