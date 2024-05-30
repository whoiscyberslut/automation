def parse_backup_directory(directory, current_year):
    print(f"Parsing directory {directory} for backup files...\n")

    backup_files = [f for f in os.listdir(directory) if f.startswith("backup_") and f.endswith(".tar.gz")]
    keep_files = []
    delete_files = []

    for file in backup_files:
        # Extract the date part from the filename
        date_str = file[7:15]
        try:
            file_date = datetime.strptime(date_str, '%Y%m%d')
            if file_date.year == current_year:
                keep_files.append(file)
            else:
                delete_files.append(file)
        except ValueError:
            continue

    # Print the results
    for file in keep_files:
        print(f"[keep]      {file}")

    for file in delete_files:
        print(f"[delete]    {file}")


if __name__ == "__main__":
    directory = "/Users/user/Desktop"
    current_year = 2015
    parse_backup_directory(directory, current_year)
