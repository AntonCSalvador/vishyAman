# Vishy Aman: Chess Puzzle Solver Efficiency Analysis

## Problem

**What problem are we trying to solve?**  
The goal is to find the most time-efficient way of solving a chess puzzle, focusing on optimizing both time and space requirements.

## Motivation

**Why is this a problem?**  
Improving at chess is a common goal among enthusiasts. Enhancing the performance of chess bots can aid in this process by enabling these systems to run on lower-end hardware, making practice more accessible.

## Features

**When do we know that we have solved the problem?**  
Success will be measured against the outputs of open-source engines like Stockfish. If our engine, potentially lower in performance (e.g., Lila), matches the output of these established engines, we'll consider it a success. The key metric is the time Lila takes to find a correct solution using the proposed search algorithm.

## Data

**Public data set we will be using and the link to the public data set**  
Our research will utilize data from the publicly available lichess.org database, accessible [here](https://database.lichess.org/). This database includes millions of data points from games and moves, providing a robust dataset for analysis.

## Tools

**Programming Languages or any other tools/frameworks**  
For the frontend development, we will be using the JavaScript framework React, along with basic HTML and CSS. The backend development will be conducted in Python, leveraging the Lichess API for data retrieval and manipulation.

## Strategy

**Preliminary algorithms or data structures you may want to implement.**  
Our approach involves searching lichess game positions for the best move using a Python chess engine. We'll compare the efficacy of depth-first search to breadth-first search in identifying the best move from a randomly selected position within a vast database of chess positions.

## Team Roles

- **UX/UI Lead and Front End Developer:** Anton Salvador
- **Backend Lead:** Caleb Owens
- **Full Stack Developer:** Cameron Daniels

