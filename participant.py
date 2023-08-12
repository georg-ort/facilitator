# participant.py
from abc import ABC, abstractmethod
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config.config import Config


class Participant(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def respond(self, question, history):
        pass


class HumanParticipant(Participant):
    def respond(self, question, history):
        response = input(question)
        history.add_to_history(self.name, response)
        return response


class AIParticipant(Participant):
    def __init__(self, name, backstory, temperature):
        super().__init__(name)
        self.backstory = backstory
        self.temperature = temperature
        self.llm = ChatOpenAI(temperature=self.temperature, model="gpt-4")
        self.prompt = PromptTemplate.from_template(
            Config.AIPARTICIPANT_PROMPT_TEMPLATE)
        self.chain = LLMChain(prompt=self.prompt, llm=self.llm)

    def respond(self, question, history):
        response = self.chain.run(question=question, history=history.get_full_history(), name=self.name,
                                  backstory=self.backstory)
        history.add_to_history(self.name, response)
        return response
