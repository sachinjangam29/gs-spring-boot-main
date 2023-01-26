import os
import datetime

now = datetime.datetime.now()

folder_name = now.strftime("%Y-%m-%d %H-%M-%S")

os.makedirs("Folder "+folder_name)