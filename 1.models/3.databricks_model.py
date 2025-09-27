from dotenv import load_dotenv
from databricks_langchain import ChatDatabricks

load_dotenv()

llm = ChatDatabricks(
    model="databricks-llama-4-maverick",
    temperature=0
)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)