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

        response = client.chat.completions.create(
            model="o3",
            messages=[{"role": "user", "content": prompt_text}],
            stream=True
        )

        # Iterate over streamed chunks:

        full_response = ""
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                # Write the chunk to the terminal
                print(chunk.choices[0].delta.content, end="", flush=True)

                # Append the chunk content to the full response
                full_response += chunk.choices[0].delta.content

        print()  # Print a newline for better formatting

        
    except OpenAIError as e:
        print(f"API request failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run an o3 prompt from a .txt file")
    parser.add_argument("prompt_file", help="Path to prompt text file")
    args = parser.parse_args()
    main(args.prompt_file)