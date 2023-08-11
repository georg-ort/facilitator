 # facilitator.py                                                                                                                       

import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config.config import Config

class Facilitator:
    def __init__(self, temperature, participants, history):
        self.temperature = temperature
        self.llm = ChatOpenAI(temperature=self.temperature, model="gpt-4")  
        self.prompt = PromptTemplate.from_template(Config.FACILITATOR_PROMPT_TEMPLATE)
        self.chain = LLMChain(prompt=self.prompt, llm=self.llm )
        self.participants = participants
        self.history = history
        

    def guide(self, proposal):
        while True:
            response = self.chain.run(proposal=proposal, history=self.history.get_full_history())
            if response == "end meeting":
                return False
        
