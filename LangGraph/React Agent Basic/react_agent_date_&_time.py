from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent,tool
from langchain_community.tools import TavilySearchResults
# Date_time_mod
import datetime 

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
search_tool=TavilySearchResults(search_depth="basic")
@tool
def get_system_time(format:str="%Y-%m-%d %H:%M:%S"):
    """ Return the current data and time in the specified format"""
    current_time=datetime.datetime.now()
    formatted_time=current_time.strftime(format)
    return formatted_time
tools=[search_tool,get_system_time]
agent=initialize_agent(tools=tools,llm=llm,agent="zero-shot-react-description",verbose=True)
agent.invoke("When was the ISRO's last launch and how many days ago was the that from this instant")

