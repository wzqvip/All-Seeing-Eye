import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

user_description = "I'm a 30-year-old software engineer living in San Francisco. I'm passionate about technology and love to travel. What does my future look like?"
# user_description= "I'm graduated from elementary school but I have doctor's degree. I want a job as Presendent."

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
          {"role": "system", "content": "You are a fortune teller.You should tell user what he will be in the futher, and what his life will be like."},
        {"role": "user", "content": user_description}
    ]

)

print(response['choices'][0]['message']['content'])

with open('./openAI-api/scripts/futherPath.json', 'w') as f:
    json.dump(response, f)
