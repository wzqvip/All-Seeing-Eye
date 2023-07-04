import openai
from chatgpt import *
import copy
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo", 
#   messages=[{"role": "user", "content": "test"},{"role": "system", "content": "randomly say something!"}],
#   temperature=1.5,
# )
trivial_prompt = ""

skillMatchDict={
    "model":"gpt-3.5-turbo",
    "messages":[{"role": "system", "content": "You are a HR and you need to preview whether the applicant's skills are useful for the job. Nonsense or too much garbage informations will make you feel bad. You need to give a score between 0 and 1 to the applicant's skills. Output as such format:{'score':0.xx, 'reply': (Your reply as a HR)}"}],
    "temperature":0.1,
}


class JobFindingGPT:
    def __init__(self, API_KEY, flush=False,frequency_penalty=1.0,presence_penalty=1.0):
        openai.api_key = API_KEY

        self.flush = flush
        self.frequency_penalty=frequency_penalty
        self.presence_penalty=presence_penalty
        self.previous_questions=[] # 4 questions
        self.goals = {} # goal is a dictionary of {goal prompt:finish percent}
        self.job_description = ""

    def main(self):
        print("What job are you looking for?");
        job_description = input();
        self.job_description = job_description
        print("List your skills");
        skill_string = input();
        m_skill_dict = copy.deepcopy(skillMatchDict)
        m_skill_dict["messages"].append({"role": "user", "content": skill_string})
        skill_ret = self.send_prompt(m_skill_dict)


    def send_prompt(self,messageDict):
        streaming = False
        if(self.flush):
            streaming = True
        completion = openai.ChatCompletion.create(
            model=messageDict["model"],
            messages=messageDict["messages"],
            temperature=messageDict["temperature"],
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            stream=streaming,
        )
        if(self.flush):
            collected_messages = []
            # iterate through the stream of events
            for chunk in completion:
                try:
                    chunk_message = chunk['choices'][0]['delta']['content']
                    collected_messages.append(chunk_message)  # save the message
                    print(chunk_message,end="")  # print the delay and text
                except:
                    pass
        else:
            collected_messages = completion.choices[0].text
            print(collected_messages)
        return collected_messages
        

    def get_job(self, job_description):
        pass

    def compare_resume(self, user_resume, generated_resume):
        pass

    def simulate_interview(self, user_answer, correct_answer):
        pass

    def calculate_success_rate(self):
        pass

    def start_simulation(self, job_description, user_resume, user_answer, correct_answer):
        pass
