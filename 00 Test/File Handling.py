# # Copy from file A to B
# try:
#     source_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\a.txt"
#     destination_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\B.txt"
    
#     with open(source_path, "r") as file_01:
#         with open(destination_path, "w") as file_02:
#             for line in file_01: # Read line by line
#                 file_02.write(line)  # Write line by line
    
# except FileNotFoundError:
#     print("Source file not found. Please check the file path.")
# except PermissionError:
#     print("Permission denied. Check read/write permissions.")
# except Exception as e:
#     print("An error occurred:", e)
# else:
#     print("File Copied Successfully")


# Delete File
f_path = "C:\\Users\\akash\\Desktop\\Py Projects\\Python-Projects\\00 Test\\File Handling\\a.txt"

import os
if os.path.exists(f_path): #1st check if the file is exist or not?
    os.remove(f_path)
else:
    print("File not available ... !")
