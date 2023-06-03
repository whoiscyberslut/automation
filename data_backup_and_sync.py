# Create a script that performs regular backups and synchronizes files between two directories. The script should
# compare the contents of the source and destination directories, identify differences, and copy/update files as needed
# to ensure both directories are in sync.

import filecmp
from dirsync import sync
import os.path
from filecmp import dircmp

source_directory = '/Users/zvezdochka/Downloads/practical-python/Work/Data/'
destination = '/Users/zvezdochka/Downloads/practical-python/Work/'

def main(dir1, dir2):
    result = filecmp.dircmp(dir1, dir2)
    result.report()
    sync(dir1, dir2, 'sync')
#   sync(dir2, dir1, 'sync') - for syncing the opposite way

main(source_directory, destination)

