# Write a script that analyzes a directory containing log files. The script should parse each log file, extract
# relevant information (e.g., timestamps, error messages), and generate a summary report or perform specific actions
# based on the log data.

# Input consists of 4 sample log files in .txt format (this could be altered to log) containing the following lines:
# [2023-05-29 10:25:12] INFO: Application started
# [2023-05-29 10:25:15] DEBUG: Connecting to database server
# [2023-05-29 10:25:16] ERROR: Database connection failed - Connection timeout
# [2023-05-29 10:25:18] WARNING: Insufficient disk space - Cleanup required
# [2023-05-29 10:25:22] DEBUG: Initializing application modules
# [2023-05-29 10:25:25] INFO: Application ready

# https://github.com/PacktPublishing/Python-for-Automating-Information-Security/tree/master

import os
import re

timestamp_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
error_pattern = r"ERROR: (.+)"

total_logs = 0
error_logs = 0

directory = '/Users/zvezdochka/Downloads/practical-python/Work/Data'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            log_content = file.read()

            timestamps = re.findall(timestamp_pattern, log_content)
            num_timestamps = len(timestamps)

            error_messages = re.findall(error_pattern, log_content)
            num_error = len(error_messages)

            total_logs += num_timestamps
            error_logs += num_error
            for error_message in error_messages:
                # Perform action for each error message, e.g., send notification, log to database, etc.
                print(f"Error: {error_message} - File: {filename}")

print("Log Analysis Summary")
print("--------------------")
print(f"Total Logs: {total_logs}")
print(f"Error Logs: {error_logs}")
