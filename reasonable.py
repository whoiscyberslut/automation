import os
import sys

def create_files(directory):
    files_to_create = [
        "group_only.txt",
        "public_knowledge.txt",
        "secret.txt",
        "secret.txt.pgp",
        "wiki.txt"
    ]

    for filename in files_to_create:
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            try:
                open(filepath, 'a').close()
            except Exception as e:
                print(f"Failed to create file: {filepath}")
                return 1

    return 0

def check_permissions(directory):
    files_to_check = [
        ("group_only.txt", "rw-r-----"),
        ("public_knowledge.txt", "rw-r--r--"),
        ("secret.txt", "rw-------"),
        ("secret.txt.pgp", "rw-r--r--"),
        ("wiki.txt", "rwxrwxrwx")
    ]

    for filename, expected_permissions in files_to_check:
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            try:
                actual_permissions = oct(os.stat(filepath).st_mode & 0o777)
                if actual_permissions != expected_permissions:
                    os.chmod(filepath, int(expected_permissions, 8))
            except Exception as e:
                print(f"Failed to check/modify permissions for file: {filepath}")
                return 1

    return 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if create_files(directory) != 0 or check_permissions(directory) != 0:
        sys.exit(1)

    print("All tasks completed successfully.")
    sys.exit(0)

if __name__ == "__main__":
    main()
