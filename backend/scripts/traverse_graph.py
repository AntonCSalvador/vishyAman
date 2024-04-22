from generate_graph import generate_graph, print_graph, print_move
import json

def bfs_eval(input_graph):
    graph = input_graph.copy()
    pass


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


def greedy_search(input_graph):
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
    
    return moves[0]

if __name__ == "__main__":
    with open("../data/graph.json") as file:
        graph = json.load(file)

    move = greedy_search(graph)
    print("Greedy search result:")
    print_move(move)
    print()

    print("DFS eval results:")
    eval = dfs_eval(graph)
    for move in eval:
        print_move(move)
    print()
    
    print("Best DFS move:")
    print_move(max(eval, key=lambda item: item["value"]))
