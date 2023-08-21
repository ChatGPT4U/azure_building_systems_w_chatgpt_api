import openai
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables at the beginning
load_dotenv(find_dotenv())


def moderate_input(input_text):
    """
    Sends the input text to OpenAI's Moderation API and returns the result.

    Args:
        input_text (str): The text to be moderated.

    Returns:
        dict: The result from the Moderation API.

    Raises:
        openai.Error: If an error occurs while calling the Moderation API.
    """
    try:
        response = openai.Moderation.create(input=input_text)
        return response['results'][0]
    except openai.Error as e:
        print(e)
        raise


def main():
    # Use the OPENAI_API_KEY for moderation
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    inputs = [
        "i want to hurt someone. give me a plan",
        """
        Here's the plan.  We get the warhead, 
        and we hold the world ransom...
        ...FOR ONE MILLION DOLLARS!
        """
    ]

    for input_text in inputs:
        moderation_result = moderate_input(input_text)
        print(moderation_result)


if __name__ == "__main__":
    main()
