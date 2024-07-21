#!/usr/bin/env python3

import os
from collections import defaultdict

def parse_process_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        process_lines = [line.strip() for line in lines[12:] if line.strip()]
        user_processes_count = defaultdict(int)
        sh_files_count_by_user = defaultdict(int)

        total_processes = 0
        sh_files = 0

        for line in process_lines:
            parts = line.split()
            if len(parts) >= 32:
                user = parts[30]
                pid = parts[0]
                command = parts[1]
                total_processes += 1
                user_processes_count[user] += 1

                if command.endswith('.sh'):
                    sh_files += 1
                    sh_files_count_by_user[user] += 1

        user_processes = {user:count for user, count in user_processes_count.items()}

        return total_processes, user_processes, sh_files, sh_files_count_by_user

if __name__ == "__main__":
    filepath = 'top.txt'
    total_processes, user_processes, sh_files, sh_files_count_by_user = parse_process_file(filepath)

    print(f"Total number of processes: {total_processes}")
    print(f"Number of .sh files currently running: {sh_files}")

    # Display processes per user
    for user, count in user_processes.items():
        print(f"Number of processes running under user '{user}': {count}")

    # Display .sh files count per user
    for user, count in sh_files_count_by_user.items():
        print(f"Number of .sh files running under user '{user}': {count}")

# Try to save the output of the 'top' commmand to a file:

import subprocess

## use the following where appropriate within your loop
with open("ss.txt", "w") as outfile:
  subprocess.call("top -n1 -p 2948", shell=True, stdout=outfile)
