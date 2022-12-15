# Install dependencies using pip
!pip install spacy
!python -m spacy download en_core_web_sm

# Use the spaCy model to analyze and interpret user input
import spacy
nlp = spacy.load('en_core_web_sm')

# Pass the user's input to the nlp object, which will then generate a spaCy Doc object containing the processed text and its associated linguistic annotations. 
user_input = input('Enter your message: ')
doc = nlp(user_input)

# Use the Doc object to extract relevant information about the user's input
# Print the raw text of the user's message
print(doc.text)

# Print any named entities mentioned in the user's message
for ent in doc.ents:
    print(ent.text, ent.label_)

# Create a dictionary of responses, where the keys are the types of user input
# and the values are the responses that the chatbot should use
responses = {
    'greeting': ['Hi there!', 'Hello!', 'Hey there!'],
    'question': ['I'm sorry, I can't answer that.', 'I'm not sure.'],
    'default': ['Sorry, I didn't understand what you said.']
}

# Generate a response to the user's input by looking for named entities in the
# spaCy Doc object and selecting the appropriate response from the database
response = None
for ent in doc.ents:
    # If the user's input contains a named entity, use a specific response
    if ent.label_ == 'PERSON' and ent.text.lower() == 'hilly':
        response = 'Hilly is a wonderful person!'
    elif ent.label_ == 'ORGANIZATION':
        response = 'I don't know much about that organization.'

# If no named entities were found, use a generic response
if response is None:
    response = random.choice(responses['default'])

# Print the selected response
print(response)
