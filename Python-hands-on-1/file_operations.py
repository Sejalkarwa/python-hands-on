import os

# 1) Print the current working directory
print("\nCurrent Working Directory:", os.getcwd())

# 2) Check if a path is a File or Directory

path = "file_operations.py"

if os.path.isfile(path):
    print(f"\n{path} is a file.")
elif os.path.isdir(path):
    print(f"\n{path} is a directory.")
else:
    print(f"\n{path} does not exist.")

# 3) Create a Directory (if not exists) 
folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"\nDirectory '{folder_name}' created.")
else:
    print(f"\nDirectory '{folder_name}' already exists.")

# 4) Loop Through Files and Filter by Extension Task: List only .txt files in the current directory.
print(                                         )
print("\nList of .txt files in current directory:")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
       

# 5) Combine Everything
 
import os
import shutil  # to move files
print(           )
# Current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create reports directory if not exists
reports_dir = os.path.join(cwd, "reports")
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print("Directory 'reports' created.")
else:
    print("Directory 'reports' already exists.")

# List and move .txt files
print("Processing .txt files:")
for file in os.listdir(cwd):
    if file.endswith(".txt") and os.path.isfile(file):
        print(f"Found: {file}")
        shutil.move(file, reports_dir)
        print(f"Moved {file} to 'reports' folder.")
        

