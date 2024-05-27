#

# Using Python's os module to execute system functions 

import os

logheader = os.popen('echo "Capturing logs for $HOSTNAME on `date`" > %s ; echo "\n"' #  logfilepath, 'w')
