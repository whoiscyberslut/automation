#!/usr/bin/env python3

# This code is original work of @abdullahzamanbabar. It will be used for personal purposes and removed from the repo afterwards.

import csv
import re
import operator

# error initializers
error_list=[]
error = {}
error_key=["Error","Count"]
error_pattern=r"ERROR ([\w ']*)"

# user initializers
names = set()
user_error = {}
user_info = {}
user_list = []
user_key = ["Username","INFO","ERROR"]
user_pattern = r"ticky: ([A-Z]*) ([\w ']*) [[\[\d+#\] ]*]?\(([a-z.]*)\)"

# Parsing the syslog.log file for error reports

with open("syslog.log") as file:
    for line in file:
        result = re.search(error_pattern,line)
        if result is None:
            continue
        error[result.group(1).strip()] = error.get(result.group(1).strip(), 0) + 1

error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

# Creating a list of dictionaries for error reports  

for item in error:
    d = {"Error":item[0],"Count":item[1]}
    error_list.append(d)

# Creating a CSV file for the error messages
    
with open("error_message.csv","w") as file:
    f = csv.DictWriter(file,fieldnames=error_key)
    f.writeheader()
    f.writerows(error_list)

# Parsing the syslog.log file for counting the number of errors and users 

with open('syslog.log') as file:
    for line in file:
        result = re.search(user_pattern,line)
        if result is None:
            continue
        names.add(result.group(3))
        if result.group(1) == "ERROR":
            user_error[result.group(3)] = user_error.get(result.group(3), 0) + 1
        elif result.group(1) == "INFO":
            user_info[result.group(3)] = user_info.get(result.group(3), 0) +1

# Removing repeated items
            
for item in names:
    if item not in user_error:
        user_error[item] = 0
    if item not in user_info:
        user_info[item] = 0

user_info=sorted(user_info.items(),key=operator.itemgetter(0))
user_error=sorted(user_error.items(),key=operator.itemgetter(0))

# Creating a list of dictionaries

for item in user_info:
    for itm in user_error:
        if itm[0]==item[0]:
            d = {"Username":item[0],"INFO":item[1],"ERROR":itm[1]}
            user_list.append(d)
            
# Creating a CSV file to write to csv_to_html.py

with open("user_statistics.csv","w") as file:
    f = csv.DictWriter(file,fieldnames=user_key)
    f.writeheader()
    f.writerows(user_list)
