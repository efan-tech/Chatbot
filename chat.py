import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize the Gemini Client
api_key = os.getenv("api_key")
client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-3.5-flash-lite")

KNOWLEDGE_FILE = "knowledge.txt"

# Read your knowledge data as a clean string
knowledge_context = ""
if os.path.exists(KNOWLEDGE_FILE):
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        knowledge_context = f.read().strip()
    print("Successfully loaded knowledge.txt base data!\n")
else:
    print(f"Warning: '{KNOWLEDGE_FILE}' not found. Running without custom data.\n")

print("Gemini RAG Chatbot started!")
print("Type 'exit' to stop. \n")

while True:
    user_query = input("You: ")
    
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
        
    # Inject your file information smoothly into the instructions
    prompt_to_send = user_query
    if knowledge_context:
        prompt_to_send = (
            f"Use the following custom business or personal document context to answer the question if relevant:\n"
            f"--- START CONTEXT ---\n{knowledge_context}\n--- END CONTEXT ---\n\n"
            f"User Question: {user_query}"
        )

    try:
        response = chat.send_message(prompt_to_send)
        print("Gemini:", response.text)
    except Exception as error:
        print("Error:", error)
# So how can I use the rug? Can I be able to use it in terms and how would I be able to use this to create rug?
