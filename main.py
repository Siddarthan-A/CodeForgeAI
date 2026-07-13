import os
from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def run_agent(user_prompt: str) -> str:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=api_key,)
    messages = [
        {"role": "system","content": system_prompt},
        { "role": "user","content": user_prompt},
    ]

    return generate_content(client, messages)


def generate_content(client, messages):
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message

        messages.append(message.model_dump())

        if not message.tool_calls:
            return message.content


        for tool_call in message.tool_calls:

            if tool_call.type != "function":
                continue

            result_message = call_function(tool_call,False)
            messages.append(result_message)


    return "Agent stopped without completing the task."