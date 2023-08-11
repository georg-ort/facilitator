 # main.py                                                                                                                              
from participant import HumanParticipant, AIParticipant
from facilitator import Facilitator
from history import History
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


# Initialize the history
history = History()



# Initialize the participants
participants = [
    HumanParticipant("Human 1"),
    AIParticipant("AI 1", "You are a genius math professor", 0.5),
    HumanParticipant("Human 2"),
    AIParticipant("AI 2", "You are a genius scientist", 0.6),
]

# Initialize the facilitator
facilitator = Facilitator(temperature=0.5, participants=participants)

proposal = input("Please enter your proposal: ")

# Start the meeting
facilitator.start(proposal)


while True:
    for participant in participants:
        response = participant.respond(question, history)
        question = facilitator.guide(response, history)