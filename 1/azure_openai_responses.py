import openai
import os
from dotenv import load_dotenv, find_dotenv
from typing import Optional


# Load environment variables at module level
load_dotenv(find_dotenv())
env_vars: dict[str, str] = os.environ
API_KEY: Optional[str] = env_vars.get("AZURE_OPENAI_KEY")
API_TYPE: Optional[str] = env_vars.get("OPENAI_API_TYPE")
API_VERSION: Optional[str] = env_vars.get("OPENAI_API_VERSION")
API_BASE: Optional[str] = env_vars.get("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_ID: Optional[str] = env_vars.get("AZURE_DEPLOYMENT_ID")

openai.api_key = API_KEY
openai.api_type = API_TYPE
openai.api_version = API_VERSION
openai.api_base = API_BASE


def get_completion(prompt: str, engine: Optional[str] = DEPLOYMENT_ID) -> Optional[str]:
    messages: list[dict[str, str]] = [{"role": "user", "content": prompt}]
    try:
        response: openai.openai_object.OpenAIObject = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(e)
        return None


def main() -> None:
    prompts: list[str] = [
        "What is the capital of France?",  # The capital of France is Paris.
        "Take the letters in lollipop and reverse them",  # ... "pillipol".
        "Take the letters in l-o-l-l-i-p-o-p and reverse them",  # p-o-p-i-l-l-o-l
    ]

    for prompt in prompts:
        response: Optional[str] = get_completion(prompt)
        print(response)


if __name__ == "__main__":
    main()
