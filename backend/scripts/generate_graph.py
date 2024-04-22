import sys

sys.path.append("../evaluation")

from homemade import sunfishEval
import chess
import json
from math import ceil
from time import time

def generate_graph(board: chess.Board, depth: int, greed=0.0, display_progress=False):
    start_time = int(time())
    count = 0

    graph = [{"move":None,"response":None,"value":None,"fen":board.fen(),"depth":0,"next":[]}]

    for i in range(depth):
        shallowest = []
        for item in graph:
            if item["depth"] == i:
                shallowest.append(item)
        
        shallowest.sort(key=lambda item: item["value"], reverse=True)
        numPositionsToKeep = ceil((1.0 - greed) * len(shallowest))
        
        for item in shallowest[:numPositionsToKeep]:
            currBoard = chess.Board(item["fen"])
            evals = sunfishEval(currBoard, depth=item["depth"] + 1)
            for eval in evals:
                item["next"].append(eval)
                graph.append(eval)           

                if display_progress:
                    count += 1
                    if count % 100 == 0:
                        print(f"Evaluated {count} positions")
            
    if display_progress:
        print(f"Done! Evaluated {count} positions in {int(time()) - start_time} seconds")

    return graph

def print_move(move, end="\n"):
    print(move["move"], move["response"], move["value"], end=" ")
    print(end, end="")

def print_graph(graph):
    for item in graph:
        print_move(item)
        for child in item["next"]:
            print("=>", end=" ")
            print_move(child)
        print("=> None")

def jsonify_graph(graph, filename):
    with open(filename, "w") as f:
        json.dump(graph, f, indent=2)
    
if __name__ == "__main__":
    fen = "5rk1/P3P3/PPPP1pKp/3pp2P/4pP1P/pppp1P1p/2p5/1K1R1RK1 w - -"
    board = chess.Board(fen)
    graph = generate_graph(board, 4, 0.0, display_progress=True)
    jsonify_graph(graph, "../data/graph.json")
    # print_graph(graph)
