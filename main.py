import os

from dotenv import load_dotenv

# loading .env file to use environment variables
load_dotenv()  # this will load .env file variables to the code


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
