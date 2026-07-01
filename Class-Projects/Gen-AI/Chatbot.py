import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Gemini API
# ----------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
my_data = """
Summary:
Computer Science Engineering

Contact Information:
Phone: 9102369979
Email: nwdankit701@gmail.com
"""

print("Ankit AI chatbot started...")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    prompt = f"""
You are Ankit Kumar's personal AI assistant.

# Use ONLY the information below to answer questions.
Use ONLY the information below to answer questions
If the answer is not available in the information, say:
"I don't have that information."

Information:
{my_data}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nBot:", response.text)
    print()



# from google import genai

# client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# my_data = """
# Summary:
# computer science Engineering

# Contact Informatino:
# Phone: 9102369979
# Email: [nwdankit701@gmail.com]
# """

# print("Ankit AI chatbot started...")
# print("Type 'exit to quit.\n")

# while True:
#     question = input("You: ")

#     if question.lower() == "exit":
#         print("Bot: Goodbye!")
#         break
#     prompt = """
# You are Ankit Kumar's personal AI assistant.

# the ONLY the information below to answer to answer questions.

# Information:
# {my_data}

# Question:
# {Question}
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt
#     )

#     print("\nBot:", response.text)
#     print()
