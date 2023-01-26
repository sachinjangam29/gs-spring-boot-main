# THIS SCRIPT WILL COMPRESS THE LARGE FILES.

import os
import gzip


def compress_file(file_path):
    """
        compress the huge files
    """

    with open(file_path, 'rb') as file_in:
        with gzip.open(file_path + '.gz', 'wb') as file_out:
            file_out.writelines(file_in)
    os.remove(file_path)
    print(f"File {file_path} has been successfully compressed ")

file_path = "S:/python/AutomationScripts/food/fruits/python_crash_course_pdf.pdf"
compress_file(file_path)