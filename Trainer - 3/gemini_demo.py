import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what is API",
    temperature=0.5
)

print("Gemini Response:\n", response.text)






# import os

# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     raise RuntimeError("GROQ_API_KEY is missing. Add it to the .env file or your environment.")

# client = Groq(api_key=api_key)

# prompt = """Classify the sentiment of the review as Positive and Negative.
# Example:
# Review: "The food was cold and the service was slow."
# Sentiment: Negative

# Now classify this:
# Review: "Amazing ambience, the staff was super friendly!"
# Sentiment: """

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {"role": "user", "content": prompt}
#     ],
#     temperature=0.7,
# )

# print("Groq Response:\n", response.choices[0].message.content)