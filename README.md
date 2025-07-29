# Healthy_lifestyle_Assistant

## Project Description
This is a Python-based chatbot that provides personalized healthy lifestyle recommendations, including yoga poses and food intake suggestions, based on user-provided information. It leverages the Google Gemini API for generating these recommendations.

## Features
- Gathers user information such as name, age, gender, height, weight, health issues, and areas for improvement.
- Validates user input for numerical fields and gender.
- Generates personalized healthy lifestyle advice using the Gemini API.
- Provides specific yoga pose recommendations with benefits and frequency suggestions.
- Offers food intake recommendations with explanations and general dietary advice.
- Handles potential API errors and provides informative messages.

## Setup Instructions

### Prerequisites
- Python 3.8+
- A Google Gemini API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nituhimani/Healthy_lifestyle_Assistant.git
    cd Healthy_lifestyle_Assistant
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Gemini API Key:**
    Create a file named `.env` in the root directory of the project (the same directory as `yoga_chatbot.py`).
    Add your Gemini API key to this file in the following format:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
    Replace `"YOUR_API_KEY_HERE"` with your actual Gemini API key, ensuring it's enclosed in double quotes.

## How to Run

To start the chatbot, run the `yoga_chatbot.py` script from your terminal:

```bash
python yoga_chatbot.py
```

The chatbot will then prompt you to enter your personal information to generate tailored recommendations.

## Example Usage
```
Welcome to the Yoga Recommendation Chatbot!
Enter your name: Himani
Enter your age: 22
Enter your gender (male/female/other): female
Enter your height in cm: 152
Enter your weight in kg: 40
Do you have any health-related issues you are facing? (yes/no): yes
Please describe your health issues: mental health
Please describe 2-3 problems or areas you'd like to improve (e.g., 'stress reduction', 'flexibility', 'weight loss'). Type 'done' when finished.
Problem/Improvement 1 (or 'done'): stress
Problem/Improvement 2 (or 'done'): anxiety
Problem/Improvement 3 (or 'done'): sleeplessness

Generating recommendations for you...

--- Your Personalized Recommendations ---
**1. Healthy Lifestyle Advice:**
... (Gemini API generated content) ...
--- End of Recommendations ---
```

## Troubleshooting
- **`ModuleNotFoundError: No module named 'google'`**: Ensure you have installed the dependencies using `pip install -r requirements.txt` and are running the script within the correct Python environment.
- **`404 models/gemini-pro is not found...` or `429 You exceeded your current quota...`**: This indicates an issue with your Gemini API key, model availability, or usage quota.
    - Double-check that `GEMINI_API_KEY` in your `.env` file is correct and active.
    - Verify the model name in `yoga_chatbot.py` (`MODEL_NAME`) matches an available model for your region (e.g., `'gemini-1.5-flash'`).
    - If using a free API key, you might have hit a rate limit. Quotas usually reset after a certain period. Check your Google Cloud project's API & Services -> Quotas for details on your specific limits.
