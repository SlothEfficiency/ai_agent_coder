import os

def get_files_info(working_directory, directory="."):
    directory = os.path.join(working_directory, directory)
    print(directory)


current_dir = os.getcwd()
print(current_dir)

get_files_info(current_dir, directory=".")
