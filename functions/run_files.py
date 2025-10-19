import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file in the specified path, constrained to the working directory. Returns the stdout and stderr or possible error messages.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to the file to run, relative to the working directory. If not provided no file can be executed. If the file doesn't exist or is not executable an error is returned.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments given to the python file like argvs. If no arguments are given, no additional arguments will be passed down to the python script.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args = []):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        

        complete_process = subprocess.run(args=["python", abs_file_path] + args, capture_output=True, cwd=abs_working_directory)

        feedback = f"STDOUT: {complete_process.stdout} \n STDERR: {complete_process.stderr}"

        if complete_process.stdout == b'':
            feedback += "\n Not output produced."

        if complete_process.returncode != 0:
            feedback += f"\n Process exited with code {complete_process.returncode}."
            
        
        return feedback
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
