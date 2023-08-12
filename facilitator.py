 # facilitator.py                                                                                                                       

import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config.config import Config
from loguru import logger
from langchain.callbacks import FileCallbackHandler

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

# logging
logger.add("all_log.log", colorize=True, enqueue=True)
handler = FileCallbackHandler(logger)


# Structured Answer from Facilitator
class FacilitatorResponse(BaseModel):
    text: str = Field(description="the whole text what the facilitator says")
    current_proposal: str = Field(description="the current proposal")
    next_step: str = Field(description="what the facilitator wants to do next (speak_to_group, speak_to_participant, end_meeting)")
    participant: str = Field(description="who the facilitator wants to speak to next")
    
    # You can add custom validation logic easily with Pydantic.
    @validator('next_step')
    def valid_next_step(cls, field):
        # field must be one of speak_to_group, speak_to_participant, end_meeting, abort_meeting
        if field not in ["speak_to_group", "speak_to_participant", "end_meeting", "abort_meeting"]:
            raise ValueError("Invalid next step. Must be one of speak_to_group, speak_to_participant, end_meeting, abort_meeting")
        return field



class Facilitator:
    def __init__(self, temperature, participants, history, name = "Aime"):
        self.name = name
        self.temperature = temperature
        self.participants = participants
        self.history = history
        self.llm = ChatOpenAI(temperature=self.temperature, model="gpt-4-0613")  
        
        self.parser = PydanticOutputParser(pydantic_object=FacilitatorResponse)
        
        self.prompt = PromptTemplate.from_template(Config.FACILITATOR_PROMPT_TEMPLATE)
        
        self.chain = LLMChain(prompt=self.prompt, 
                              llm=self.llm, 
                              callbacks=[handler], 
                              verbose=True )
        
        
    
    def get_participant_names(self) -> str :
        return ', '.join([participant.name for participant in self.participants])    


    # Actually run the facilitator
    def run(self, proposal) -> FacilitatorResponse:
        response = self.chain.run(proposal=proposal, 
                                  history=self.history.get_full_history(), 
                                  participant_list=self.get_participant_names(), 
                                  format_instructions=self.parser.get_format_instructions(),
                                  name=self.name,
                                  verbose=True)
        parsed_response = self.parser.parse(response)
        logger.info(parsed_response)
        return parsed_response


    # Logic how the facilitator guides the group
    def guide(self):
        
        print("""           
----------------------------------      
Welcome to the facilitator demo!
""")
        
        initial_proposal = input("Please enter your proposal: ")
        
        tmp_inc = 0
        
        while True:
            tmp_inc += 1
            
            parsed_response = self.run(initial_proposal)
            
            print(parsed_response["text"])
            
            # What does the facilitator whant to do next?
            
            # speak_to_group
            if parsed_response["next_step"] == "speak_to_group":
                self.history.add_to_history("Facilitator", parsed_response["text"])
                
            # speak_to_participant
            elif parsed_response["next_step"] == "speak_to_participant":  
                participant = next(participant for participant in self.participants if participant.name == parsed_response["participant"])
                response = participant.respond(parsed_response["text"], self.history)
                self.history.add_to_history(participant.name, response)
            
            # end_meeting
            elif parsed_response["next_step"] == "end_meeting":
                current_proposal=parsed_response["current_proposal"]
                print(f"""    
------                        
Final Proposal: 
{current_proposal}
------

""", )
                
                break
               
            # abort_meeting
            elif parsed_response["next_step"] == "abort_meeting":
                break
            elif tmp_inc > 3:
                break
            
        
        print("""      
             
Goodbye!
----------------------------------""")
                
        return
    
    
