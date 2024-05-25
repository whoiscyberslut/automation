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
  
