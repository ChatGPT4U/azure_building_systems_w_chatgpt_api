import openai
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables at module level
load_dotenv(find_dotenv())
API_KEY = os.getenv('AZURE_OPENAI_KEY')
API_TYPE = os.getenv('OPENAI_API_TYPE')
API_VERSION = os.getenv('OPENAI_API_VERSION')
API_BASE = os.getenv('AZURE_OPENAI_ENDPOINT')
DEPLOYMENT_ID = os.getenv('AZURE_DEPLOYMENT_ID')

openai.api_key = API_KEY
openai.api_type = API_TYPE
openai.api_version = API_VERSION
openai.api_base = API_BASE


def get_completion_and_token_count(messages, engine, temperature=0, max_tokens=500):
    try:
        response = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        content = response.choices[0].message["content"]

        token_dict = {
            'prompt_tokens': response['usage']['prompt_tokens'],
            'completion_tokens': response['usage']['completion_tokens'],
            'total_tokens': response['usage']['total_tokens'],
        }

        return content, token_dict
    except openai.error.OpenAIError as e:
        print(e)
        return None, None


def process(messages, engine=DEPLOYMENT_ID, temperature=0):
    response, token_dict = get_completion_and_token_count(
        messages, engine=engine, temperature=temperature)
    print(response)
    print(token_dict)
    print('-' * 60)


def generate_messages(system_content, user_content):
    return [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': user_content},
    ]


def main():
    messages = generate_messages(
        'You are an assistant who responds in the style of Dr Seuss.',
        'write me a very short poem about a happy carrot')
    process(messages, temperature=1)

    messages = generate_messages(
        'All your responses must be one sentence long.',
        'write me a story about a happy carrot')
    process(messages, temperature=1)

    messages = generate_messages(
        'You are an assistant who responds in the style of Dr Seuss. All your responses must be one sentence long.',
        'write me a story about a happy carrot')
    process(messages, temperature=1)

    messages = generate_messages(
        'You are an assistant who responds in the style of Dr Seuss.',
        'write me a very short poem about a happy carrot')
    process(messages)


if __name__ == "__main__":
    main()
