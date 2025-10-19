from functions.get_files import get_file_content, get_files_info
from functions.write_files import write_file
from functions.run_files import run_python_file

from google.genai import types

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    args = function_call_part.args

    if verbose:
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    args["working_directory"] = "./calculator"

    function_dict = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }


    if function_name not in function_dict:
        return types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    function_result = function_dict[function_name](**args)
    
    return types.Content(
        role="user",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

    