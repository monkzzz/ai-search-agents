from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from langchain.chains import LLMMathChain
from langchain.agents import Tool, initialize_agent
from langchain_community.tools import DuckDuckGoSearchRun

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = hub.pull("hwchase17/openai-functions-agent")

llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
math_tool = Tool.from_function(
        func=llm_math_chain.run,
        name="Calculator",
        description="Useful for when you need to answer questions about math. This tool is only for math questions and nothing else. Only input math expressions.",
    )

search = DuckDuckGoSearchRun()

tools = [math_tool, search]

agent = create_openai_functions_agent(llm= llm, tools = tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": "Who won the 2021 world series and how many years was it since their last world series win"})