def getlistofprocessesortedbymemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listofprocobjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listofprocobjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    # Sort list of dict by key vms i.e. memory usage
    listofprocobjects = sorted(listofprocobjects, key=lambda procobj: procobj['vms'], reverse=True)

    return listofprocobjects

# OR:

#!/usr/bin/env python
import psutil
processes = []
for proc in psutil.process_iter(['pid']):
    p = psutil.Process(pid=proc.pid)
    processes.append(p.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent']))
print("--------------------Top 5 by CPU---------------------------------")
cpu = sorted(processes, key=lambda i: i['cpu_percent'], reverse=True)
count = 0
while (count < 5):   
    count = count + 1
    print(cpu[count])

