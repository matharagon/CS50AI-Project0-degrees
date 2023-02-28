# Movie Degrees of Separation
This is a Python implementation of the Degrees of Separation problem for movies, developed as part of CS50AI's Project0.

# Problem Description
The Degrees of Separation problem involves finding the shortest path between two individuals in a social network, where each path consists of a sequence of connections between individuals. In this implementation, we apply the Degrees of Separation problem to movies, where each individual is a movie actor or actress, and each connection is a shared movie credit between two individuals.

Given a set of movie credits and two actors, the goal is to find the shortest path between the two actors, where each path is a sequence of movies that connect the two actors.

# Solution Strategy
This implementation uses graph theory to represent the movie credits and the connections between actors. The movie credits are represented as nodes in the graph, and the connections between actors are represented as edges between the corresponding movie nodes. We then apply the Breadth-First Search (BFS) algorithm to find the shortest path between the two actors.

The implementation includes the following steps:

Parse the movie credits from a CSV file and create a graph representation of the credits.
Use BFS to find the shortest path between the two actors in the graph.
Output the shortest path as a sequence of movie credits.

# How to Use
To run the movie degrees of separation solver, execute the following command:

```python degrees.py``` 
Follow the instructions by typing the names into the prompt. The solver will then output the shortest path between the two actors as a sequence of movie credits.

# Project Structure
The repository contains the following files:

* `degrees.py`: the main file that runs the solver
* `util.py`: utility functions for parsing the CSV file and creating the graph
* `degrees_of_separation.ipynb`: a Jupyter notebook that contains an analysis of over 1000 actors from IMDB
* `imdb_scraping.py`: a Python script that uses web scraping to gather movie credits data from IMDB
* `README.md`: this file

# Contributing
Contributions to the movie degrees of separation solver are welcome! If you have any suggestions or find any bugs, feel free to open an issue or submit a pull request.
