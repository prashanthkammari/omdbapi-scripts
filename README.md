# OMDB-API-Invocation-Scripts
I have implemented a python script which invokes omdb-api for getting Rotten Tomatoes Rating for a given movie and Dockerized this python script.

## Python Script
This script requires a movie name as a command line parameter to display the Rotten Tomatoes Rating.

## Dockerfile
Docker file is for dockerizing the above python script. We can reuse docker image once we build it.
## Commands
```bash

# Clone git repository
$ git clone https://github.com/prashanthkammari/omdbapi-scripts.git

# Change the directory to the omdbapi-scripts repo
$ cd omdbapi-scripts

# Building docker image
$ docker build -t omdbapi . 

# Running the docker container by passing MOVIE environment variable
# Note: You can pass any movie name in 'single'/"double" quotes
$ docker run -it -e MOVIE='avengers' omdbapi


# Sample Output looks like below 
  Rotten Tomatoes Rating for  avengers Movie Rating is: 92%

```
