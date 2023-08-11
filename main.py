 # main.py     
import os
from dotenv import load_dotenv, find_dotenv                                                                                                                   
from participant import HumanParticipant, AIParticipant
from facilitator import Facilitator
from history import History

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Initialize the history
history = History()


# Initialize the participants
participants = [
    HumanParticipant("Bob"),
    AIParticipant("AxiomFlow", "You are a genius math professor", 0.5),
    HumanParticipant("Berta"),
    AIParticipant("QuantumNode", "You are a genius scientist", 0.6),
]

proposal = input("Please enter your proposal: ")

# Initialize the facilitator
facilitator = Facilitator(temperature=0.5, participants=participants, history=history)

# Start the meeting
facilitator.guide(proposal)

""" 
while True:
    for participant in participants:
        response = participant.respond(question, history)
        question = facilitator.guide(response, history) """