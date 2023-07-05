# All-Seeing-Eye

All Seeing Eye - Unique Hackday Project.

# Project Description

The All-Seeing-Eye is an innovative and comprehensive AI-powered tool designed to assist individuals in navigating their daily lives and achieving their personal goals. The project leverages the power of AI to record, predict, and guide users in various aspects of their lives, from education and career planning to social interactions and personal relationships.

## Features

1. **Recording** : The AI system is capable of recording user activities and interactions in various formats such as text, voice, and video. This data serves as the foundation for the AI's understanding of the user's lifestyle, preferences, and objectives.
2. **Predicting** : Based on the recorded data, the AI system can make predictions about future outcomes and developments. These predictions can assist users in making informed decisions and planning their lives more effectively.

## Applications

1. **Education** : The AI can aid users in improving their learning efficiency. For instance, if a user aspires to become a mathematician, the AI can track their academic progress, predict their performance, and provide suggestions for improvement.
2. **Social Interaction** : The AI can assist users in enhancing their social skills. For instance, if a user has emotional difficulties, the AI can recommend individuals with whom they might have effective communication based on their recorded interactions.
3. **Career Planning** : The AI can help users plan their career paths. For instance, if a user is in a poverty-stricken country and unsure of how to generate income, the AI can provide career advice and planning based on the user's interests and abilities.
4. **Personal Relationships** : The AI can assist users in resolving emotional issues. For instance, if a user has feelings for someone, the AI can predict the likelihood of a successful relationship based on the user's behavior and feedback, and provide suggestions for improvement.

# Implementation

The All Seeing Eye project is a web-based application that includes both front-end and back-end development.

## Front-End UI

The front-end of the web application includes several features:

1. **Recording** : Users can record their current status. This information will be used as input for the AI to build a user profile.
2. **Prediction** : After the user logs in, the AI uses its inferential capabilities to predict the direction and outcome of events.
3. **Goal Setting** : Users can set their desired goals. The AI provides feasible guidance based on the user's current status, the prediction based on the current status, and the user's set goals. It also calculates the probability of the user achieving their goals.

## AI Model

The AI model is based on GPT-3.5 or GPT-4. We will fine-tune the model and build a related database for training to equip the AI with event information in this field. We will also use algorithms and mathematical methods to calculate more accurate event probabilities. Combined with the AI's inferential capabilities, we aim to provide more reliable and meaningful inference results.

## Data Type Conversion

We will use AI-enhanced voice-to-text technology. Users can input voice or video, and after converting to text, we extract emotional features from the voice and video, such as optimism or pessimism. These variables are included in the user profile.

# How To Run

## Front End

```
cd WebUI/vue
```

### Project Setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

## Back End

#### Setup 

1. Set up a Python virtual environment and install the `openai` package:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate  # For Windows
cd openAI-api/framework
pip install -r requirements.txt
</code></div></div></pre>

2. Set your API key as an environment variable:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">export OPENAI_API_KEY="your_api_key_here"  # For Linux and macOS
set OPENAI_API_KEY="your_api_key_here"  # For Windows cmd
$env:OPENAI_API_KEY="your_api_key_here"  # For Windows powershell
</code></div></div></pre>

3. Run the `main.py` script:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">python main.py
</code></div></div></pre>

# Special Note

Due to time limitation, we will mainly focus on career planning, job acquirement.

# Demo

## Front End

### 人生预测器-UI

非常简洁，非常朴素的一个UI，没有华丽的装饰。

用户输入自己的需求之后，按确定键。 后端收到请求之后会判断问题类型，并依据不同的情况进行处理。 

预测的结果会呈现在下面。

*因为时间关系，没有完成前后端的对接。 上面显示的是测试文字， 功能部分请查看后端。*

![1688561653129](image/README/1688561653129.png)

#### 咨询历史记录

![1688561673548](image/README/1688561673548.png)




## Back End

### Calculate the probability of successful job application

*PATH: openAI-api/scripts/CalculateJobProbability.py*

User1:

```
I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google.
```

Reply:

```
Calculated success rate of Google is 60%.

However, if you're looking for alternative options, here are a few that may interest you:

1. Software Engineer at Amazon: Success rate 65%
2. Senior Software Engineer at Microsoft: Success rate 70%
3. Developer at Apple: Success rate 75%
```


User2:

```
I have ten years of driving experience. I want to be a texi driver to earn a live. Will i success?
```

Reply:

