# cassandra-data-modeling

## Introduction
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions. For this project, I created a database for this analysis. 

## Data
The dataset is stored in `event_data` directory. The directory contains CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
> event_data/2018-11-08-events.csv
> event_data/2018-11-09-events.csv

I transfered the  data from a set of CSV files within the `event_data` directory to create a streamlined CSV file `new_events_data.csv` to model and insert data into Apache Cassandra tables.

## Files
* `event_data` directory contains the dataset from sparkify
* `new_events_data.csv` Streamlined CSV file with all the data from the events data directory
* `process_data.py` extracts and transforms the data to streamline the etl pipeline creation
* `cassandra_etl.ipynb` data pipeline to create and load data into cassandra tables
