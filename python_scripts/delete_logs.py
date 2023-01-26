# This script will delete the logs older than 3 months

import os
import datetime

directory = "s:/repository/python_scripts/"

#get the current date and time
now = datetime.datetime.now()

log_files = [file for file in os.listdir(directory) if file.endswith('.logs')]

for file in log_files:
    file_path = os.path.join(directory,file)
    
    # BELOW STATEMENT IS FOR 10 MINUTES BELOW
    delete_time = now - datetime.timedelta(minutes=10)

    file_modified_path = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

    # BELOW STATEMENT WILL DELETE THE LOG FILES MORE THE 20 DAYS
    #if (now - file_modified_path).days > 20:

    if delete_time > file_modified_path:
        os.remove(file_path)
        print(f"File {file_path} has been deleted from the system")
    
    if not log_files:
        print("The log files are not present in the provided directory")    


# import os
# import datetime

# now = datetime.datetime.now()
# file_path = "s:/repository/python_scripts/"

# log_files = [file for file in os.listdir(file_path) if file.endswith('.logs')]

# for file in log_files:
#     file_location = os.path.join(file_path,file)
#     file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_location))

#     if (now - file_modified_time).days > 90:
#         os.remove(file_location)
#         print("The file is removed from the provided location")
    
#     if not log_files:
#         print("There are no log files in the given location")



