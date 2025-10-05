from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

while True:
    query = input("You : ")
    if query == "exit()":
        break
    response = llm.invoke(query)
    print("AI : ", response.content)