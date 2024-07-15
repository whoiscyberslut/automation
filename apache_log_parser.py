#!/usr/bin/env python3
"""
USAGE:
apache_log_parser.py some_log_file

This script takes one command line argument: the name of a log file to parse.
It then parses the log file and generates a report which associates remote hosts
with the total number of bytes transferred to them.
"""

import sys

def parse_log_line(line):
    """
    Parse a single log line and return the remote host and bytes sent.
    """
    parts = line.split()
    return parts[0], parts[9]

def generate_log_report(logfile):
    """
    Generate a report of total bytes transferred per remote host from the log file.
    """
    report = {}
    for line in logfile:
        remote_host, bytes_sent = parse_log_line(line)
        try:
            bytes_sent = int(bytes_sent)
        except ValueError:
            continue
        if remote_host in report:
            report[remote_host] += bytes_sent
        else:
            report[remote_host] = bytes_sent
    return report

def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    infile_name = sys.argv[1]
    try:
        with open(infile_name, 'r') as infile:
            log_report = generate_log_report(infile)
            for host, total_bytes in log_report.items():
                print(f"{host}: {total_bytes} bytes")
    except IOError:
        print(f"Could not read file: {infile_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Example input:

# 127.0.0.1 - - [10/Jul/2023:22:14:15 +0000] "GET /index.html HTTP/1.1" 200 1043
# 92.168.1.1 - - [10/Jul/2023:22:14:16 +0000] "GET /about.html HTTP/1.1" 200 2048
# 127.0.0.1 - - [10/Jul/2023:22:14:17 +0000] "POST /submit-form HTTP/1.1" 200 512
# 10.0.0.1 - - [10/Jul/2023:22:14:18 +0000] "GET /contact.html HTTP/1.1" 200 1024
# 192.168.1.1 - - [10/Jul/2023:22:14:19 +0000] "GET /home.html HTTP/1.1" 200 4096
# 127.0.0.1 - - [10/Jul/2023:22:14:20 +0000] "GET /index.html HTTP/1.1" 404 -

# OR: As a single function

#!/usr/bin/env python3
"""
USAGE:
apache_log_parser.py some_log_file

This script takes one command line argument: the name of a log file to parse.
It then parses the log file and generates a report which associates remote hosts
with the total number of bytes transferred to them.
"""

import sys

def generate_log_report(logfile):
    """
    Return a dictionary of format remote_host => total bytes sent.
    This function takes a file object, iterates through all the lines in the file,
    and generates a report of the total number of bytes transferred to each remote host.
    """
    report_dict = {}
    for line in logfile:
        split_line = line.split()
        remote_host = split_line[0]
        bytes_sent_str = split_line[9]
        
        try:
            bytes_sent = int(bytes_sent_str)
        except ValueError:
            # Ignore lines where bytes_sent is not a valid integer
            continue
        
        if remote_host in report_dict:
            report_dict[remote_host] += bytes_sent
        else:
            report_dict[remote_host] = bytes_sent
    
    return report_dict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    
    infile_name = sys.argv[1]
    
    try:
        with open(infile_name, 'r') as infile:
            log_report = generate_log_report(infile)
            print(log_report)
    except IOError:
        print(f"You must specify a valid file to parse: {infile_name}")
        print(__doc__)
        sys.exit(1)
