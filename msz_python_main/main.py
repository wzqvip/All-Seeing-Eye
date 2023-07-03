import openai

openai.api_key = "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" 

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "test"}]
)

print(completion)