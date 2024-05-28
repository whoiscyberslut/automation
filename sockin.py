import socket 

try:
  domain = "google.com"
  ipdom = socket.gethostbyname(domain)   # Check IP address of a website
  print(f"IP address of {domain} is: {ipdom}")
  host = socket.gethostname()  # Getting the hostname
  ip = socket.gethostbyname(host)  # Getting the IP address of the host
  print(f"IP address: {ip}")
  print(f"Hostname: {host}")
except:
  print("An error occurred.")


# Using requests module to downoad any web page

import requests

producturl = "http://100daysofdevops.com/"  
  
res = requests.get(producturl, timeout = 5) # save output to a variable  
print(res)
print(res.text) # -> complete web page
