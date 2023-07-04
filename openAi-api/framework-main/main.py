import openai
import lib.jobfinding as jobfinding

KEY ="" 

openai.api_key = KEY

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo", 
#   messages=[{"role": "user", "content": "test"},{"role": "system", "content": "randomly say something!"}],
#   temperature=1.5,
# )

# print(completion)

new_model = jobfinding.JobFindingGPT(KEY,flush=True)
new_model.main()


