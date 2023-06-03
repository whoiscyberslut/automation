# Write a script that processes text files in a directory. The script could perform tasks like word counting, finding specific patterns or 
# keywords, generating statistics (e.g., line count, word frequency), or applying text transformations (e.g., converting to uppercase or lowercase).

import os
import re
from collections import Counter

directory = "path/to/text/files/directory"

# Track statistics
total_files = 0
total_lines = 0
word_count = Counter()

# Process each text file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            # Read the contents of the file
            text = file.read()

            # Count the lines in the file
            lines = text.split("\n")
            num_lines = len(lines)
            total_lines += num_lines

            # Count the words in the file
            words = re.findall(r"\w+", text)
            word_count.update(words)

            # Perform specific tasks on the text file
            # Example: Convert text to uppercase
            # modified_text = text.upper()
            # print(modified_text)

        total_files += 1

# Print statistics
print("Text Processing Summary")
print("-----------------------")
print(f"Total Files: {total_files}")
print(f"Total Lines: {total_lines}")
print(f"Total Words: {sum(word_count.values())}")

# Print word frequency
print("\nWord Frequency:")
for word, count in word_count.most_common(10):
    print(f"{word}: {count}")
