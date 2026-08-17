import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Chatbot is ready. Type 'exit' to quit.\n")

messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Bot: {reply}\n")
