from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)