# Import the necessary libraries
import spacy
import random
from openai import api_key, get_model
import openai

openai_apikey = "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"

# Define a database of facts about "Hilly"
hilly_facts = [
    "Hilly loves to paint.",
    "Hilly is an excellent knitter.",
    "Hilly is a talented writer.",
    "Hilly has a passion for music.",
    "Hilly is an avid reader.",
]

# Load the pre-trained NLP model
nlp = spacy.load('en_core_web_sm')

# Load the pre-trained NLG model
model = get_model('text-davinci-002')

while True:
    # Prompt the user to enter their message
    user_input = input('Enter your message: ')

    # Use the NLP model to analyze and interpret the user's input
    doc = nlp(user_input)

    # Create an empty list to store the selected facts
    selected_facts = []

    # Loop through the user's input and look for words or phrases related to each fact in the database
    for fact in hilly_facts:
        for token in doc:
            # If a word or phrase related to the fact is found, add the fact to the selected facts list
            if token.text in fact:
                selected_facts.append(fact)

    # If any facts were selected, choose a random fact from the selected facts list
    if selected_facts:
        hilly_fact = random.choice(selected_facts)
    # If no facts were selected, choose a random fact from the entire database
    else:
        hilly_fact = random.choice(hilly_facts)

    # Generate a response to the user's input using the NLG model
    response = model.generate(
        prompt=f'Hilly is a wonderful person! {hilly_fact} What do you think about that?',
        max_tokens=256,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the generated response
    print(response)
