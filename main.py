from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from transformers.utils.logging import set_verbosity_error

load_dotenv()
set_verbosity_error()

llm =  HuggingFacePipeline.from_model_id(
    model_id="openai-community/gpt2",
    task="text-generation",
    model_kwargs={"temperature": 0, "max_length": 512}
)


print(llm.invoke("Explain the theory of relativity in 200 words."))