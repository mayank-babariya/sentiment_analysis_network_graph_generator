
# Sentiment Analyser & Network graph generator (TwitterSphere)
The application was designed to analyze sentiment by collecting real-time tweets from Twitter and generating a network graph to visualize which other tags are being used alongside a specified tag.

-Sentiment Analyzer

-To analyze tweet sentiments, we trained a CNN model with 1.6 million tweets from a Kaggle dataset. Due to Twitter's recent restriction on tweet collection to around 2400 tweets per day, gathering a large dataset directly from Twitter has become challenging.
-We achieved 83% accuracy after training for 2 epochs. Training was halted at this point because each epoch took nearly 2 hours, and we lacked sufficient computing resources to continue. Attempts to train the model using Google Colab were unsuccessful as the process consumed excessive resources, exceeding the limits of the free version.


-Network Graph Generator

-For the network graph, when a user enters a tag and requests a graph, we collect the latest tweets containing that tag and extract other tags used in conjunction with it. We then generate a network graph based on these collected tags using the NetworkX library.
    



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
