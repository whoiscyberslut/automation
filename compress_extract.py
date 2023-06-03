# Build a script that compresses or extracts files in a directory. The script should support different compression
# algorithms (e.g., zip, gzip) and allow for compressing multiple files into an archive or extracting specific files
# from an archive.

import os
import shutil
import zipfile
import gzip

def compress_files(directory, output_file, compression_algorithm):
    if compression_algorithm == "zip":
        with zipfile.ZipFile(output_file, "w") as zipf:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory))
        print(f"Successfully compressed files to {output_file} using ZIP format.")
    elif compression_algorithm == "gzip":
        with gzip.open(output_file, "wb") as gz_file:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        shutil.copyfileobj(f, gz_file)
        print(f"Successfully compressed files to {output_file} using GZIP format.")
    else:
        print("Unsupported compression algorithm.")

def extract_files(archive_file, extraction_path):
    if zipfile.is_zipfile(archive_file):
        with zipfile.ZipFile(archive_file, "r") as zipf:
            zipf.extractall(extraction_path)
        print(f"Successfully extracted files from {archive_file} using ZIP format.")
    elif archive_file.endswith(".gz"):
        with gzip.open(archive_file, "rb") as gz_file:
            with open(extraction_path, "wb") as f:
                shutil.copyfileobj(gz_file, f)
        print(f"Successfully extracted files from {archive_file} using GZIP format.")
    else:
        print("Unsupported archive format.")

# Example usage
compress_files("path/to/directory", "compressed.zip", "zip")
extract_files("compressed.zip", "path/to/extract")

