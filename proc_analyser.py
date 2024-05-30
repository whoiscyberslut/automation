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
