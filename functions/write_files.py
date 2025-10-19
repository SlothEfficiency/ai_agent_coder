import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file in the specified directory and with the specified name, constrained to the working directory. Gives feedback about the success. Always overwrites the whole file with the given content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to write the file, relative to the working directory. If not provided no file can be written. If the directory doesn't exist yet it will be created.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file. If not provided the file will not be written.",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.mkdir(os.path.dirname(abs_file_path))

        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

    