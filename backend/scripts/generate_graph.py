import sys

sys.path.append("../evaluation")

from homemade import sunfishEval
import chess
import json
from math import ceil

def generate_graph(board: chess.Board, depth: int, greed=0.0, display_progress=False):
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
                    print(f"Evaluated {count} positions")

    return graph

def print_move(move):
    print(move["move"], move["response"], move["value"], end=" ")

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
    board = chess.Board()
    # board = chess.Board("8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8 w - - 99 50")
    graph = generate_graph(board, 4, 0.5, display_progress=True)
    print(f"Positions: {len(graph)}")
    jsonify_graph(graph, "../data/graph.json")
    # print_graph(graph)
