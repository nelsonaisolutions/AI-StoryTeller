# Generate a story using GPT-2 with the prompt "Once upon a time"
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompt = "Once upon a time"
output = generator(prompt, max_length=100)
story_text = output[0]["generated_text"]
print(story_text)
