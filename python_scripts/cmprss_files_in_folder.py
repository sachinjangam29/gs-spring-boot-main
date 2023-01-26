#THIS SCRIPT WILL WALK THROUGH THE FILES UNDER THE FOLDERS.

import os
import datetime
import gzip

def compress_files_in_folders(folder_path):
    """
        COMPRESS ALL THE FILES IN THE FOLDER
    """
    # WALK THROUGH ALL THE FILES AND THE SUB-FOLDERS IN THE FOLDER
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for file_name in filenames:
                #CONSTRUCT THE FULL FILE PATH
                file_path = os.path.join(dirpath,file_name)
                #COMPRESS THE FILE
                compress_file(dirpath,file_path)
    except Exception as e:
        print(f"An error occurred while compressing the files : {e}")

    

def compress_file(dirpath,file_path):
 
        try:
            with open(file_path, 'rb') as file_in:
                with gzip.open(file_path +'.gz', 'wb') as file_out:
                    file_out.writelines(file_in)
        except Exception as e:
            print(f"An error occurred while compressing the file {e}")

        os.remove(file_path)

        print(f"File {file_path} has been successfully compressed")


folder_path = "S:/python/AutomationScripts/food/fruits/"
compress_files_in_folders(folder_path)