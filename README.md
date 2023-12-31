# Building Systems with the ChatGPT API using Azure OpenAI API

This repository contains my learnings and implementations from the DeepLearning.AI course on Building Systems with the ChatGPT API. Nearly all the implementations are done using Azure OpenAI API.

## Table of Contents

0. [Introduction](#introduction)
1. [Language Models, the Chat Format and Tokens](#language-models-the-chat-format-and-tokens)
2. [Evaluate Inputs: Classification](#evaluate-inputs-classification)
3. [Evaluate Inputs: Moderation](#evaluate-inputs-moderation)
4. [Process Inputs: Chain of Thought Reasoning](#process-inputs-chain-of-thought-reasoning)
5. [Process Inputs: Chaining Prompts](#process-inputs-chaining-prompts)
6. [Check Outputs](#check-outputs)
7. [Evaluation](#evaluation)
8. [Evaluation Part I](#evaluation-part-i)
9. [Evaluation Part II](#evaluation-part-ii)
10. [Summary](#summary)

## Introduction

This section will be updated soon.

## Language Models, the Chat Format and Tokens

### `1\azure_openai_responses.py`

This script demonstrates how to use the OpenAI API to generate responses to a set of prompts. The API settings are securely loaded from environment variables.

### `1\azure_openai_token_counter.py`

This script showcases how to use the OpenAI API to generate chat responses and count tokens in different scenarios, providing insights into the token usage of your API calls.

## Evaluate Inputs: Classification

### `2\customer_service_query_classifier.py`

This script implements a customer service chatbot using the OpenAI API. It classifies user queries into categories and generates appropriate responses based on these classifications.

## Evaluate Inputs: Moderation

### `3\openai_moderation.py`

This script provides a simple example of how to use OpenAI's Moderation API to moderate a list of text strings, ensuring the content is appropriate and adheres to community guidelines.

### `3\prompt_injection_prevention.py`

This script is designed to interact with OpenAI's Chat models to prevent prompt injection attacks.

## Process Inputs: Chain of Thought Reasoning

### `4\chain-of-thought.py`

This script demonstrates a "chain of thought" approach where the AI assistant follows predefined steps to analyze and respond to customer queries about a limited set of products. The system message defines the steps, and the assistant follows them to identify assumptions, check facts, and provide a final polite response.

## Process Inputs: Chaining Prompts

This section will be updated soon.

## Check Outputs

This section will be updated soon.

## Evaluation

This section will be updated soon.

## Evaluation Part I

This section will be updated soon.

## Evaluation Part II

This section will be updated soon.

## Summary

This section will be updated soon.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Thanks to DeepLearning.AI for the informative course.
* Thanks to OpenAI for their powerful API.
