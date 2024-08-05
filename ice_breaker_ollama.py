import os
import sys

from dotenv import load_dotenv

from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

"""
Prompt Template = help translate user input and parameters into instruction for a LM. Prompt template take as input a dictionary, where each key represents a variable in the prompt template and the value is the value of that variable. The prompt template then uses these variables to generate a prompt string that is passed to the language model.

Chat models = wrapper around LLM that allow us to interact with them.

LLM Chains = allow us to combine multiple components together creating one single, coherent application.
"""

information = """
Jason Statham is an English actor and martial artist. He is known for portraying characters in various action-thriller films who are typically tough, gritty, or violent. Statham has been credited for leading the resurgence of action films during the 2000s and 2010s.[1] His film career through 2017 generated over $1.5 billion (£1.1 billion) in ticket sales, making him one of the film industry's most bankable stars.[2][3]

Statham began practising Chinese martial arts, kickboxing, and karate recreationally in his youth while working at local market stalls. An avid footballer and diver, he was a member of Britain's national diving team and competed for England in the 1990 Commonwealth Games. Shortly after, he was asked to model for French Connection, Tommy Hilfiger, and Levi's in various advertising campaigns. His past history working at market stalls inspired his casting in the Guy Ritchie crime films Lock, Stock and Two Smoking Barrels (1998) and Snatch (2000).

The commercial success of these films led Statham to star as Frank Martin in the Transporter trilogy (2002–2008). After starring in a variety of heist and action-thriller films such as The Italian Job (2003), Crank (2006), War (2007), The Bank Job (2008), The Mechanic (2011), Spy (2015), and Mechanic: Resurrection (2016), he established himself as a Hollywood leading man. However, he has also starred in commercially and critically unsuccessful films such as Revolver (2005), Chaos (2005), In the Name of the King (2007), 13 (2010), Blitz (2011), Killer Elite (2011), Hummingbird (2013), and Wild Card (2015). He regained commercial success as a part of the ensemble action series The Expendables (2010–2014) and the Fast & Furious franchise, playing Deckard Shaw in several films, including the spin-off Hobbs & Shaw (2019)
"""


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file - no need to generate the launch.json file

    summary_template = """
        given the information {information} about a person, I want you to generate:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=1000)

    # Use Llama3 model
    # llm = ChatOllama(model="llama3")

    # Use Mistral model
    llm = ChatOllama(model="mistral")

    chain = (
        summary_prompt_template | llm | StrOutputParser()
    )  # The output is a AI message object that has a content attribute that contains the response from the model. Output parser can be used to take the output if a model and transform it into a more usable object.

    res = chain.invoke(input={"information": information})

    print(res)
