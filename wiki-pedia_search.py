from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = hub.pull("hwchase17/openai-functions-agent")

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)

tools = [WikipediaQueryRun(api_wrapper=api_wrapper)]

agent = create_openai_functions_agent(
    llm,
    tools,
    prompt
    )

agent_executor = AgentExecutor(agent=agent, tools=tools)

result = agent_executor.invoke({"input": "Who won won the 2023 world series? If you don't know please look it up on wikipedia and give the source link"})
print ("")
print ("Result")
print (result)
print ("")