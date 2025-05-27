import sys
import google.generativeai as genai

def main():
    print("Welcome to the Gemini 2.0 Flash AI Bot!")
    api_key = input("Please enter your Gemini API key: ").strip()
    if not api_key:
        print("API key is required. Exiting.")
        sys.exit(1)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
    except Exception as e:
        print(f"Failed to initialize Gemini client: {e}")
        sys.exit(1)

    print("Type 'exit' or 'quit' to end the session.")
    while True:
        prompt = input("enter prompt: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not prompt:
            print("Please enter a prompt.")
            continue
        try:
            response = model.generate_content(prompt)
            print("Response:", response.text)
        except Exception as e:
            print(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
