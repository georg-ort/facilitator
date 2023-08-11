 # facilitator.py                                                                                                                       

import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config.config import Config

class Facilitator:
    def __init__(self, temperature):
        self.temperature = temperature
        self.llm = ChatOpenAI(temperature=self.temperature, model="gpt-4")
        
        self.prompt = PromptTemplate.from_template(Config.PROMPT_TEMPLATE)
        
        self.chain = LLMChain(prompt=self.prompt, llm=self.llm )
        
        self.llm = ChatOpenAI(temperature=temperature, model="gpt-4")

    def guide(self, question, history):
        response = self.llm.run(question=question, history=history.get_full_history())
        return response