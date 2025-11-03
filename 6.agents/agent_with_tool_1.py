import warnings
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
# from pydantic import BaseModel

warnings.filterwarnings(action="ignore")

load_dotenv()

@tool
def multiply(input: str) -> int:
    """Multiply two numbers provided as a comma-separated string."""
    a, b = map(int, input.split(","))
    return a * b

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

prompt = hub.pull("hwchase17/react") # pulls prompt from https://smith.langchain.com/hub/hwchase17/react

my_agent = create_react_agent(
    llm=llm,
    tools=[multiply],
    prompt=prompt
)

my_executor = AgentExecutor(
    agent=my_agent,
    tools=[multiply],
    verbose=True
)

result = my_executor.invoke({"input":"Hi how are you?"})
# result = my_executor.invoke({"input":"What is multiplication of 5 and 7"})

print(result['output'])