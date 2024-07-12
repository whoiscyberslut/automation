#!/usr/bin/env python3
"""
USAGE:
apache_log_parser.py some_log_file

This script takes one command line argument: the name of a log file to parse.
It then parses the log file and generates a report which associates remote hosts
with the total number of bytes transferred to them.
"""

import sys

def dictify_logline(line):
    """
    Return a dictionary of the pertinent pieces of an apache combined log file.
    Currently, the only fields we are interested in are remote host and bytes sent,
    but we are putting status in there just for good measure.
    """
    split_line = line.split()
    return {
        'remote_host': split_line[0],
        'status': split_line[8],
        'bytes_sent': split_line[9],
    }

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
        
        # Populate report_dict with remote_host as key and list of bytes_sent as value
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    
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
