import subprocess

# This script is original work of @aronmilenait. It will be used for personal purposes and removed from the repo afterwards.

def check_package_updates():
    try:
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        
        result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
        if result.stdout:
            print('Available updates:')
            print(result.stdout)
        else:
            print('No packages need to be updated.')
            
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        
def update_packages():
    try:
        choice = input('Do you want to update available packages? (yes/no): ')
        if choice.lower() in ['yes', 'y']:
            subprocess.run(['sudo', 'apt', 'upgrade', '-y'], check=True)
            print('Packages updated successfully!')
        else:
            print('No packages were updated.')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        
def check_network_connection():
    try:
        choice = input('Do you want to check your network connection? (yes/no): ')
        if choice.lower() in ['yes', 'y']:
            result = subprocess.run(['ping', '-c', '1', 'google.com'], capture_output=True, text=True)
            if result.returncode == 0 and '1 packets transmitted, 1 received' in result.stdout:
                print('Network connection is good!')
            else:
                print('Network connection is unstable or unavailable.')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')

def main():
    print("Welcome! Let's perform system updates and check network connectivity.")
    check_package_updates()
    update_packages()
    check_network_connection()
    
if __name__ == '__main__':
    main()
