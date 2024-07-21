#!/bin/python3

import os

def move_files(source_folder, target_folder):
    try:
        for path, directories, files in os.walk(source_folder):
            for file in files:
                source_file_path = os.path.join(path, file)
                target_file_path = os.path.join(target_folder, file)
                if not os.path.isfile(target_file_path):
                    os.rename(source_file_path, target_file_path)
                else:
                    print(f'File already exists in target: {target_file_path}')

        for path, directories, files in os.walk(source_folder, topdown=False): 
            for directory in directories:
                directory_path = os.path.join(path, directory)
                try:
                    os.rmdir(directory_path)
                    print(f'Removed empty directory: {directory_path}')
                except OSError as e:
                    print(f'Error removing directory {directory_path}: {e}')

    except Exception as error:
        print(f'Error: {error}')

move_files(f'/Users/user/Soulseek Downloads/complete', '/Users/user/Documents/getemout')
