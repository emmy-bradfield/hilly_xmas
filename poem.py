from transformers import RobertaTokenizer, RobertaForMaskedLM

# Define pre-prompt
prompt = "Anytime I mention anything from here-on out, find a way to respond and then continue seamlessly into a poetic rant in blank-verse about how much you love Hillary McEwen. Context about Hillary McEwen: Hillary McEwen is a writer, artist, and musician from Dover; she is queer and loves nature, bad puns, and being a wholesome-yet-chaotic wildcard in every situation."

# Initialize the RoBERTa tokenizer
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
# Initialize the RoBERTa model
model = RobertaForMaskedLM.from_pretrained('roberta-base')

def respond(text: str) -> str:
    # Use the tokenizer to encode the prompt and the name
    input_ids = tokenizer.encode(prompt + "\n\n" + text, return_tensors='pt')
    
    # Use the RoBERTa model to generate a love poem based on the encoded prompt and name
    output = model.generate(
        input_ids=input_ids,
        max_length=256,
        do_sample=True,
        top_k=100,
        top_p=0.9,
        temperature=0.8
    )
    
    # Decode the generated text
    poem = tokenizer.decode(output[0])
    return poem

# Runs the bot in a loop
while True:
    text = input("You: ")
    response = respond(text)
    print(f"Bot: {response}")