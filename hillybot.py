# Import the necessary libraries
import spacy
import os
import random
import openai

# Setup openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a database of facts about "Hilly"
hilly_facts = [
    "Hilly loves to paint",
    "Hilly is an excellent knitter",
    "Hilly is a talented writer",
    "Hilly has a passion for music",
    "Hilly is an avid reader",
    "Hilly lives in Dover",
    "",
    "",
    "Hilly speaks many languages"
]

# Load the pre-trained NLP model
nlp = spacy.load('en_core_web_sm')

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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'You think Hilly is a wonderful person and you are in love with her! {hilly_fact}. I have said {user_input} and I want you to find a way to relate that to Hilly and your love of her',
        max_tokens=128,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=-0.2,
        presence_penalty=0.3
    )

    # Print the generated response
    print(response['choices'][0]['text'])
