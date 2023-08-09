 # facilitator.py                                                                                                                       
from langchain import ChatOpenAI

class Facilitator:
    def __init__(self, temperature):
        self.llm = ChatOpenAI(temperature=temperature, model="gpt-4")

    def guide(self, question, history):
        response = self.llm.run(question=question, history=history.get_full_history())
        return response