import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import messages_from_dict, messages_to_dict, AIMessage, HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder(variable_name="chat_history", n_messages=4),
        ("human", "{query}")
    ]
)

parser = StrOutputParser()

file_path="conversation.json"
memory=[]

# read previous conversation from file
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        memory_data = json.load(f)
        memory = messages_from_dict(memory_data)

except FileNotFoundError: # create file if not exists 
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)

print(f"previous conversations: {memory}")

while True:
    query = input("You: ")
    if query == "exit()":
        break
    
    memory.append(HumanMessage(content=query))
    chain = prompt | llm | parser
    result = chain.invoke({"chat_history":memory, "query":query})
    memory.append(AIMessage(content=result))
    print(f"AI: {result}")

# write list of messages back to conversation file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(messages_to_dict(memory), f, ensure_ascii=False, indent=2)
