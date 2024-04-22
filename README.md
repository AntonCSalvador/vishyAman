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

## Running Vishy Aman

This project consists of both frontend and backend components for analyzing chess positions and suggesting optimal moves using Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms and comparing the times.

### Prerequisites
- Python 3.x
- Flask
- Chess (Python chess library)
- Firefox (or any web browser)

### Instructions

1. **Clone the Repository:**
    ```
    git clone <repository-url>
    ```

2. **Navigate to the Backend Directory:**
    ```
    cd backend
    ```

2. **Pip install all dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the Flask Application:**
    ```
    python3 app.py
    ```

4. **Navigate to the Frontend Directory:**
    ```
    cd ../frontend
    ```

5. **Open `index.html` in Your Web Browser:**
    - Double-click on `index.html` to open it in your default web browser.
    - Alternatively, open `index.html` using Firefox by running:
        ```
        firefox index.html
        ```

6. **Input a FEN String:**
    - In the input field provided, enter a valid FEN string representing a chess position. For example:
        ```
        rnbqkb1r/p1pp1ppp/1p5n/4p3/4P3/7N/PPPP1PPP/RNBQKB1R w KQkq - 0 4
        ```

7. **Submit and Wait for Analysis:**
    - Click on the submit button to initiate the analysis.
    - Wait for the backend to process the FEN string and provide the optimal moves.

8. **Boom!**
    - Once the analysis is complete, the frontend will display the best moves suggested by DFS and BFS algorithms.
    - You will also see the time taken for each algorithm to compute the results.
