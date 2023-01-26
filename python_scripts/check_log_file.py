# This script will create a particular file in a specific directory

import os
import datetime

dir = "s:/repository/python_scripts/"

#below statement will give the exact path of the file
#file_path = os.path.abspath(__file__)

now = datetime.datetime.now()

folder_name = 'Folder '+now.strftime('%Y-%m-%d %H-%M-%S')

full_dir_name = os.path.join(dir,folder_name)

#os.makedirs(full_dir_name)
#print("The folder "+folder_name+" has been successfully created in the location "+dir)
#print("File Address is "+full_dir_name)


# Below statement will check if a specific file present at the given location

if os.path.isfile(dir+'check.logs'):
    print("True")
else:
    print("False")

logs_files = [file for file in os.listdir(dir) if file.endswith('.logs')]

if logs_files:
    print("Logs are present in the director",logs_files)
else:
    print("Logs are not present in the directory")