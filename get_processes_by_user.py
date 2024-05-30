import psutil

def get_processes_by_user(username):
    user_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['username'] == username:
                user_processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass
    return user_processes

def main():
    username = input("Enter the username to filter processes: ")
    processes = get_processes_by_user(username)
    
    if not processes:
        print(f"No processes found for user: {username}")
    else:
        print(f"Processes owned by user {username}:")
        for proc in processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}")
            
if __name__ == "__main__":
    main()
