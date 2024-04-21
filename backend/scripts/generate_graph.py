import sys

sys.path.append("../lichess-bot")

from homemade import sunfishEval
import chess

def generate_graph(board: chess.Board, depth: int):
    graph = [{"move":None,"value":None,"fen":board.fen(),"depth":0,"next":[]}]

    for i in range(0, depth):
        shallowest = []
        for item in graph:
            if item["depth"] == i:
                shallowest.append(item)
        
        for item in shallowest:
            currBoard = chess.Board(item["fen"])
            evals = sunfishEval(currBoard, depth=item["depth"] + 1)
            for eval in evals:
                item["next"].append(id(eval))
                graph.append(eval)           

    return graph

def print_graph(graph):
    for item in graph:
        print(id(item), end=" ")
        for n in item["next"]:
            print("=>", n, end=" ")
        print("=> None")
    
if __name__ == "__main__":
    board = chess.Board()
    graph = generate_graph(board, 4)
    print(f"Positions: {len(graph)}")
    print_graph(graph)