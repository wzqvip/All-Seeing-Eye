import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful career planning assistant.."},
        {"role": "user", "content": "I want to apply for a job, can you offer me some help?"},
        {"role": "assistant", "content": "Sure. Please Describe yourself and the job you are going to acquire. I will give you the chance you will be accepted and the similar jobs."},
        {"role": "user", "content": "I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google."}
    ]
)
# messages=[
#     {"role": "system", "content": "You are a career planning assistant."},
#     {"role": "user", "content": "I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google."}
# ]

print(response['choices'][0]['message']['content'])

with open('response.json', 'w') as f:
    json.dump(response, f)
