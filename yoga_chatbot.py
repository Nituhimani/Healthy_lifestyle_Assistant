import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

# Configure your Gemini API key here
# It's recommended to set this as an environment variable
# For example: os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"
MODEL_NAME = 'gemini-1.5-flash'
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_user_info():
    """Gathers user information."""
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid age. Please enter a number.")
    gender = input("Enter your gender (male/female/other): ").lower()
    while gender not in ["male", "female", "other"]:
        print("Invalid gender. Please enter 'male', 'female', or 'other'.")
        gender = input("Enter your gender (male/female/other): ").lower()
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            break
        except ValueError:
            print("Invalid height. Please enter a number.")
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            break
        except ValueError:
            print("Invalid weight. Please enter a number.")
    
    health_issues = input("Do you have any health-related issues you are facing? (yes/no): ").lower()
    if health_issues == 'yes':
        health_issues_details = input("Please describe your health issues: ")
    else:
        health_issues_details = "None"
        
    while True:
        problem_count = 0
        problems_improvements = []
        print("Please describe 2-3 problems or areas you'd like to improve (e.g., 'stress reduction', 'flexibility', 'weight loss'). Type 'done' when finished.")
        for i in range(1, 4):
            problem = input(f"Problem/Improvement {i} (or 'done'): ")
            if problem.lower() == 'done':
                if problem_count == 0:
                    print("Please enter at least one problem/improvement.")
                    continue # Ask for input again if no problems were entered
                else:
                    break
            problems_improvements.append(problem)
            problem_count += 1
        if problem_count > 0:
            break # Exit if at least one problem was entered

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "health_issues": health_issues_details,
        "problems_improvements": problems_improvements
    }

def generate_recommendations(user_info):
    """Generates yoga and food recommendations using Gemini API."""
    try:
        # It's recommended to set your API key as an environment variable
        # For example: export GEMINI_API_KEY="YOUR_API_KEY" in your terminal
        # Or, uncomment the line below and replace with your actual key (not recommended for production)
        # genai.configure(api_key="YOUR_API_KEY")
        
        # If using environment variable, it will be automatically picked up
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
        Given the following user information, provide a personalized recommendation for a healthy lifestyle, including specific yoga poses and food intake suggestions.

        User Information:
        - Name: {user_info['name']}
        - Age: {user_info['age']}
        - Gender: {user_info['gender']}
        - Height: {user_info['height']} cm
        - Weight: {user_info['weight']} kg
        - Health Issues: {user_info['health_issues']}
        - Problems/Improvements: {', '.join(user_info['problems_improvements'])}

        Please structure your response clearly with the following sections:
        1.  **Healthy Lifestyle Advice:** General advice based on the user's profile.
        2.  **Yoga Recommendations:**
            -   List 3-5 specific yoga poses.
            -   Briefly explain the benefit of each pose related to the user's goals.
            -   Suggest a frequency (e.g., "daily", "3 times a week").
        3.  **Food Intake Recommendations:**
            -   Suggest specific food groups or items.
            -   Explain why they are beneficial for the user's goals.
            -   Provide general dietary advice.
        """

        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=0.5))
        return response.text

    except Exception as e:
        return f"An error occurred while generating recommendations: {e}. Please ensure your GEMINI_API_KEY is correctly set."

def main():
    print("Welcome to the Yoga Recommendation Chatbot!")
    user_data = get_user_info()
    print("\nGenerating recommendations for you...")
    recommendations = generate_recommendations(user_data)
    print("\n--- Your Personalized Recommendations ---")
    print(recommendations)
    print("\n--- End of Recommendations ---")

if __name__ == "__main__":
    main() 