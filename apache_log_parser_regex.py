#!/usr/bin/env python3
"""
USAGE:
apache_log_parser_regex.py some_log_file

This script parses an Apache combined log file and generates a report
associating remote hosts with the total number of bytes transferred to them.
"""

import sys
import re

log_line_re = re.compile(r'''
    (?P<remote_host>\S+)       # IP ADDRESS
    \s+                         # whitespace
    \S+                         # remote logname (not captured)
    \s+                         # whitespace
    \S+                         # remote user (not captured)
    \s+                         # whitespace
    \[[^\[\]]+\]                # time (not captured)
    \s+                         # whitespace
    "[^"]+"                     # first line of request (not captured)
    \s+                         # whitespace
    (?P<status>\d+)             # status code
    \s+                         # whitespace
    (?P<bytes_sent>-|\d+)       # bytes sent or '-' if not available
    \s*                         # optional whitespace
''', re.VERBOSE)

def dictify_logline(line):
    """
    Return a dictionary of the pertinent pieces of an apache combined log file.
    Currently, the only fields we are interested in are remote host, status, and bytes sent.
    """
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict['bytes_sent'] == '-':
            groupdict['bytes_sent'] = '0'
        return groupdict
    else:
        return {'remote_host': None, 'status': None, 'bytes_sent': "0"}

def generate_log_report(logfile):
    """
    Return a dictionary of format remote_host => [list of bytes sent].
    This function takes a file object, iterates through all the lines in the file,
    and generates a report of the total number of bytes transferred to each remote host.
    """
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            # Ignore lines where bytes_sent is not a valid integer
            continue
        
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    
    return report_dict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.strip())
        sys.exit(1)
    
    infile_name = sys.argv[1]
    
    try:
        with open(infile_name, 'r') as infile:
            log_report = generate_log_report(infile)
            print(log_report)
    except FileNotFoundError:
        print(f"Error: File '{infile_name}' not found.")
        sys.exit(1)
