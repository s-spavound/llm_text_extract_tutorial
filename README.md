# Tutorial: Extracting Unstructured Text Using Large Language Models

This repository contains code to accompany the paper Spavound, S., and Schaer, O., and Markou, P.,, Tutorial: Extracting Unstructured Text Using Large Language Models (April 10, 2026). Available at SSRN: https://ssrn.com/abstract=6556303.

## Prerequisites

### 1. OpenAI API Setup
This tutorial requires a paid OpenAI developer account. Follow these steps to generate your credentials:

* **Account & Billing:** Go to the [OpenAI Platform](https://platform.openai.com/) and sign up. You must add a payment method and purchase a minimum of $5 in credits to activate your API access (Tier 1).
* **Generate Key:** Navigate to the **API Keys** section and click "Create new secret key." 
* **Security:** Save this key immediately in a secure location. You will not be able to view it again. 
* **Environment Variable:** For security, do not hard-code your key. Set it as an environment variable in your terminal:
    * **macOS/Linux:** `export OPENAI_API_KEY='your-key-here'`
    * **Windows:** `setx OPENAI_API_KEY "your-key-here"`

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

## Usage

1. Open the `tutorial_example.ipynb` tutorial files in your preferred editor (JupyterLab, Jupyter Notebook, or VS Code).
2. Select your Python kernel.
3. Execute the cells sequentially.