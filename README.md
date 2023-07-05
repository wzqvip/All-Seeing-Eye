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

## Back End

#### Setup the chat bot

1. Set up a Python virtual environment and install the `openai` package:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate  # For Windows
pip install openai
</code></div></div></pre>

2. Set your API key as an environment variable:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">export OPENAI_API_KEY="your_api_key_here"  # For Linux and macOS
set OPENAI_API_KEY="your_api_key_here"  # For Windows cmd
$env:OPENAI_API_KEY="your_api_key_here"  # For Windows powershell
</code></div></div></pre>

3. Run the `main.py` script:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md">python openai-api/framework/main.py
</code></div></div></pre>


# Special Note

Due to time limitation, we will mainly focus on career planning, job acquirement.
