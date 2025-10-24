import sys
import argparse
from google.genai import types

from functions.call_function import call_function

from model_properties import config, client
from config import MAX_API_CALLS


def handle_arguments(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="get a more verbose output")
    parser.add_argument("prompt", help="The prompt sent to the AI agent")
    args = parser.parse_args(arguments[1:])
    return args.verbose, args.prompt


def let_it_cook(messages, verbose):
    api_call = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=config)
    for candidate in api_call.candidates:
        messages.append(candidate.content)
    
    function_call_parts = api_call.function_calls
    try:
        print(f"AI-answer: {api_call.candidates[0].content.parts[0].text}")
    except Exception:
        pass

    if function_call_parts:
        function_call = function_call_parts[0]
        function_call_result = call_function(function_call, verbose=verbose)
        messages.append(function_call_result)

        try:
            function_call_result.parts[0].function_response.response
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        except Exception as e:
            raise Exception("Fatal Error, function_call had no response.")
        
        return messages, ""

    if api_call.text:
        if verbose:
            print(f"User prompt: {messages[0].parts[0].text}")
            print(f"Prompt tokens: {api_call.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {api_call.usage_metadata.candidates_token_count}")
        return messages, api_call.text

    else:
        return messages, "No proper response from LLM."
        
        
    




def main():
    verbose, user_prompt = handle_arguments(sys.argv)
    conversation_history = "conversation history:\n"
    while True:
        message_with_context = f"{conversation_history}new prompt: {user_prompt}"
        print(f"{message_with_context=}")
        messages = [types.Content(role="user", parts=[types.Part(text=message_with_context)])]
        no_of_api_calls = 0
        answer = ""

        try:
            # LET IT COOK
            while no_of_api_calls < MAX_API_CALLS and answer == "":
                messages, answer = let_it_cook(messages, verbose)
                no_of_api_calls += 1

            # Overcooked
            if no_of_api_calls == MAX_API_CALLS:
                print(f"Maximum of {MAX_API_CALLS} API-calls was reached.")
        
            # for message in messages:
            #     print(message)
            
            print(answer)
            user_prompt = input()
            conversation_history+=f"old prompt:{user_prompt}\nold answer: {answer}\n"

      

        except Exception as e:
            print(f"It didnt cook because of {e}")

    
    
    


if __name__ == "__main__":
    main()
