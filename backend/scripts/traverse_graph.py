from generate_graph import generate_graph, print_graph, print_move
import time
import json

def bfs_search(graph, greed=0.0):
    pass


def dfs_search(graph):
    pass
    

def greedy_search(graph):
    moves = []
    depth = graph[-1]["depth"]

    root = graph[0]
    for i in range(depth):
        maxValueMove = root["next"][0]
        for child in root["next"]:
            if child["value"] > maxValueMove["value"]:
                maxValueMove = child
        
        moves.append(maxValueMove)
        root = maxValueMove
    
    return moves

if __name__ == "__main__":
    with open("../data/graph.json") as file:
        graph = json.load(file)

    greedy = greedy_search(graph)
    for move in greedy:
        print_move(move)
        print()
