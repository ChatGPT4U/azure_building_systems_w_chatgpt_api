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


def get_completion_from_messages(messages, engine, temperature=0, max_tokens=500):
    try:
        response = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        print(e)
        raise e


def create_message_and_get_completion(system_message, user_message, engine=DEPLOYMENT_ID):
    delimiter = "####"
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    return get_completion_from_messages(messages, engine)


def main():
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with \
    characters.
    Classify each query into a primary category \
    and a secondary category. 
    Provide your output in json format with the \
    keys: primary and secondary.

    Primary categories: Billing, Technical Support, \
    Account Management, or General Inquiry.

    Billing secondary categories:
    Unsubscribe or upgrade
    Add a payment method
    Explanation for charge
    Dispute a charge

    Technical Support secondary categories:
    General troubleshooting
    Device compatibility
    Software updates

    Account Management secondary categories:
    Password reset
    Update personal information
    Close account
    Account security

    General Inquiry secondary categories:
    Product information
    Pricing
    Feedback
    Speak to a human

    """
    user_messages = [
        "I want you to delete my profile and all of my user data",
        "Tell me more about your flat screen tvs"
    ]

    for user_message in user_messages:
        response = create_message_and_get_completion(
            system_message, user_message)
        print(response)


if __name__ == "__main__":
    main()
