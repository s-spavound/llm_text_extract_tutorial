# LLM Text Extraction Tutorial

This repository contains code to accompany the paper **"Tutorial: Extracting Unstructured Text Using Large Language Models"** by Simon Spavound, Oliver Schaer, and Panos Markou.

## Prerequisites

### 1. OpenAI API Setup
This tutorial requires a paid OpenAI developer account. Follow these steps to generate your credentials:

* **Account & Billing:** Go to the [OpenAI Platform](https://platform.openai.com/) and sign up. You must add a payment method and purchase a minimum of $5 in credits to activate your API access (Tier 1).
* **Generate Key:** Navigate to the **API Keys** section and click "Create new secret key." 
* **Security:** Save this key immediately in a secure location. You will not be able to view it again.
* **Usage:** We do not recommend keeping it hard-coded in your code - for this tutorial we show where to enter your code but for more secure usage we recommend the use of environment variables.
<!-- * **Environment Variable:** For security, do not hard-code your key. Set it as an environment variable in your terminal:
    * **macOS/Linux:** `export OPENAI_API_KEY='your-key-here'`
    * **Windows:** `setx OPENAI_API_KEY "your-key-here"` -->

### 2. System Dependencies (Poppler)
The `pdf2image` library requires **Poppler**, a system-level PDF rendering library. You must install it based on your operating system:

* **Linux (Ubuntu/Debian):** `sudo apt-get install poppler-utils`
* **macOS:** `brew install poppler`
* **Windows:** Download binaries from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/), extract them, and add the `bin` folder to your system **PATH**.

### 3. Python Environment Setup
The required Python packages are listed in `requirements.txt`. Follow these steps to isolate the dependencies and ensure the code runs with the correct versions.

**Create and activate the virtual environment:**
```bash
# Create the environment
python3 -m venv .venv

# Activate the environment (macOS/Linux)
source .venv/bin/activate

# Activate the environment (Windows)
.venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Jupyter Kernel Registration
To use this environment within the Jupyter Notebook interface (or VS Code), you must register the environment as a kernel.

```bash
python -m ipykernel install --user --name=llm_tutorial --display-name "Python (LLM Tutorial)"
```

## Usage

1. Open the `tutorial_example.ipynb` tutorial files in your preferred editor (JupyterLab, Jupyter Notebook, or VS Code).
2. Select the **"Python (LLM Tutorial)"** kernel from the kernel picker or dropdown menu.
3. Execute the cells sequentially.