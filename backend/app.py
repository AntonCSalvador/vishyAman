from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import chess
from scripts.generate_graph import generate_graph, jsonify_graph
from scripts.traverse_graph import dfs_eval, bfs_eval
from time import time
import random
from math import ceil

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Configure CORS to allow all origins for all routes

@app.route('/random_fen', methods=["GET"])
def random_fen():
    print("Recieved request for random fen")
    try: 
        with open("./examples/example_fens.txt") as examples:
            example = random.choice([x for x in examples])
        fen = example
        greed = random.random() * 0.9
        print("Processing FEN:", fen, "with greed:", greed)  # Debug output
        result = {
            "fen":fen,
            "greed":greed
        }
        print("Result:", result)  # Debug output
        return jsonify({'result': result})

    except Exception as e:
        print("Error processing request:", str(e))  # Print any errors during processing
        return jsonify({'error': 'Failed to process request'}), 500

@app.route('/process_fen', methods=['POST'])
def process_fen():
    print("Received request")  # Check if the server receives the request
    try:
        data = request.get_json()
        fen = data['fen']
        greed = float(data['greed'])
        print("Processing FEN:", fen, "with greed:", greed)  # Debug output
        result = process_fen_string(fen, greed)
        print("Result:", result)  # Debug output
        return jsonify({'result': result})
    except Exception as e:
        print("Error processing request:", str(e))  # Print any errors during processing
        return jsonify({'error': 'Failed to process request'}), 500

def process_fen_string(fen, greed):
    print("before chess.Board(fen)")
    board = chess.Board(fen)
    print("before generateGraph")
    start_time_generate = time()
    graph = generate_graph(board, 4, greed, display_progress=True)
    generate_duration = ceil(time() - start_time_generate)
    print("before dfs eval and bfs eval")

    # Time DFS evaluation
    start_time_dfs = time()
    dfs_result = dfs_eval(graph)
    dfs_duration = int((time() - start_time_dfs) * 1000)  # Convert to milliseconds

    # Time BFS evaluation
    start_time_bfs = time()
    bfs_result = bfs_eval(graph)
    bfs_duration = int((time() - start_time_bfs) * 1000)  # Convert to milliseconds    print("after dfs eval and bfs eval")

    print("after bfs and dfs")
    # Finding the best moves from the evaluations
    best_dfs_move = max(dfs_result, key=lambda item: item["value"]) if dfs_result else None
    best_bfs_move = max(bfs_result, key=lambda item: item["value"]) if bfs_result else None

    # Construct the response object
    result = {
        "generate_time_s": generate_duration,
        "dfs_best_move": best_dfs_move["move"] if best_dfs_move else "No move found",
        "bfs_best_move": best_bfs_move["move"] if best_bfs_move else "No move found",
        "dfs_fen": best_dfs_move["fen"] if best_dfs_move else "",
        "bfs_fen": best_bfs_move["fen"] if best_bfs_move else "",
        "dfs_time_ms": dfs_duration,  # Time in milliseconds
        "bfs_time_ms": bfs_duration   # Time in milliseconds
    }
    return result

if __name__ == '__main__':
    app.run(debug=True)
