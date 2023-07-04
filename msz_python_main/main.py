import openai

openai.api_key = "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" 

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "test"},{"role": "system", "content": "randomly say something!"}],
  temperature=1.5,
)

print(completion)
