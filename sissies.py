# With the help of the sys module, arguments can be passed to the Python scripts

import sys 

print('\n')
print('The name of the script is: %s' %sys.argv[0]) # name of the script
print('The input to the script is: %s' %sys.argv[1]) # argument passed by user

