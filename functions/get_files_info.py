import os

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
    
