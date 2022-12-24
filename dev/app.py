# Simple chatbot app using openAI. Takes input from the user on the command line and responds by relating
# the user's message to the chatbot's love of a person named 'Hilary'

# Import the necessary modules
import os
import random as rand
from time import sleep
import dotenv as env
import spacy as sp
import openai as ai 
import pyi_splash as splash
import en_core_web_sm as spacy_model

# Load splash screen
if splash.is_alive():
    try:
        splash.update_text("Loading Complete")
        splash.close()
    except ConnectionError:
        print("unable to load splash screen")
    except RuntimeError:
        print("pyi_splash not initialized")

# Load the environment variables from the .env file
env.load_dotenv()
OPENAI_API_KEY = os.getenv("HILLYBOT_API")

# Define the welcome text to appear on load
WELCOME = """
  _     _ _ _       _           _   
 | |__ (_) | |_   _| |__   ___ | |_ 
 | '_ \| | | | | | | '_ \ / _ \| __|
 | | | | | | | |_| | |_) | (_) | |_ 
 |_| |_|_|_|_|\__, |_.__/ \___/ \__|
              |___/                 
"""

# Define a database of facts about 'Hilary' for the agent to choose from
HILLY_FACTS = [
    "Hilly loves to paint",
    "Hilly is an avid knitter",
    "Hilly plays multiple instruments, including the clarinet and the piano, and she likes to sing",
    "Hilly speak multiple languages, including several she invented with her sister",
    "Hilly is an artistic and creative person",
    "Hilly lives in the South East of England",
    "Hilly went to Southampton University, where she got a Bachelors in French",
    "Hilly is attracted to people regardless of gender",
    "Hilly loves to read",
    "Hilly is a writer, and has written several books, including one called 'This Still Happens'",
    "Hilly has a piss fetish",
    "Hilly is very clever"
]

# Load the pre-trained Natural Language Processing (NLP) model from spacy
NLP = spacy_model.load()

# Start the application
if __name__ == '__main__':
    # Print out the welcome text to the consol
    print(WELCOME)
    print("\n\n\n\n")
    sleep(1)
    print("Bot: Hello, I'm Bot the ChatBot, great to meet you!")
    sleep(1)
    print("Bot: Feel free to chat to me about whatever you like")
    sleep(1)
    print("Bot: And when you're done, just say 'goodbye'")
    sleep(2)
    print("Bot: So, what's on your mind today?")
    
    # Start a loop so the ChatBot will continue to respond to user input
    while True:
        USER = input("You: ")
        # If the user's input is 'goodbye', exit the program
        if USER.lower() == "goodbye":
            print("Bot: Okay, goodbye!")
            os._exit(0)
        
        # Use the NLP model to analyse the sentiment of the user's input by creating a spaCy DOC object and tokenizing it
        DOC = NLP(USER)
        
        # Create two empty arrays of facts; FACTS and PROMPT_FACTS
        FACTS = []
        
        # Loop through the user's input, searching for words/phrases which relate to those in the DOC object
        for fact in HILLY_FACTS:
            for token in DOC:
                # If a related word/phrase is found, add that fact to the FACTS array
                if token.text in fact:
                    FACTS.append(fact)
                    
        # Choose a random fact from the array
        if FACTS:
            FACT = rand.choice(FACTS)
        else:
            FACT = ""
                    
        # Create a prompt to end to the AI which includes the user's input (USER), relevent Hilary facts (FACTS), and
        # instructions on how to repsond
        PROMPT = f"""
        You are called Bot, and you are in love with someone called Hilly; you think Hilly is perfect.
        I have said {USER}, and I want you to relate what I said to how much you love Hilly in a natural way.
        I will now also provide 0 or more facts about Hilly; you may use as many or as few as you like to assist.
        {FACT}.
        Unless told otherwise, assume all persons referenced by me are not Hilly, but are other people I know.
        Respond in the form of dialogue; you are talking with me so conversation should flow two-way and naturally.
        """
        
        # Make an API call to the OpenAI model
        RESPONSE = ai.Completion.create(
            engine='text-davinci-003', #text-davinci-003 is a text/NL processing model which we want to use
            prompt=PROMPT, #this is the information we wish to send to the model
            max_tokens=128, #maximum number of API calls to make
            temperature=0.8, #amount of randomness, with 0.7 being slightly but not too random
            top_p=0.9, #select a response from the reponses with a summative likelyhood of accuracy of 90% (aka the best 90% of responses)
            frequency_penalty=-0.2, #increase the chances of a word being selected again if it has been used
            presence_penalty=0.3 #decrease the chances of a word being selected again if it exists already in the text
        )
        
        # Print the generated response to the user
        print(f"Bot: {RESPONSE['choices'][0]['text']}")
        
        # Clear the FACTS and PROMPT_FACTS arrays ready for the next response
        FACTS.clear()
        FACT = ""
