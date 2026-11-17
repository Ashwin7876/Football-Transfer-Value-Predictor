# Football-Transfer-Value-Predictor
## About the Project

I built this project to explore machine learning and how it can be used in football.
The goal is to predict a football player's estimated market value based on their age, goals, assists, playing time, and position.
I wanted to combine two things I'm interested in: football and coding.

## How It Works

I collected football player data and cleaned it using Python.
I used Pandas to organise the data.
I trained a Linear Regression model using Scikit-learn.
I used OneHotEncoder to help the model understand different player positions.
I built a website using Streamlit where users can enter player stats and get a predicted market value.

## Technologies I Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Model Performance

I tested my model using data it hadn't trained on.
Model: Linear Regression
Training data: 80%
Testing data: 20%
Mean Absolute Error: Around €11.96 million
This means the model's predictions were off by about €11.96 million on average during testing. It's not perfect, but it's a starting point I can improve.

## How to Run It

Clone this repository.
Install the required libraries:
pip install -r requirements.txt
Run the app:
streamlit run app.py

## My Development Experience

I used AI tools throughout the development of this project to help me understand concepts, work through errors, and learn how different parts of the code fit together.

I'm still developing my programming skills, so AI played a big role in helping me build this project. However, I made an effort to understand the code, learn from the process, and figure out how the machine learning model works. I mainly made this because I'm interested in both football and programming, so I wanted to build something that combines them. This project has helped me learn more about Python, machine learning, data cleaning, and how models are trained.

## Dataset Credits

The football player dataset used in this project was created by Lluis Manso Matachana and Marc Costa Quer.
Source: [Zenodo – Dataset](https://zenodo.org/records/19396819)
The dataset is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
I used this dataset for educational and personal learning purposes and made changes to prepare it for machine learning.

## Additional Data Source
The players.csv file was collected using the football-data.org API.
It contains Premier League team and squad information, including player names, positions, dates of birth, nationalities, and shirt numbers.
Attribution: Data provided by football-data.org.
This data was collected for educational and personal project purposes.
