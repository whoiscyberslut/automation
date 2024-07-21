import os
import stat
import pwd
import grp
import sys

def create_files(directory):
    files = [
        "group_only.txt",
        "public_knowledge.txt",
        "secret.txt",
        "secret.txt.pgp",
        "wiki.txt"
    ]
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(file_path):
            open(file_path, 'a').close()
            # OR: 
            # with open(file_path, 'a') as file:
            #     pass  # Creates an empty file

def check_ownership(directory):
    files = [
        "group_only.txt",
        "public_knowledge.txt",
        "secret.txt",
        "secret.txt.pgp",
        "wiki.txt"
    ]
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        stat_info = os.stat(file_path)
        owner = pwd.getpwuid(stat_info.st_uid).pw_name
        if owner != "root":
            os.chown(file_path, 0, -1)

def check_permissions(directory):
    files = [
        ("group_only.txt", 640),
        ("public_knowledge.txt", 644),
        ("secret.txt", 600),
        ("secret.txt.pgp", 644),
        ("wiki.txt", 777)
    ]
    for file_name, expected_perm in files:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            current_perm = stat.S_IMODE(os.lstat(file_path).st_mode)
            if current_perm != expected_perm:
                os.chmod(file_path, expected_perm)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    try:
        create_files(directory)
        check_ownership(directory)
        check_permissions(directory)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

