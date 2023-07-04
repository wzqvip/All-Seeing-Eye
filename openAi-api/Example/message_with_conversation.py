import openai

openai.api_key = ''

response = openai.Completion.create(
  engine="text-davinci-003.5",  # or "text-davinci-004" for GPT-4
  # messages=[
  #       {"role": "system", "content": "You are a helpful assistant."},
  #       {"role": "user", "content": "Who won the world series in 2020?"},
  #       {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
  #       {"role": "user", "content": "Where was it played?"}
  #   ]
  messages=[
        {"role": "system", "content": "You are a career planning assistant."},
        {"role": "user", "content": "I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google."},
    ]
)

print(response['choices'][0]['message']['content'])
