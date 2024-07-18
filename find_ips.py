"""
This python script parses all files in a directory (passed as argument) and its subdirectories and
prints all valid IP addresses found in the files in sorted order.
If directory name is not passed it will parse all files in the current directory and its subdirectories.
Usage: 
   find_ip.py [<DIR>]
   find_ip.py -h | --help
Options:
  -h --help  Show this screen.
"""

# This script is original work of @deoluoyinlola. It will be used for personal purposes and removed from the repo afterwards. 

import re
from pathlib import Path
from docopt import docopt

ip_candidates = []
text_content = ""
SEARCH_DIR = "."

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["<DIR>"] != None:
        SEARCH_DIR = arguments["<DIR>"]

def find_ip_in_text(text):
    return re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", text)

def find_all_ip_in_dir(dir_name):
    entries = Path(dir_name)
    for entry in entries.iterdir():
       if entry.is_file():
           with open(entry) as f:
              textcontent = f.read()
              ip_candidates.extend(find_ip_in_text(textcontent))
       elif entry.is_dir():
           find_all_ip_in_dir(entry)

find_all_ip_in_dir(SEARCH_DIR)

for ip in sorted(ip_candidates):
    print(ip)
