# YouTube Data Analysis App with MONGODB, and Streamlit

## Purpose

Build a Streamlit app for analyzing data from YouTube channels, storing it in MongoDB, and enabling SQL-based data warehousing and analysis.

## Tech Stack

- Python
- MySQL
- MongoDB
- Google API Client
- Streamlit

## Imports
=>Requirement Libraries to Install
      pip install google-api-python-client, pymongo, mysql-connector-python,mysql, pandas, plotly-express, streamlit.

=>Import Libraries

##Youtube API libraries
  from googleapiclient.discovery import build
  import json

##MongoDB
  import pymongo

##SQL libraries
  import mysql.connector as sql
  from mysql.connector  import Error
  from datetime import datetime

##pandas
import pandas as pd

##Dashboard libraries
  import streamlit as st
  from streamlit_option_menu import option_menu
  import plotly.express as px

## Steps

1.Streamlit App Setup: Created a Streamlit app for user-friendly data access.

2.YouTube API Integration: Connected to YouTube API V3 using the Google API client library to fetch channel and video datas.

3.MongoDB Data Lake: Storing the data in MongoDB collections for structured organization of collections: channels, videos, and comments.
                     We here use Mongodb because it can handle both structured and unstructured datas efficiently.

4.SQL Data Warehouse: Transfering datas from MongoDB to SQL (e.g., MySQL or PosgreSQL). Design SQL schema with proper keys(datatypes).

5.SQL Data Analysis: Utilizing SQL queries to join tables, enabling advanced data analysis as per requirements.

6.Streamlit Data Visualization: Displaying data using Streamlit, including charts and graphs for better insights.

This approach provides an efficient way to collect, store, and analyze YouTube channel data within a user-friendly app.