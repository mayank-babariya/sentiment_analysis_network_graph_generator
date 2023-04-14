
# Sentiment Analyser & Network graph generator
The application was developed to analyse sentiemnt by collecting real time tweet from twitter and generate network graph to visualize what individuals using other tags with specific tag given.


- Sentiment Analyser
    - For the analysis of the sentiment of tweet, we have trained CNN model with 1.6 millions tweets collected from twiiter and provided into Kaggle dataset, because twitter just reduced tweet collection to around 2400 tweets per day. So, it is difficult to collect large amount of dataset.
    - We achieve 83% accuracy after 2 epochs, then we stopped the training because one epoch almost took 2 hours to train and we don't habe enough computing power resources to train further. And, we also traid to train model into Google Colab but it also crashed because it is using lot of resources and in free version of Google Colab we are limited to use resources.

- Network grpah generator
    - For the network graph, when user enter tag and hit generate graph, we start collecting latest tweets related to that tag and extract other tags people are using with that tag. Based on that collected tags we generate network graph using networkx library.
    



## Architecture

This application is developed using MVC Architecture. Because it is easier to debug and test applicaiton.

Below is the structure of current applicaiton.
```bash
   app.py (Main file which start server)
    com--
        controller--
            Responsible for controlling requests and response.
        dao Database Access Object(Model)--
            Responsible for viewing data from database.
        vo (View Object)--
            Create database tables.

    static--
        Stores css, js and other user related files.
        Model - ML trained model to predict sentiment of new tweets.
        
    templates--
        Stores all html files.
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`EMAIL_USER=`

`EMAIL_PASSWORD=`

`CONSUMER_KEY=`

`CONSUMER_SECRET=`

`ACCESS_KEY=`

`ACCESS_SECRET=`
## Deployment

The website is hosted on an Amazon EC2 Ubuntu instance, which means that the database used for this application (PostgreSQL) is also located on that same Ubuntu instance. In addition, the application uses an ORM (Object-Relational Mapping) based on SQLAlchemy.

## Requirements

To run this project first need to install all required packages mentioned in Requirements.txt by running following command.

```bash
    pip install -r requirements.txt
```
## Create database

Before running whole project, need to create database in PostgreSQL. 

```bash
    CREATE database sentiment_analysis;
```

## Septs to run
Go to root directory, there is app.py file. Run that file it will start whole project.
```bash
    python3.7 app.py
```

## Machine learning steps

The outlined procedures can be viewed in Google Colab and are accessible via the hyperlink provided below.

- [@Link to Google Colab](https://colab.research.google.com/drive/1CWqdZ5ufv3fdDQbIeUX1jKpbiRRvbrrr?authuser=1#scrollTo=rFL-_mkI8vXN)
## Documentation

[Documentation](https://github.com/mayank-babariya/sentiment_analysis_network_graph_generator)


## Authors

- [@mayank-babariya](https://www.github.com/mayank-babariya)
- [@vansh-shah](https://www.github.com/Vanshshah23)
