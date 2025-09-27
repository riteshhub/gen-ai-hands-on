from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation",
    temperature=0
)

llm = ChatHuggingFace(llm=model)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)