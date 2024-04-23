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
    git clone git@github.com:AntonCSalvador/vishyAman.git
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

## Troubleshooting

If you encounter issues while setting up or running Vishy Aman, here are a few common problems and their solutions:

- **Dependency Installations:** Ensure that you have correctly installed all the dependencies. Refer back to the step where you run `pip install -r requirements.txt` in the backend directory. If you encounter any errors during installation, make sure Python and pip are correctly installed and up to date on your system.

- **Correct Fetch URL in `board.js`:** When the frontend attempts to communicate with the backend, it uses a fetch request in `board.js`. Ensure that this fetch request points to the correct URL where `app.py` is running. Typically, this will be something like `http://127.0.0.1:5000/process_fen`. If you've configured the Flask app to run on a different port or host, you'll need to update this URL accordingly but MAKE SURE YOU ADD THE `/process_fen`.

- **Browser Compatibility:** If you're experiencing issues with how the website looks or behaves, make sure you're using a compatible web browser. We recommend using the latest version of Firefox, Chrome, or Safari. If you're using a different or outdated browser, some features might not function as expected.

By following these troubleshooting steps, most common issues with running the Vishy Aman Chess Puzzle Solver should be resolved. If problems persist, consider checking console logs in your web browser for any error messages that could provide more insight into the issue.
