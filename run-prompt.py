# Install dependencies:
# pip install python-dotenv openai

import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

def load_api_key():
    load_dotenv()  
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY in environment. Please add it to .env")
    return api_key

def read_prompt_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def main(prompt_file):
    api_key = load_api_key()
    client = OpenAI(api_key=api_key)

    prompt_text = read_prompt_file(prompt_file)
    if not prompt_text:
        raise ValueError(f"Prompt file '{prompt_file}' is empty")

    try:
        response = client.responses.create(
            model="o3",
            input=[{"role": "user", "content": prompt_text}]
        )
        print(response.output_text)
    except OpenAIError as e:
        print(f"API request failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run an o3 prompt from a .txt file")
    parser.add_argument("prompt_file", help="Path to prompt text file")
    args = parser.parse_args()
    main(args.prompt_file)