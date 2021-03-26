# Degrees
---
## Overview
Write a program that determines how many “degrees of separation” apart two actors are.

## Background
According to the <a href="https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon">Six Degrees of Kevin Bacon</a> game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

In this problem, we’re interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”

We can frame this as a search problem: our states are people. Our actions are movies, which take us from one actor to another (it’s true that a movie could take us to multiple different actors, but that’s okay for this problem). Our initial state and goal state are defined by the two people we’re trying to connect. By using breadth-first search, we can find the shortest path from one actor to another.

#### Supported use-cases
* The system must be able to return the shortest path between two actors if their names are found in the database.


#### Out of Scope 
* The system should not be able to return the shortest path between two actors if their names are not found in the database.


### Diagram
![alt-text](https://github.com/LeoZorzoli/CS50-AI-2021/blob/main/degrees/diagram.png)

### Json model
```json
    {
        "people.csv": {
            "id": 102,
            "name": "Kevin Bacon",
            "birth": 1958
        },
        "movies.csv": {
            "id": 112384,
            "title": "Apollo 13",
            "year": 1995
        },
        "stars.csv": {
            "person_id": 102,
            "movie_id": 104257
        },
    }
```


