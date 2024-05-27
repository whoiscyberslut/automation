# Python script that parses the filenames of files in a particular directory, separates them into groups according to the fields within the file names, and performs operations within these groups. The filenames follow,
# the convention PROJECT-x-SUBJECT-x-SESSION-x-TYPE.extension, where -x- serves as a field divider. The goal is to be able to perform operations on every group of files that shares the same PROJECT-x-SUBJECT-x-SESSION 
# component.

# Method 1: Using defaultdict to make a dictionary that contains lists

from collections import defaultdict 

groups = defaultdict(list)

for filename in os.listdir(directory):
  basename,extension = os.path.splitext(filename)
  project, subject, session, ftype = basename.split('-x-')
  groups[session].append(filename) # Now, groups contain a mapping between session names and filenames

# Method 2: Using defaultdict to group filenames, glob to find the appropriate files, and fileinput to red lines from all files with the same key

import os
from glob import glob
import fileinput
from collections import defaultdict

filenames = glob('*-x-*')

dd = defaultdict(list)

for filename in filenames:
  name, ext = os.path.splitext(filename)
  dd[tuple(name.split('*-x-*'[:3])].append(filename)
for key, fnames in dd.iteritems():
  for line in fileinput.FileInput(fnames): # uses fileinput to read lines from all files in the group as if they were a single file
    pass # do something with lines from files with the same key

