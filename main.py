 # main.py     
import os
from dotenv import load_dotenv, find_dotenv                                                                                                                   
from participant import HumanParticipant, AIParticipant
from facilitator import Facilitator
from history import History
from loguru import logger
from config.config import Config


load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# logging
logger.add(Config.LOGFILE, level=Config.LOGGING_LEVEL, colorize=True, enqueue=True)

# Initialize the history
history = History()


# Initialize the participants
participants = [
    HumanParticipant("Fry"),
    AIParticipant("C-3PO", "You are a friendly, polite and helpful robot", 0.2),
    HumanParticipant("Professor Farnsworth"),
    AIParticipant("Bender", "You are a bending robot with an alcohol addiction. You are not very helpful and like to create trouble.", 1)
]

# Initialize the facilitator
facilitator = Facilitator(temperature=0.2, participants=participants, history=history)

# Start the meeting
facilitator.guide()
