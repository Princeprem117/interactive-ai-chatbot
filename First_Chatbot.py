import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list stores the full conversation history
os.makedirs("chat_history", exist_ok=True)

history_file = "chat_history/history.json"
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are a friendly and helpful AI assistant. "
            "Keep answers concise, simple, and easy to understand."
            "allign every line clearly of your answer"
        )
    }
]
if os.path.exists(history_file):
    try:
        with open(history_file, "r") as file:
            conversation_history = json.load(file)
    except json.JSONDecodeError:
        conversation_history
else:
    conversation_history

print("\nCHATBOT🤖 is ready! \n Type 'bye' or 'quit' to exit.")
print("-" * 40)

while True:
    # Take input from user
    user_input = input("You: ")
    
    if user_input.lower() == "bye" or user_input.lower() == "quit":
        print("Goodbye!\n Thank you for chatting with me.\n If you want to chat again, just run the program again...😊🫡")
        break
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send full history to Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation_history
    )
    
    # Get the reply
    reply = response.choices[0].message.content
    
    # Add assistant reply to history too
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    with open(history_file, "w") as file:
        json.dump(conversation_history, file, indent=4)

    print(f"Bot: {reply}")
    print("-" * 40)