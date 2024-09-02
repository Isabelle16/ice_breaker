import os
import sys
from dotenv import load_dotenv

sys.path.append(r"C:\Users\ISAM\Documents\GitHub\ice_breaker\tools")
from tools.tools import get_profile_url_tavily

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Tools are interfaces that help the LLM/agents to interact with the outside world (online, databases, etc). Tools are objects that have the following information:
# a function to execute
# a description describing what the function does -> very important because the LLM will use that description
# a name, inherited from the basetool object

# The tool that our agent will be using is a search tool that has the capability to search online. LKangchain allows to convert any fpython function into a langchain tool and make it accessibe to our LLM

# React is the most popular way to implement an agent with an LLM.
# The create_react_agent is a built-in function that receives the LLM that we use, tools and a promp (called React prompt) and returns a React agent.

# AgentExecutor is the runtime of the agent. It is responsible for executing the agent and returning the result.

# langchain hub -> a place where you can find agents, tools, and prompts that are already built and ready to use.


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to provide a link of their LinkedIn profile. Exclude URL of the page with the list of linkedin profiles with same name. Your answer should be only a URL.
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin personal profile page",  # the name will be supplied to the reasoning engine and displayed in the logs
            description="Useful when you need to provide the person Linkedin page URL",  # super-important, the LLM will use this description to determine if the tool is relevant to the prompt
            func=get_profile_url_tavily,
        )
    ]

    react_prompt = hub.pull("hwchase17/react")  # popular prompt for ReAct prompting
    agent = create_react_agent(
        llm=llm,
        prompt=react_prompt,
        tools=tools_for_agent,
    )
    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True
    )  # agent runtime

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_url = result["output"]
    return linkedin_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Isabella Masiero")
