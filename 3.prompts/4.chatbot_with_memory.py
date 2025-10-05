from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

memory=[]
while True:
    query = input("You: ")
    if query == "exit()":
        break
    memory.append(query)
    response = llm.invoke(memory)
    memory.append(response.content)
    print("AI: ", response.content)