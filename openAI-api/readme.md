# The implemented functions of this API:

## Your input structure

* you have 5 parameters:
* query type(success rate predicting?suggestions in finding dream job?Future predicting?)

* is your input a pure text or mp3?
* your text input content if your input is pure text

* your mp3 input if your input is voice
* do you need an generated image feedback?


## Different Query Types


### Calculate the probability of successful job application

You input your dream job and your conditions and chatbot will compute the success rate for you based on the *pre-training data*.

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

You are not confident in getting this job and you can ask chatbot how can you improve yourself. Trained on some *professional suggestions*, chatbot will give you the best suggestions.

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

### Predict future life trajectory

You are unsure about your future and you want to look into it. Chatbot will simulate your life direction and will do some *cyber divination* for you!

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


## Voice input

When the second parameter is mp3 and you have a valid voice mp3 input, you can input a .mp3 file and get the output. The AI assistant is hearing your question.

### Example:

Your input is a mp3 file that sounds like this:

```
I want to be a Google frontend Engineer
```

And you want to predict your application success rate. By choosing to predict the success rate you get the answer below:

```
The success rate is below 20% if you don't mention your extra information. You should tell me your skills and knowledges first...
```

## Image generating

if you choose to generate the image, the chatbot will generate an image based on its answer.

If you want to get a job as a cashier and you choose to predict, you input this:

```
I want to be a cashier and I am good at computing. I am also delegent.
```

You may get answer like this:

```
The success rate is above 90%, congratulations! Computing skill is important when you are a cashier...
```

And you may receive a picture like this:

![1688743966702](image/WhatIdid/1688743966702.png)
