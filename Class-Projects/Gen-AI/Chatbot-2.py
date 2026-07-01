import os

from google import genai

# Keep API key private
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set GEMINI_API_KEY before running this chatbot.")

client = genai.Client(api_key=api_key)

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

Rules:
1. If the question is about Ankit's education, skills, projects, internship, certifications, achivements or experience, use the information provided below.
2. If answer is not presnet in Ankits Information, answer using your general knowledge.

2. Be concise and helpful.

Information:
{my_data}

Question:
{question}
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nBot:", response.text)

    # Save chat history
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {question}\n")
        file.write(f"Bot: {response.text}\n")
        file.write("-" * 50 + "\n")

except Exception as e:
    print("\nError:", e)
