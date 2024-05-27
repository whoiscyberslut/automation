# Argument parsing using argparse

import argparse
ap = argparse.ArgumentParser() # Construct the argument parser

# Add the arguments to the parser 
ap.add_argument("-d", "--foperand", required=True,
                help="first operand")
ap.add_argument("-b", "--soperand", required=True, 
                help="second operand")
args = vars(ap.parse_args())

# Calculate the sum 
print("Sum is {}".format(int(args['foperand']) + int(args['soperand'])))
