from shlex import split
from scripts.generate_graph import generate_graph, print_move
from scripts.traverse_graph import dfs_eval, bfs_eval
import chess
import random
from time import time

def cli():
    board = chess.Board()
    graph = None

    print()
    print("Enter a command, or type 'help' for help.")
    print()
    command = ""
    while command != "quit":
        command = split(input(">> "))
        print()

        match command[0]:
            case "quit":
                return

            case "help":
                print("Commands:")
                print("'quit' - Exits the program")
                print("'help' - Displays this help screen")
                print("'view' - Displays the current board")
                print("'enter <FEN>' - Loads a new board based on an inputted FEN string")
                print("'random' - Picks a random FEN value")
                print("'generate <DEPTH> <GREED>' - Generates a graph and provides diagnostics")
                print("    (a maximum depth of 4 is recommended, greed must be between 0.0 and 0.9)")

            case "view":
                print("FEN:", board.fen())
                print(board)

            case "enter":
                fen = " ".join(command[1:])
                board = chess.Board(fen)

            case "random":
                with open("./examples/example_fens.txt") as examples:
                    example = random.choice([x for x in examples])
                fen = example
                board = chess.Board(fen)
                print("New FEN:", fen, end="")

            case "generate":
                if float(command[2]) < 0 or float(command[2]) > 0.9:
                    print("Invalid greed coefficient")
                    continue
                
                if int(command[1]) < 0:
                    print("Invalid depth")
                    continue
                    
                if int(command[1]) > 4:
                    print("You've chosen a depth greather than 4, this might take a while.")
                    selection = input("Are you sure you want to continue? [y/N] >> ")
                    if not selection == "y" and not selection == "Y":
                        continue

                selection = input("Would you like to view the graph generator's progress? [y/N] >> ")
                if selection == "y" or selection == "Y":
                    display_progress = True
                else:
                    display_progress = False

                graph = generate_graph(board, int(command[1]), float(command[2]), display_progress)

                print()
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

            case _:
                print("Invalid command! Type 'help' for help.")
            
        print()
    

if __name__ == "__main__":
    cli()