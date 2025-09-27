from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline

load_dotenv()

llm =  HuggingFacePipeline.from_model_id(
    model_id="LiquidAI/LFM2-350M",
    task="text-generation",
)

result = llm.invoke(input="What are the most spoken languages in the world?")

print(result)