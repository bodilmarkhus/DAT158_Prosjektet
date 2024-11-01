# DAT158_Prosjekt

## Description of the Project
For the final project work, your task is to make a complete, machine learning-based software product. You are free to choose the project idea, and which ML and web frameworks you want to use to deploy your model. Make sure, however, that you follow the instructions listed below. If need some assistance in defining a good project, come ask us at the lab or send a message on Canvas.

## Goal of the Project
The goal of the project is to create an ML-based software in form of a website, that solves some kind of useful, cool, and/or fun task.

## Two Options
There are two directions you can follow:

1. Create a model from bottom up, following the steps of the ML project lifecycle we have discussed in lectures. This way you will have control of all steps and can tailor your model to be the optimal solution to the task you are trying to solve.
2. Build your project on top of existing ML products, such as the large language model (LLM) that powers ChatGPT. If you want to build a chatbot or an image generation tool, it is far beyond the scope of the course to train this type of model from scratch -- which is also the case for most businesses. In this case we have to build the project around the API of a pre-made model.
Remember that if you go for this approach, you still need to adapt the solution to your use-case (you can't just make a generic ChatGPT clone).
 
## Instructions to Follow
- You should work in groups of 2-3 students.
- You are allowed to use AI coding tools and take inspiration from solutions you find on the Internet, but you need to cite sources you use. Plagiarism is, as always, strictly forbidden.
- You must write a short report documenting your work, following this template: Norwegian, English. It's a good idea to start writing as soon as you have a plan for the project, as this helps you focus. You can upload the template to Google Docs for easier collaborative writing.
- The code you write, the report, and everything related to the project, must be put in a GitHub repository. You project submission here on Canvas will be a link to the repository. The repository has to be readable my me, so in case you want to set it as "private", you need to invite me (smaeland) as a collaborator.
- The final product must be a website that takes in user input, and gives a ML-based result in return. There are two ways to show how the website works: Either
    - Deploy it publicly on the Internet (the preferred option -- some hosting options listed below), or
    - Make a video/screencast of you interacting with it.
- The code and documentation in the GitHub repository must be complete, meaning anyone should be able to reproduce your results and deploy the website.

## How to Submit
Submit a link to the GitHub repository containing the group's work. Everyone must individually submit on Canvas, but within a group you just submit the same link.

## Submission Checklist
The group's GitHub repo contains:
- The report
- All code required to reproduce your results
- Documentation of you final website, either as
    - Link to the live website
    - Video of you showing the features of the website

## How Much Work is Expected?
There is no lower limit on the number of lines of code you are supposed to produce, since a big part of the project is to invent the idea, research the topic, and then plan and design the solution. The report should convey how much effort you spent on this part. You can expect to spend around a week of fulltime work to compete the project.

## Project Ideas
These are just suggestions to get your creativity flowing -- you don't have to choose among these, but they can be a point of inspiration for your own ideas. 

### To Find Interesting Datasets, Look for Instance on ..
- Kaggle ([her](https://www.kaggle.com/datasets))
- UCI ML repository ([her](https://archive.ics.uci.edu/))
- Google Dataset Search ([her](https://datasetsearch.research.google.com/))

### Make a Web App to ..
- Estimate the value of a used car ([her](https://www.kaggle.com/competitions/playground-series-s4e9/))
- Predict wine quality ([her](https://archive.ics.uci.edu/dataset/186/wine+quality))
- Classify mushrooms as poisonous or edible ([her](https://archive.ics.uci.edu/dataset/73/mushroom))

### Create a Chatbot to ..
- Be a student assistant in DAT158 (using for instance OpenAI ([her](https://platform.openai.com/docs/overview)), Gemini API ([her](https://ai.google.dev/gemini-api/docs)), Anthropic API ([her](https://docs.anthropic.com/en/api/getting-started)))
- Write tweets based on your current mood
- Generate pictures of today's weather based on meteorological info (OpenAI image generation API ([her](https://platform.openai.com/docs/guides/images/image-generation)))

### Website hosting
Some suggestions for ways to easily host your website:
- Gradio ([her](https://www.gradio.app/)).
- Streamlit ([her](https://streamlit.io/)).

## Our Own Notes
**Anbefaler alle å lese kap. 1, 2, 3, 4, 6, 7 i lizard boken, da dette er teori som ligger bak maskinlæringsmodellene. Det ligger også notebooks ute som er lurt å gå gjennom selv om man ikke forstår alt med en gang - *den er designet slik!***

### Immediate Thoughts
Bruk en Random Forest Classifier (kap. 7 i lizard boken), med Decision Trees (kap. 6 i lizard boken).
Det er en av de sterkeste modellene som finnes og brukes i mange større maskinlæringsmodeller.

**Side 988 i lizard boken tar for seg "A Machine Learning Problem Checklist" som kan være nyttig å få med seg!** Den ligger etter kap. 19.

#### Oppsummering fra kap. 7:
*"In conclusion, ensemble methods are versatile, powerful, and fairly simple to use. Random forests, AdaBoost, and GBRT are among the first models you should test for most machine learning tasks, and they particularly shine with heterogeneous tabular data. Moreover, as they require very little preprocessing, they’re great for getting a prototype up and running quickly. Lastly, ensemble methods like voting classifiers and stacking classifiers can help push your system’s performance to its limits."*

#### Static training vs. dynamic training av en ML modell:
[from here](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-training) <br />
**Advantages** <br />
*Static training:*	Simpler. You only need to develop and test the model once. <br />
***Dynamic training:*** More adaptable. Your model will keep up with any changes to the relationship between features and labels. <br />
<br />
**Disadvantages** <br />
*Static training:*	Sometimes staler. If the relationship between features and labels changes over time, your model's predictions will degrade. <br />
***Dynamic training:*** More work. You must build, test, and release a new product all the time. <br />
<br />
If your dataset truly isn't changing over time, choose static training because it is cheaper to create and maintain than dynamic training. However, datasets tend to change over time, even those with features that you think are as constant as, say, sea level. The takeaway: even with static training, you must still monitor your input data for change.

## Google Drive
Vi har en google drive til dokumenter, rapportskriving og annet nyttig.
Den finnes [her](https://drive.google.com/drive/folders/1YO_cdITiRyF1ruG6hA6MQTmpEVm-r7tf?usp=drive_link).
