ip_regex = r'(?<!\d)(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?!\d)'

'''
[ip for ip in ip_addresses if ip == ip_address] # iterates over each element (ip) in the ip_addresses list and filters out only those elements that are equal to the current ip_address; so, for each ip_address in 
the list this expression creates a list containing only occurrences of that ip_address
len(...): this calculates the length of the list generated by the list comprehension. In other words, it counts how many elements are in the list that contains only occurrences of the current ip_address.

So, altogether len([ip for ip in ip_addresses if ip == ip_address]) calculates how many times the current ip_address appears in the ip_addresses list. This value represents the number of files associated with that 
ip_address.
'''