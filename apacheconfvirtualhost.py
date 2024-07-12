#!/usr/bin/env python3
# Script that parses through an Apache config file, finds a specified VirtualHost section, and replaces the DocumentRoot for that VirtualHost.
# Usage: python3 apache_conf_docroot_replace.py /etc/apache2/sites-available/psa local2:80 /tmp

import re
import sys

# Regular expressions
vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
docroot_re = re.compile(r'(DocumentRoot\s+)(\S+)')

def replace_docroot(conf_string, vhost, new_docroot):
    '''Yield new lines of an httpd.conf file where docroot lines matching
    the specified vhost are replaced with the new_docroot.'''
    in_vhost = False
    curr_vhost = None

    # Split the configuration string into lines
    conf_lines = conf_string.splitlines()

    for line in conf_lines:
        # Check for <VirtualHost> start tag
        if not in_vhost:
            vhost_start_match = vhost_start.search(line)
            if vhost_start_match:
                curr_vhost = vhost_start_match.group(1)
                in_vhost = True
        
        # Replace DocumentRoot if inside the target VirtualHost block
        if in_vhost and curr_vhost == vhost:
            docroot_match = docroot_re.search(line)
            if docroot_match:
                line = docroot_re.sub(r'\1%s' % new_docroot, line)
        
        # Check for </VirtualHost> end tag
        if in_vhost:
            if '</VirtualHost' in line:
                in_vhost = False
        
        yield line

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 replace_docroot.py <conf_file> <vhost> <new_docroot>")
        sys.exit(1)

    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    new_docroot = sys.argv[3]

    try:
        with open(conf_file, 'r') as f:
            conf_string = f.read()
    except FileNotFoundError:
        print(f"Error: File '{conf_file}' not found.")
        sys.exit(1)

    # Replace DocumentRoot and print the modified configuration
    for line in replace_docroot(conf_string, vhost, new_docroot):
        print(line)
