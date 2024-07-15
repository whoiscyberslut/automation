import os
import shutil
import gzip
import time
from datetime import datetime, timedelta

def archive_old_logs(log_directory, archive_directory, days):
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)
    
    threshold_date = datetime.now() - timedelta(days=days)
    
    for filename in os.listdir(log_directory):
        filepath = os.path.join(log_directory, filename)
        if os.path.isfile(filepath):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
            if file_mtime < threshold_date:
                shutil.move(filepath, archive_directory)
                with open(os.path.join(archive_directory, filename), 'rb') as f_in:
                    with gzip.open(os.path.join(archive_directory, filename + '.gz'), 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(os.path.join(archive_directory, filename))
                print(f"Archived and compressed: {filename}")

log_directory = '/path/to/log/directory'
archive_directory = '/path/to/archive/directory'
days = 30

archive_old_logs(log_directory, archive_directory, days)
