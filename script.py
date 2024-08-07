import os
import stat
import sys
import pwd
import grp

def create_files(directory):
    files = [
        ("group_only.txt", 0o770),
        ("public_knowledge.txt", 0o644),
        ("secret.txt", 0o600),
        ("secret.txt.pgp", 0o644),
        ("wiki.txt", 0o777)
    ]
    
    for filename, mode in files:
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            try:
                with open(filepath, 'w') as f:
                    os.chmod(filepath, mode)
                    f.write('')
            except Exception as e:
                print(f"Failed to create {filename}: {e}")
                sys.exit(1)

def check_ownership(directory):
    files = [
        ("group_only.txt", "root", "wheel"),
        ("public_knowledge.txt", "root", "root"),
        ("secret.txt", "root", "root"),
        ("secret.txt.pgp", "root", "root"),
        ("wiki.txt", "nobody", "nogroup")
    ]
    
    for filename, owner, group in files:
        filepath = os.path.join(directory, filename)
        try:
            stat_info = os.stat(filepath)
            current_owner = pwd.getpwuid(stat_info.st_uid).pw_name
            current_group = grp.getgrgid(stat_info.st_gid).gr_name
            if current_owner != owner or current_group != group:
                os.chown(filepath, pwd.getpwnam(owner).pw_uid, grp.getgrnam(group).gr_gid)
        except Exception as e:
            print(f"Failed to check ownership of {filename}: {e}")
            sys.exit(1)

def check_permissions(directory):
    files = [
        ("group_only.txt", 0o640),
        ("public_knowledge.txt", 0o644),
        ("secret.txt", 0o600),
        ("secret.txt.pgp", 0o644),
        ("wiki.txt", 0o777)
    ]
    
    for filename, permissions in files:
        filepath = os.path.join(directory, filename)
        try:
            current_permissions = stat.S_IMODE(os.stat(filepath).st_mode)
            if current_permissions != permissions:
                os.chmod(filepath, permissions)
        except Exception as e:
            print(f"Failed to check permissions of {filename}: {e}")
            sys.exit(1)


def check_permissions(directory):
    files = [
        ("group_only.txt", 0o770),
        ("public_knowledge.txt", 0o644),
        ("secret.txt", 0o600),
        ("secret.txt.pgp", 0o644),
        ("wiki.txt", 0o777)
    ]
    
    for filename, permissions in files:
        filepath = os.path.join(directory, filename)
        try:
            current_permissions = stat.S_IMODE(os.stat(filepath).st_mode)
            if current_permissions != permissions:
                os.chmod(filepath, permissions)
        except Exception as e:
            print(f"Failed to check permissions of {filename}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py directory")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    create_files(directory)
    check_ownership(directory)
    check_permissions(directory)
