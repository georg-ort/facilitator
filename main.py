 # main.py                                                                                                                              
 from participant import HumanParticipant, AIParticipant                                                                                
 from facilitator import Facilitator                                                                                                    
 from history import History                                                                                                            
                                                                                                                                        
 # Initialize the history                                                                                                               
 history = History()                                                                                                                    
                                                                                                                                        
 # Initialize the facilitator                                                                                                           
 facilitator = Facilitator(temperature=0.5)                                                                                             
                                                                                                                                        
 # Initialize the participants                                                                                                          
 participants = [                                                                                                                       
     HumanParticipant("Human 1"),                                                                                                       
     AIParticipant("AI 1", "You are a genius math professor", 0.5),                                                                     
     HumanParticipant("Human 2"),                                                                                                       
     AIParticipant("AI 2", "You are a genius scientist", 0.6),                                                                          
 ]                                                                                                                                      
                                                                                                                                        
 # Start the decision-making process                                                                                                    
 question = input("Please enter your proposal: ")                                                                                       
 while True:                                                                                                                            
     for participant in participants:                                                                                                   
         response = participant.respond(question, history)                                                                              
         question = facilitator.guide(response, history) 