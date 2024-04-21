with open("../data/lichess_db_standard_rated_2013-01.pgn", "r") as f:
    with open("lichess_db.pgn", "w") as output:
        lines = f.readlines()
        for line in lines:
            if not line.startswith("[") and not line == "\n":
                tokens = line.split(" ")
                for token in tokens:
                    if not token[0].isdigit():
                        output.write(token + " ")
                output.write("\n")
