# Regex 

text = "The quick brown fox jumps over the lazy dog." # Sample text
pattern = r"quick.*fox" # Define a regex pattern


# Breakdown: 
# (1) Quick mathes the exact substring "quick" 
# (2) .* is a wildcard that matched any character (except a newline) zero or more times
# (3) Fox matches the exact substring "fox"
# Thus, quick.*fox will match any substring that starts with "quick" and ends with "fox" with any characters in between

match = re.search(pattern, text) # Search for the pattern in the text

if match:
  # If a match is found, print the matched portion 
  matched_text = match.group()
  print(f"Match found: '{matched_text}'"}
  else:
    print("No match found.")
    

# Example 1: Sanitise illegal characters for filename and replace them with "_".

import re
in = '' # string here
query = r"^[ .]|[/<>:\"\\|?*]+|[ .]$"
illegal_char = re.findall(query, in)

if len(illegal_char) == 0:
	return
else:
	print(f"filename contains illegal characters:\n {illegal_char}\n replacing with \"_\"")
	in = re.sub(query, "_", in)

# Example 2: Parse filenames of anime episodes from a text file names filenames.txt and rename filenames with the episode number (without changing the extension).

'''
Contents example:

    [AW] One Piece - 629 [1080P][Dub].mkv
    EP.585.1080p.mp4
    EP609.m4v
    EP 610.m4v
    One Piece 0696 A Tearful Reunion! Rebecca and Kyros!.mp4
    One_Piece_0745_Sons'_Cups!.mp4
    One Piece - 591 (1080P Funi Web-Dl -Ks-)-1.m4v
    One Piece - 621 1080P.mkv
    One_Piece_S10E577_Zs_Ambition_A_Great_and_Desperate_Escape_Plan.mp4

Expected output:
    609.m4v
    610.m4v
    585.mp4
    621.mkv
    629.mkv
    745.mp4 (or) 0745.mp4
    696.mp4 (or) 0696.mp4
    591.m4v
    577.mp4
''' 

'''
Output:
609.m4v
610.m4v
585.mp4
621.mkv
629.mkv 
745.mp4
696.mp4
591.m4v
577.mp4
'''

# Method 2:

import re
import os

with open('filenames.txt', 'r') as f:
  files = f.read().splitlines()

p = re.compile(r'0?(\d{3})')

for file in files:
  if m := p.search(file):
    episode_number = m.group(1) 
    extension = file.split('.')[-1]
    new_filename = f"{episode_number}.{extension}"
    os.rename(file, new_filename)
    print(f"Renamed '{file}' to '{new_filename}'")
  else:
    print(f"No episode number found in '{file}', skipping.")

# Method 3:

import os
import re

for file in os.listdir(path="/full/path/to/folder"):
  for match_obj in re.finditer(r'\d{3,4}', file): # searches for the first 3 or 4 digit number less than 1000 for each line
    episode = match_obj.group(0)
    if int(episode) < 1000:
      new_filename = episode.lstrip('0') + '.' + file.split('.')[-1]
      old_name = "/full/path/to/folder" + file
      new_name = "/full/path/to/folder" + new_filename
      os.rename(old_name, new_name)
      break #  go to next file if ep found (avoid the else clause)
  else:
    pass # if episode not found, just leave the filename as it is; executes if no valid episode number is found, doing nothing in this case.

# Example 3: Filtering files based on a pattern

import os
import re

def get_files_matching_pattern(directory, pattern):
  files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
  matching_files = [f for f in files if re.search(pattern, f)]
  return matching_files

# Example usage:

directory = '/path/to/data'
pattern = r'.*\.csv$'  
csv_files = get_files_matching_pattern(directory, pattern)

# Example 4: Extract only the valid IPv4 addresses from file names

import re
import os 

ip_list = [ip for file in os.list('.') for ip in re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file)]
print(ip_list)

# Example 4: Organise image files

import re

regex = re.compile(r'^IMG_(\d{4})(\d{2}))(\d{2})_(\d{2})(\d{2})(\d{2})\.jpeg$')
oldstr = 'IMG_20190401_235959.jpeg'
match = regex.match(oldstr)
newstr = '{}--{}--{}_{}_{}.jpg.format(*match.groups())
print(newstr) # 2019-04-01_29_59.jpg

url_regex = (http)?s?\:?\/?\/?\/?(www\.)?[a-zA-Z0-9]+\.com

# Email in a log file: [a-zA-Z0-9-.]+\@[a-z-]+\.[a-z]+
