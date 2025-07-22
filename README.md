# run-openai-prompt

Python scripts to test a prompt with the OpenAI API.

## Installation

Set up virtual environment and install dependencies):

```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key (based on `.env.example`)

## Usage 

Streaming version:

```
python run-prompt-streaming.py prompt.txt
```

Non-streaming version:

```
python run-prompt.py prompt.txt
```

## Edits 

The Python scripts default to using `o3`. Update the scripts to use another model.



