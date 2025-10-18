import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    verbose = False
    arguments = sys.argv
    if "--verbose" in arguments:
        verbose = True
        arguments.remove("--verbose")
        
    try:
        user_prompt = arguments[1]
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    
    except Exception as e:
        print(f"{e} was thrown.")
        exit(1)
    
    api_call = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print(api_call.text)
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {api_call.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {api_call.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
