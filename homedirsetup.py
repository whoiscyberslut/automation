# A script that sets up a home directory for a new user. It creates the directory if it doesn't exist, sets appropriate ownership 
# and permissions, and creates default configuration files.



import os
import pwd
import grp
import shutil

def setup_user_home(username, base_path):
    home_directory = os.path.join(base_path, username)
    if not os.path.exists(home_directory):
        os.makedirs(home_directory)
        print(f"Created home directory: {home_directory}")
    
    uid = pwd.getpwnam(username).pw_uid
    gid = grp.getgrnam(username).gr_gid
    
    os.chown(home_directory, uid, gid)
    os.chmod(home_directory, 0o755)
    
    create_default_files(home_directory, uid, gid)
    
    print(f"Home directory setup complete for user: {username}")

def create_default_files(home_directory, uid, gid):
    default_files = ['.bashrc', '.profile']
    for filename in default_files:
        filepath = os.path.join(home_directory, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write(f"# Default {filename} for user\n")
            os.chown(filepath, uid, gid)
            os.chmod(filepath, 0o644)
            print(f"Created default file: {filename}")

username = 'newuser'
base_path = '/home'

setup_user_home(username, base_path)
