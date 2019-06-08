#!/usr/local/bin/python

# importing requests for API invocation
import requests

# importing json for converting response bytes to dictionary
import json

# importing argparse for reading commandline parameters
import argparse

# setting command line arguments
parser = argparse.ArgumentParser(description='Command Line Parameters')
parser.add_argument('-m', '--movie',help="Pass movie name",type=str)
opts = parser.parse_args()

# setting default Movie value empty
movie = ""
if opts.movie :
    # getting movie value from command line options
    movie = opts.movie
else:
    # aborting script if user doesn't pass movie parameter
    print("Please pass -movie <value>")
    exit(1)
# appending movie vaule to apiURL
apiURL="http://www.omdbapi.com/?i=tt3896198&apikey=b9565191&t="+movie
try:
    # invoking api
    response=requests.get(apiURL)
    # parsing response content to dictionary
    parsed = json.loads(response.content)
    # iterating Ratings sources from the reponse
    if "Ratings" in parsed:
        available=False
        for source in parsed['Ratings']:
            # printing movie rating value when source is 'Rotten Tomatoes'
            if source['Source'] == "Rotten Tomatoes":
                print("Rotten Tomatoes Rating for ",movie,"Movie Rating is:",source['Value'])
                available=True
                break
        if available == False:
                print("Rotten Tomatoes Rating for ",movie,"is not available")
except Exception as e:
    print(e)
