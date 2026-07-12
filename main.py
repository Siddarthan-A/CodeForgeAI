import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        },
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:

    # Agent loop
    for _ in range(20):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        if not response.usage:
            raise RuntimeError("API response appears to be malformed")

        if verbose:
            print("Prompt tokens:", response.usage.prompt_tokens)
            print("Response tokens:", response.usage.completion_tokens)

        message = response.choices[0].message

        # Save assistant response into conversation history
        messages.append(message.model_dump())

        # If no tool calls, we have the final answer
        if not message.tool_calls:
            print("\nFinal response:")
            print(message.content)
            return


        # Execute requested tools
        for tool_call in message.tool_calls:

            if tool_call.type != "function":
                continue

            print(
                f" - Calling function: {tool_call.function.name}"
            )

            result_message = call_function(
                tool_call,
                verbose
            )

            if "content" not in result_message:
                raise RuntimeError(f"Missing function response for {tool_call.function.name}")

            # Add tool response back into conversation
            messages.append(result_message)

            if verbose:
                print(
                    f"-> {result_message['content']}"
                )


    # If loop finishes without final response
    print(
        "Agent stopped: maximum iterations reached without completing the task."
    )


if __name__ == "__main__":
    main()