import openai
import os
from dotenv import load_dotenv, find_dotenv


# Load environment variables at module level
load_dotenv(find_dotenv())
env_vars = os.environ
API_KEY = env_vars.get('AZURE_OPENAI_KEY')
API_TYPE = env_vars.get('OPENAI_API_TYPE')
API_VERSION = env_vars.get('OPENAI_API_VERSION')
API_BASE = env_vars.get('AZURE_OPENAI_ENDPOINT')
DEPLOYMENT_ID = env_vars.get('AZURE_DEPLOYMENT_ID')

openai.api_key = API_KEY
openai.api_type = API_TYPE
openai.api_version = API_VERSION
openai.api_base = API_BASE


def get_completion(prompt, deployment_id):
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            engine=deployment_id,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(e)
        return None


def main():
    prompts = [
        "What is the capital of France?",  # The capital of France is Paris.
        "Take the letters in lollipop and reverse them",  # ... "pillipol".
        "Take the letters in l-o-l-l-i-p-o-p and reverse them"  # p-o-p-i-l-l-o-l
    ]

    for prompt in prompts:
        response = get_completion(prompt, DEPLOYMENT_ID)
        print(response)


if __name__ == "__main__":
    main()
