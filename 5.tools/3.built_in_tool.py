from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchResults

xyz = DuckDuckGoSearchResults()

print(xyz.invoke("ayurveda presence outside India"))