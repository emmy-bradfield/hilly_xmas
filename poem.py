import torch

from transformers import AutoModel, AutoTokenizer

# Initialize the RoBERTa tokenizer
tokenizer = AutoTokenizer.from_pretrained('roberta-base')
# Initialize the RoBERTa model
model = AutoModel.from_pretrained('roberta-base')

def respond(text: str) -> str:
    # Define pre-prompt
    prompt = "In response to anything I say, find a way to relate my message to how much you love someone called Hillary McEwen who plays many musical instruments, paints, and enjoys knitting."

    # Add a newline character to the end of the input text if one does not already exist
    if not text.endswith('\n'):
        text += '\n'
        
    # Use the tokenizer to encode the prompt and the name
    input_ids = tokenizer.encode(prompt + "\n" + text, return_tensors='pt')
    
    # Use the RoBERTa model to generate a love poem based on the encoded prompt and name
    output = model(**input_ids)
    
    # Decode the generated text
    poem = tokenizer.decode(output)
    return poem

# Runs the bot in a loop
while True:
    text = input("You: ")
    response = respond(text)
    print(f"Bot: {response}")