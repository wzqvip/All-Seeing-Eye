import openai

openai.api_key = 'your-api-key'

response = openai.Completion.create(
  engine="text-davinci-003.5",  # or "text-davinci-004" for GPT-4
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message']['content'])
