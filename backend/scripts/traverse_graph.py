from generate_graph import generate_graph, print_graph, print_move
import json
from queue import Queue

# def bfs_eval(input_graph):
#     graph = input_graph.copy()
#     if not graph:
#         return []

#     # Initialize a queue for BFS
#     queue = Queue(graph)

#     # Process the graph in BFS manner
#     while queue:
#         current_node = queue.get()

#         # Check if current node has children
#         if current_node["next"]:
#             # If so, update its value based on the maximum value of its children
#             current_node["value"] = max(child["value"] for child in current_node["next"])

#             # Enqueue all children for further processing
#             for child in current_node["next"]:
#                 queue.append(child)

#     # Return the updated root node value
#     return graph[0]["next"]


def dfs_eval(input_graph):
    graph = input_graph.copy()
    depth = graph[-1]["depth"]

    def dfs_util(item):
        if not item["next"]:
            return item["value"]
        
        if item["depth"] == depth:
            return item["value"]
        
        item["value"] += max([dfs_util(x) for x in item["next"]])
        return item["value"]
    
    for item in graph[0]["next"]:
        dfs_util(item)
    
    return graph[0]["next"]


def bfs_eval(input_graph):
    graph = input_graph.copy()
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
    
    for i in range(len(moves) - 2, -1, -1):
        moves[i]["value"] += moves[i + 1]["value"]
    
    return moves


if __name__ == "__main__":
    with open("../data/ex1.json") as file:
        graph = json.load(file)

    print("DFS eval results:")
    eval = dfs_eval(graph)
    for move in eval:
        print_move(move)
    print()
    
    print("Best DFS move:")
    print_move(max(eval, key=lambda item: item["value"]))
    print()

    print("BFS eval results:")
    eval = bfs_eval(graph)
    for move in eval:
        print_move(move)
    print()
    
    print("Best BFS move:")
    print_move(max(eval, key=lambda item: item["value"]))
    print()
