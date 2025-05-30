from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# result = llm.invoke("Tell me a coding joke")
search_tool=TavilySearchResults(search_depth="basic")
tools=[search_tool]
agent=initialize_agent(tools=tools,llm=llm,agent="zero-shot-react-description",verbose=True)
# zero-shot-react-description  -> means the agent have no prior knowledge

# result = llm.invoke("Give me latest today tweet of the PM modi ")
agent.invoke("Give me today's latest  tweet of the PM modi ")
# print(result)
