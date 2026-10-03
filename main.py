from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def english_teacher(text):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions="""
You are a friendly English teacher.

When the user gives you an English sentence or text:

1. Explain the meaning in simple English.
2. Explain important vocabulary.
3. Explain the grammar simply.
4. Give 2 example sentences.
5. Give the user 3 short practice questions.

Keep the explanation clear and suitable for an intermediate English learner.
""",
        input=text
    )

    return response.output_text


text = input("Give me an English sentence or text: ")

result = english_teacher(text)

print("\n--- ENGLISH TEACHER ---\n")
print(result)