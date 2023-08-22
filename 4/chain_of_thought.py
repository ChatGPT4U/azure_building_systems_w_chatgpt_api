import openai
import os
from dotenv import load_dotenv, find_dotenv
import logging

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

# DELIMITER = "####"


def get_completion_from_messages(messages, engine=DEPLOYMENT_ID, temperature=0, max_tokens=500):
    try:
        response = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        logging.error(e)
        raise


def create_messages(system_message, user_message, delimiter):
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    return messages


def main():
    delimiter="####"
    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with four hashtags,\
    i.e. {delimiter}. 

    Step 1:{delimiter} First decide whether the user is \
    asking a question about a specific product or products. \
    Product cateogry doesn't count. 

    Step 2:{delimiter} If the user is asking about \
    specific products, identify whether \
    the products are in the following list.
    All available products: 
    1. Product: TechPro Ultrabook
       Category: Computers and Laptops
       Brand: TechPro
       Model Number: TP-UB100
       Warranty: 1 year
       Rating: 4.5
       Features: 13.3-inch display, 8GB RAM, 256GB SSD, Intel Core i5 processor
       Description: A sleek and lightweight ultrabook for everyday use.
       Price: $799.99

    2. Product: BlueWave Gaming Laptop
       Category: Computers and Laptops
       Brand: BlueWave
       Model Number: BW-GL200
       Warranty: 2 years
       Rating: 4.7
       Features: 15.6-inch display, 16GB RAM, 512GB SSD, NVIDIA GeForce RTX 3060
       Description: A high-performance gaming laptop for an immersive experience.
       Price: $1199.99

    3. Product: PowerLite Convertible
       Category: Computers and Laptops
       Brand: PowerLite
       Model Number: PL-CV300
       Warranty: 1 year
       Rating: 4.3
       Features: 14-inch touchscreen, 8GB RAM, 256GB SSD, 360-degree hinge
       Description: A versatile convertible laptop with a responsive touchscreen.
       Price: $699.99

    4. Product: TechPro Desktop
       Category: Computers and Laptops
       Brand: TechPro
       Model Number: TP-DT500
       Warranty: 1 year
       Rating: 4.4
       Features: Intel Core i7 processor, 16GB RAM, 1TB HDD, NVIDIA GeForce GTX 1660
       Description: A powerful desktop computer for work and play.
       Price: $999.99

    5. Product: BlueWave Chromebook
       Category: Computers and Laptops
       Brand: BlueWave
       Model Number: BW-CB100
       Warranty: 1 year
       Rating: 4.1
       Features: 11.6-inch display, 4GB RAM, 32GB eMMC, Chrome OS
       Description: A compact and affordable Chromebook for everyday tasks.
       Price: $249.99

    Step 3:{delimiter} If the message contains products \
    in the list above, list any assumptions that the \
    user is making in their \
    message e.g. that Laptop X is bigger than \
    Laptop Y, or that Laptop Z has a 2 year warranty.

    Step 4:{delimiter}: If the user made any assumptions, \
    figure out whether the assumption is true based on your \
    product information. 

    Step 5:{delimiter}: First, politely correct the \
    customer's incorrect assumptions if applicable. \
    Only mention or reference products in the list of \
    5 available products, as these are the only 5 \
    products that the store sells. \
    Answer the customer in a friendly tone.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 reasoning>
    Step 4:{delimiter} <step 4 reasoning>
    Response to user:{delimiter} <response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    user_message1 = "by how much is the BlueWave Chromebook more expensive than the TechPro Desktop"
    user_message2 = "do you sell tvs"

    messages1 = create_messages(system_message, user_message1, delimiter)
    response1 = get_completion_from_messages(messages1)
    print(f"{response1}\n{'-' * 80}")

    messages2 = create_messages(system_message, user_message2, delimiter)
    response2 = get_completion_from_messages(messages2)
    print(f"{response2}\n{'-' * 80}")

    try:
        final_response = response2.split(delimiter)[-1].strip()
    except IndexError:
        final_response = "Sorry, I'm having trouble right now, please try asking another question."

    print(final_response)


if __name__ == "__main__":
    main()