```
Based on your description of having ten years of driving experience and applying for a job as a taxi driver, the chances of being accepted are quite high and I estimate a success rate of 85%.

If for any reason you are not accepted as a taxi driver, there are a few other options to consider based on your current skillset:

1. Bus driver: Success rate 80%
2. Truck driver: Success rate 75%
3. Delivery Driver: Success rate 90%
```


### Provide suggestions to better apply for a job

User1:

```
I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google.
```

Reply:

```
Calculated success rate of Google is 30%. The competition for the position is very high and getting accepted for the job at Google is not easy. Since you have only 2 years of experience, it's unlikely to get the Senior Software Engineer position in Google. However, you can still improve your chances and apply for similar positions on other companies such as:

1. Software Engineer at Microsoft
2. Software Engineer at Apple
3. Senior Developer at Amazon

To increase the chances of being hired for this or any other position, here are some suggestions:

1. Tailor your resume and cover letter to match the job description.
2. Showcase your most relevant experiences on your resume that make you an ideal candidate
3. Practice for technical interviews with coding exercises and practice questions
4. Research the company beforehand and prepare questions to ask during the interview.
5. Build a personal project that can reflect your coding ability.
```


User2:

```
I'm an experienced programmer, software developer. I have been worked at Google, Microsoft. I want to apply for a job as senior software developer at Amazon.
```

Reply:

```
The calculated success rate of Amazon is 70%.

Great news! With a 70% chance of success, you have a good chance of landing the job at Amazon. Here are some suggestions to increase your chances of success:

1. Tailor your resume to fit the job description and highlight your relevant experience and achievements.
2. Research Amazon's culture and values and be prepared to demonstrate how your skills align with them.
3. Practice for the interview and be ready to demonstrate your technical skills, problem-solving abilities, and teamwork experience.

Good luck with your application! If you are interested, here are some other job opportunities you may be suited for:

1. Senior Software Developer at Google
2. Senior Software Engineer at Apple
3. Principal Engineer at Microsoft.
```


### *Predict future life trajectory*

User1:

```
I'm a 30-year-old software engineer living in San Francisco. I'm passionate about technology and love to travel. What does my future look like?
```

Reply:

```
As I gaze into the crystal ball, I see that your future is bright and promising. In the next year or so, you will continue to excel in your career as a software engineer. You will work on innovative projects that will gain you recognition and respect in the tech community.

Around the age of 32, you will meet someone special, a kindred spirit with whom you will bond over your shared love of adventure and exploration. You will embark on many travels together, visiting exotic places and experiencing new cultures. Your relationship will flourish, and you will realize that you have found your soulmate.

In your mid thirties, you will receive an exciting opportunity to work abroad. This will be a major turning point in your life, and you will seize the chance to live in a foreign country. You will embrace the new culture and become fluent in a new language.

Around the age of 40, you will have achieved great success in your career and will have amassed a significant amount of wealth. You will use your resources to support philanthropic causes and make a positive impact on the world.

In your fifties and beyond, you will continue to pursue new experiences and adventures. You will remain curious and passionate, always seeking to learn more about the world around you. Your life will be full of love, happiness, success, and fulfillment.
```



User2:

```
I'm a CS graduated student, I have less money. I live in China, I'm longing for freedom in USA.
```

Reply:

```
As I gaze into the crystal ball, the future starts to unravel. I see a path that will lead you to your heart's desires, but it will not be an easy one. 

In the next few years, you will be working hard to get your foot into the tech industry. You will face many challenges and rejections, but you will not give up. You will continue to learn new skills, refine your work, and network with people in the industry. Through your hard work, you will finally find a job in a tech company that will offer you decent pay and a chance to grow. This will give you a solid foundation to build your future on.

Over the next few years, you will continue to work hard and save your money. You will be able to move to the USA, but it will take some time to save up for a big house. You will rent a small place in the meantime until you can afford a home of your own. 

In the next decade, you will meet the love of your life, but it will not be an easy journey. There will be heartbreaks and conflicts along the way, but you will eventually find the woman of your dreams. She will be someone who shares your values, goals, and passions. You will build a beautiful life together and be blessed with children.

As you settle into your married life, you will be able to buy a big house, fulfill your dreams, and enjoy the fruits of your labor. However, life is not without its challenges, but you will face them with grace and determination. You will find happiness, fulfillment, and contentment in your life. Remember to always stay true to yourself and never give up on your dreams.
```
