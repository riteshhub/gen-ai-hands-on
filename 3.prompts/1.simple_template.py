from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

template = PromptTemplate.from_template("Tell me five characteristics of {plant_name} plant")

parser = StrOutputParser()

chain = template | llm | parser
result = chain.invoke({"plant_name": "mogra"})

print(result)