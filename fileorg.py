import os
import shutil

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic', '.nef','.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv','.mov'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar'],
    'Others': [],  # For any other file type
    'Duplicates': []  # For duplicate files
}

def move_file(source, destination):
    try:
        # Check if the destination file already exists
        if os.path.exists(destination):
            # If it exists, create a "Duplicates" folder in the same directory
            duplicates_folder = os.path.join(os.path.dirname(destination), 'Duplicates')
            if not os.path.exists(duplicates_folder):
                # Create the "Duplicates" folder if it doesn't already exist
                os.makedirs(duplicates_folder)
            # Generate the destination path for the duplicate file
            duplicate_destination = os.path.join(duplicates_folder, os.path.basename(destination))
            # Move the source file to the duplicate destination
            shutil.move(source, duplicate_destination)
            # Print a message indicating that a duplicate file was detected and moved
            print(f"Duplicate file detected: {source} moved to {duplicate_destination}")
        else:
            # If the destination doesn't exist, move the source file to the destination
            shutil.move(source, destination)
        # Return True to indicate successful file movement
        return True
    except Exception as e:
        # If any error occurs during file movement, print an error message and return False
        print(f"Error moving file from {source} to {destination}: {e}")
        return False


def organize_files(root_dir):
    # Create a dictionary to store the file counts for each file type
    file_counts = {file_type: 0 for file_type in file_types}

    # Traverse the directory tree starting from root_dir
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Iterate over the files in the current folder
        for filename in filenames:
            # Get the file extension of the current file
            file_extension = os.path.splitext(filename)[1]
            # Initialize a flag to track if the file has been moved
            file_moved = False

            # Iterate over the file types and their associated extensions
            for file_type, extensions in file_types.items():
                # Check if the current file extension matches any of the extensions for the current file type
                if file_extension.lower() in extensions:
                    # Generate the source and destination paths for the file
                    source_path = os.path.join(foldername, filename)
                    destination_folder = os.path.join(root_dir, file_type)
                    destination_path = os.path.join(destination_folder, filename)

                    # Create the destination folder if it doesn't exist already
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    # Move the file to the destination folder using the move_file function
                    if move_file(source_path, destination_path):
                        # Increment the file count for the current file type
                        file_counts[file_type] += 1
                        # Set the file_moved flag to True
                        file_moved = True
                    # Exit the loop after the file has been successfully moved
                    break

            # If the file extension didn't match any defined file type, move it to the "Others" folder
            if not file_moved:
                source_path = os.path.join(foldername, filename)
                destination_folder = os.path.join(root_dir, 'Others')
                destination_path = os.path.join(destination_folder, filename)

                # Create the "Others" folder if it doesn't exist already
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Move the file to the "Others" folder using the move_file function
                if move_file(source_path, destination_path):
                    # Increment the file count for the "Others" category
                    file_counts['Others'] += 1

    # Return the dictionary containing the file counts for each file type
    return file_counts


def count_files(root_dir):
    # Create a dictionary to store the file counts for each file type
    file_counts = {file_type: 0 for file_type in file_types}

    # Traverse the directory tree starting from root_dir
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Iterate over the files in the current folder
        for filename in filenames:
            # Get the file extension of the current file
            file_extension = os.path.splitext(filename)[1]

            # Iterate over the file types and their associated extensions
            for file_type, extensions in file_types.items():
                # Check if the current file extension matches any of the extensions for the current file type
                if file_extension.lower() in extensions:
                    # Increment the file count for the current file type
                    file_counts[file_type] += 1
                    # Exit the loop after finding a matching file type
                    break
            else:
                # If the file extension didn't match any defined file type, increment the "Others" file count
                file_counts['Others'] += 1

    # Return the dictionary containing the file counts for each file type
    return file_counts


# Example usage
root_directory = 'your/root/directory/here'

# Count files before organizing
initial_file_counts = count_files(root_directory)
print('Initial file counts:')
for file_type, count in initial_file_counts.items():
    print(f'{file_type}: {count}')


# Organize files
final_file_counts = organize_files(root_directory)
print('\nFinal file counts:')
for file_type, count in final_file_counts.items():
    print(f'{file_type}: {count}')

# Count files after organizing
new_file_counts = count_files(root_directory)
print('\nNew file counts:')
for file_type, count in new_file_counts.items():
    print(f'{file_type}: {count}')
