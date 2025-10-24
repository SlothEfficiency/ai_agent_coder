# 🤖 AI Agent Coder

This repository contains a Python-based AI agent powered by Google's Gemini AI that understands natural language commands to manipulate files and execute code. The agent can:

## ✨ Features
- Navigate and manage files in your directory
- Read and write file contents
- Execute Python files
- Access file metadata


### 🛠️ Available Functions
- 📊 `get_files_info`: Get metadata about files (size, permissions, etc.)
- 📖 `get_file_content`: Read and display file contents
- ✏️ `write_file`: Create or modify files
- 🏃 `run_python_file`: Execute Python scripts

## 🧮 Example Usage - Calculator Package
To showcase the agent's abilities, the package `calculator` was created. It contains a calculator class capable of processing simple arithmetic operations (addition, subtraction, multiplication, and division). The calculator requires input where operators and numbers are separated by spaces (e.g., "3 + 7 * 2"). Using the Shunting Yard algorithm, mathematical operations are executed according to operator precedence.

Note: For demonstration purposes, the addition operator has higher precedence than multiplication and division operators.

## 📥 Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
    pip install pip-tools
    pip-compile pyproject.toml
    pip install -r requirements.txt
   ```
4. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🚀 Usage

Run the agent with a prompt:
```bash
python main.py "Edit the file xy such that it does this and that."
```

For detailed output, use the verbose flag:
```bash
python main.py "Run the file xy." --verbose
```

### 💡 Command Examples

```bash
# List files in current directory
python main.py "Show me all files in this directory"

# Read a specific file
python main.py "Show me the contents of main.py"

# Execute a Python script
python main.py "Run calculator.py with input 2+2"

# Create or modify a file
python main.py "Create a new file called test.py with a simple print statement"
```


