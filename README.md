# CodeCriticAI

CodeCriticAI is a tool for performing AI-powered code reviews using Git diffs. It leverages OpenAI's API to analyze code changes and generate detailed reviews.

## Features

- Analyzes code changes using Git diffs
- Utilizes OpenAI's API for code review
- Generates HTML reports of the code review

## Requirements

- Python 3.6+
- OpenAI API key
- Git

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mihir20/CodeCriticAI.git
    cd CodeCriticAI
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

Run the main script with the required arguments:
```sh
python codecriticAI/main.py --dir <directory_path> [--base <base_branch>]