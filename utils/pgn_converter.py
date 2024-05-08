def create_pgn(moves_text, output_file, result="*"):
    moves = moves_text.split()
    pgn_moves = []
    move_number = 1

    for i in range(len(moves)):
        if i % 2 == 0:  
            pgn_moves.append(f"{move_number}. {moves[i]}")
        else:           
            pgn_moves[-1] += f" {moves[i]}"
            move_number += 1
        

    pgn_header = """[Event "*"]
[Site "*"]
[Date "2024.05.03"]
[Time "18:52:38"]
[Round "*"]
[White "Human"]
[Black "hm::Human"]
[Result "*"]
[ECO "D06"]
[Opening "QGD"]
[TimeControl "40/300+1"]
[PlyCount "19"]
"""

    pgn_content = pgn_header + "\n" + " ".join(pgn_moves) + " " + result
    with open(output_file, "w") as f:
        f.write(pgn_content)


