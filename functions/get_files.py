import os
from functions.config import MAX_CHARS
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

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
    


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file in the specified directory limited to 10000 characters, constrained to the working directory. You can only get 1 file at once.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to read the file from, relative to the working directory. If not provided, no file can be read.",
            ),
        },
    ),
)


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
    
