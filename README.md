# Twitter_Pipeline
Build a Dockerized Data Pipeline that analyzes the sentiment of tweets.

# [Project: Twitter Sentiment Project](https://github.com/spicedacademy/fenugreek-student-code/tree/karen/week_06_project)

* Spiced Academy Project

<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Twitter_workflow.png" width="350" height="250"  class="center"> 

* Used Python, MongoDB, Tweeter APIs, tweepy, Docker.
* Built a data pipeline with Docker-compose that collected tweets and stored them in a MongoDB database. 
* Created an ETL job that pulled the tweets from MongoDB, cleans data and calculates compound sentiment score (Vader Sentiment Analysis) for sentiment analysis and then stored the analysed tweets on a second database (PostgreSQL).

<img src="https://github.com/kbolon1/Portfolio/blob/main/images/Twitter_Sentiment_George_Takei.png" width="500" height="300"> 

*How to Run?

- Create Tweeter API and add to config.py file
- Run command 'Docker build' from main dir (where docker-compose file is) to build the image for the first time.
- Run command 'Docker-compose up' to start all containers in yml file.