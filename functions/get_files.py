import os
from functions.config import MAX_CHARS


def get_files_info(working_directory, directory="."):
    try:    
        target_directory = os.path.abspath(os.path.join(working_directory, directory))

        if not target_directory.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(target_directory)

        return "\n".join(
            list(map(
                lambda x: f"- {x}: file_size={os.path.getsize(os.path.join(target_directory, x))}, is_dir={os.path.isdir(os.path.join(target_directory, x))}", contents)
                )
            )

    except Exception as e:
        return f"Error: {e}"
    


def get_file_content(working_directory, file_path):
    try:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_directory = os.path.abspath(working_directory)

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string


    except Exception as e:
        return f"Error: {e}"
    
