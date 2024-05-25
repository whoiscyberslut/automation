#!/usr/bin/env python3

# (c) 2021 - Nick Janetakis <nick.janetakis@gmail.com>
# This code is licensed under the MIT license

#This code is original work of nickjj and will be used for personal use during exam, and after that deleted. 
#In case anyone sees this and is curious, you can check out his video explaining the script here: https://nickjanetakis.com/blog/a-python-script-to-increment-file-names-starting-at-a-specific-number

import argparse
import os
import textwrap


def check_path(path):
    if os.path.exists(path):
        return path
    else:
        msg = f'path does not exist: "{path}"'
        raise argparse.ArgumentTypeError(msg)


def check_positive_int(val):
    int_val = int(val)

    if int_val >= 0:
        return int_val
    else:
        msg = f'must be a positive integer: "{val}"'
        raise argparse.ArgumentTypeError(msg)


def get_files(dirname):
    sorted_files = sorted(os.scandir(dirname), key=lambda e: e.name)

    return [f.name for f in sorted_files if f.is_file()]


def inc_by(current_index, dex):
    """
    When adding a new item, you'll end up with a duplicate number before the
    renaming is done. For example, let's say we have:
      01-hi
      02-cool
      03-bye
    And now we want to insert a new item between 02 and 03, as such:
      01-hi
      02-cool
      02-something-else
      03-bye
    We need to increment everything by 1 except when the current file in the
    loop matches the number we want to start renaming from.
    Using the above example, the logic below produces files named like this:
      01-hi
      02-cool
      03-something-else
      04-bye
    This is a pretty limited approach as it only supports adding 1 new file at
    a time. If you added let's say 3 new items at once and wanted to re-index
    everything this function won't properly increment the files.
    """
    amount = 1

    if current_index == start_index:
        amount = 0

    return amount


def increment_files(source_path, dex, delimiter, pad_len, dry_run):
    files = get_files(source_path)

    for index, file in enumerate(files, 1):
        file_name = os.path.basename(file)

        # Let's skip files that don't have the delimiter.
        if delimiter not in file_name:
            continue

        # We only want to split once in case the delimiter is used elsewhere
        # in the file name, ie. 01-hello-world with a - delimiter.
        file_name_parts = file_name.split(delimiter, 1)

        # if we do a = '01-cool-file' in then Python interpreter, and run just a.split('-') with just a delimiter, it would return a list, where each item that was split becomes
        # its own item in the list, like this: ['01', 'cool', 'name']; but, if we do a.split('-', 1), then it is going to split once, like so: ['01', 'cool-name']
        # so we get the prefix, which is the number, and everything else is part of the filename.
  
        prefix = file_name_parts[0]
        # i.e. 01
        name = file_name_parts[1]
        # i.e. cool-name 

        # Let's also ignore any files that happen to contain the prefix but
        # aren't a numbered file, such as: hey-this-file-should-be-skipped
        try:
            prefix_int = int(prefix)
        except ValueError:
            continue

        # Only increment the files we want to.
        increment_amount = 0
        if prefix_int >= dex:
            increment_amount = inc_by(index, dex)

        # zfill pads the string with N number of characters.
        new_prefix = str(prefix_int + increment_amount).zfill(pad_len)
        new_file_name = f'{new_prefix}{delimiter}{name}'

        if dry_run:
            print(f'{file_name} -> {new_file_name}')
        else:
            os.rename(file_name, new_file_name)

    return None


def parseargs():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Increment file prefixes starting at a specific index.'''))

    parser.add_argument('path', default=None,
                        metavar='PATH', type=check_path,
                        help='source path to look for files')

    parser.add_argument('-i', '--index', type=check_positive_int,
                        metavar='VAL', required=True,
                        help='start incrementing at this prefix number')

    parser.add_argument('-d', '--delimiter', type=str, default='-',
                        metavar='str',
                        help='prefix delimiter (defaults to a hyphen)')

    parser.add_argument('-p', '--pad-len', type=check_positive_int,
                        metavar='VAL', required=True,
                        help='pad prefixes by this amount of zeros')

    parser.add_argument('-n', '--dry-run', action='store_true',
                        help='print the results instead of renaming the files')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parseargs()

    increment_files(args.path, args.index, args.delimiter, args.pad_len,
                    args.dry_run)

#setup.sh 
# 1. Create the file inc-file-names anywhere on your dev box
#touch inc-file-names

# 2. Make it executable
#chmod +x inc-file-names

# 3. Copy the script below into the file you just created

# 4. Move it onto your system path
#sudo mv inc-file-names /usr/local/bin

# 5. Verify it works
#inc-file-names --help

# -------------------------------
# An example of using the script:
# -------------------------------

# Create a temporary directory to mess around in
#mkdir /tmp/inctest
#cd /tmp/inctest

# Set up a few sample files to test the script with
#touch 1-hello 2-another-title 3-another-new-file 4-this-happened \
#      5-check-that-out 6-very-cool 7-yeah-that-exists 8-seriously 9-the-end

# Add a new file in the middle of the list
#touch 3-just-adding-another-file

# Increment the files (remove the -n to not do a dry run)
#inc-file-names . -i 3 -p 2 -n

# Remove the temporary directory
#rm -rf /tmp/inctest
