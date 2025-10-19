import os

from google import genai
from google.genai import types

from functions.get_files import schema_get_files_info
from functions.get_files import schema_get_file_content
from functions.write_files import schema_write_file
from functions.run_files import schema_run_python_file

from dotenv import load_dotenv


system_prompt = """
                You are a helpful AI coding agent.

                When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

                - List files and directories
                - Read file contents
                - Execute Python files with optional arguments
                - Write or overwrite files

                All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                Also do not ask for more arguments. Always work with what you got and find it out yourself. At the end of your work if you made any changes, explain them.
                """



#Define config
available_functions = types.Tool(function_declarations=[
                                    schema_get_files_info,
                                    schema_get_file_content,
                                    schema_write_file,
                                    schema_run_python_file])
config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)


# Define the API
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)