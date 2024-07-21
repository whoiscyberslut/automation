#!/usr/bin/env python3

import os

def parse_process_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

        # Skip the header line and strip whitespace from each line
        process_lines = [line.strip() for line in lines[1:] if line.strip()]

        # Extract PIDs and filenames
        pids = []
        sh_files = 0
        for line in process_lines:
            parts = line.split()
            if len(parts) > 1:
                pid = parts[0]
                filename = parts[1]
                pids.append(pid)
                if filename.endswith('.sh'):
                    sh_files += 1

        total_processes = len(pids)
        # Since user info is not available in the file, we assume all processes belong to the current user.
        user_processes = total_processes

        return total_processes, user_processes, sh_files

if __name__ = "__main__":
    filepath = 'processes.txt'
    total_processes, user_processes, sh_files = parse_process(filepath)

    print(f"Total number of processes: {total_processes}")
    print(f"Number of processes running under the current user: {user_processes}")
    print(f"Number of .sh files currently running: {sh_files}")

# OR: if users are different

#!/usr/bin/env python3

import os
from collections import defaultdict

def parse_process_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

        # Skip the header line and strip whitespace from each line
        process_lines = [line.strip() for line in lines[1:] if line.strip()]

        # Initialize counters and user process tracking
        user_processes_count = defaultdict(int)
        sh_files_count_by_user = defaultdict(int)

        total_processes = 0
        sh_files = 0

        for line in process_lines:
            parts = line.split()
            if len(parts) >= 3:
                user = parts[0]
                pid = parts[1]
                filename = parts[2]

                # Increment total process count
                total_processes += 1
                user_processes_count[user] += 1

                # Check if the file is a .sh file
                if filename.endswith('.sh'):
                    sh_files += 1
                    sh_files_count_by_user[user] += 1

        # Total processes per user
        user_processes = {user: count for user, count in user_processes_count.items()}

        return total_processes, user_processes, sh_files, sh_files_count_by_user

if __name__ == "__main__":
    filepath = 'processes.txt'
    total_processes, user_processes, sh_files, sh_files_count_by_user = parse_process_file(filepath)

    print(f"Total number of processes: {total_processes}")
    print(f"Number of .sh files currently running: {sh_files}")
    
    # Display processes per user
    for user, count in user_processes.items():
        print(f"Number of processes running under user '{user}': {count}")

    # Display .sh files count per user
    for user, count in sh_files_count_by_user.items():
        print(f"Number of .sh files running under user '{user}': {count}")
