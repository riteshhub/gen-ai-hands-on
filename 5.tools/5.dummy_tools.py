from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location"""
    # For demonstration purposes, we'll return a static response.
    # In a real implementation, you would call a weather API here.
    print("Tool used: get_current_weather")
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@tool
def get_news(topic: str) -> str:
    """Get the latest news on a given topic"""
    # For demonstration purposes, we'll return a static response.
    # In a real implementation, you would call a news API here.
    print("Tool used: get_news")
    return f"The latest news on {topic} is that AI is transforming the tech industry."

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

llm_with_tools = llm.bind_tools([get_current_weather,get_news])

# result = llm_with_tools.invoke("How are you?")
# result = llm_with_tools.invoke("what is the latest news on Cricket")
# result = llm_with_tools.invoke("get me today's weather for Indore")
result = llm_with_tools.invoke("what is the latest news of Indore and also get the current weather for the city Pune")

print(result)

if result.content=='':
    for item in result.tool_calls:
        tool_name = item['name']
        tool_args = item['args']
        if tool_name == 'get_news':
            result = get_news.invoke(tool_args)
            print(result)
        elif tool_name == 'get_current_weather':
            result = get_current_weather.invoke(tool_args)
            print(result)