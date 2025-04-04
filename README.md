<div align="center">

# 🚀 CodeCriticAI

### AI-Powered Code Review Tool

[![PyPI version](https://img.shields.io/pypi/v/codecriticai)](https://pypi.org/project/codecriticai/)
[![PyPI downloads](https://img.shields.io/pypi/dm/codecriticai)](https://pypi.org/project/codecriticai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

</div>

CodeCriticAI is a tool for performing AI-powered code reviews using Git diffs. It leverages OpenAI's API to analyze code changes and generate detailed reviews.

## Features

- Analyzes code changes using Git diffs
- Utilizes OpenAI's API for code review
- Generates HTML reports of the code review

## Requirements

- Python 3.6+
- OpenAI API key
- Git

## 🚀 Quick Start

### Installation

```bash
pip install codecriticai
```

> 💡 **Check out [codecriticai on PyPI ](https://pypi.org/project/codecriticai/) for the latest version and release notes.**

### Configuration

```bash
# Linux/macOS
export OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

## 📚 Usage

```bash
# Review current directory changes
codecriticai

# Review specific directory
codecriticai --dir /path/to/repo

# Compare with different base branch
codecriticai --base develop
```

## 🤝 Contributing

We love contributions! Here's how you can help:

### 🛠️ Development Setup

1. Clone the repository:
```bash
git clone https://github.com/mihir20/codecriticAI
cd codecriticAI

2. Set up Python environment:

#### Using pyenv (Recommended)
```bash
# Install Python 3.13.0
pyenv install 3.13.0

# Create a virtual environment
pyenv virtualenv 3.13.0 codecriticAI-dev

# Activate the environment
pyenv activate codecriticAI-dev
```

#### Using venv (Alternative)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Run locally:
```bash
# Using Python module directly (recommended for development)
python -m codecriticAI.main --base main

# Or after installing in development mode
codecriticai --base main
```

> 💡 **Note:** Using pyenv is recommended as it provides better Python version management and isolation.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find codecriticAI useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 🤝 Contributing to the code
- 📢 Spreading the word

---

<div align="center">
Made by <a href="https://github.com/mihir20">Mihir Gandhi</a>
</div>