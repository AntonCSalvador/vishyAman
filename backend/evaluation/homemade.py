"""
Some example classes for people who want to create a homemade bot.

With these classes, bot makers will not have to implement the UCI or XBoard interfaces themselves.
"""

from __future__ import annotations
import chess
from chess.engine import PlayResult, Limit
import random
from lib.engine_wrapper import MinimalEngine, MOVE
from typing import Any
import logging
import chess.engine
import struct
from collections import namedtuple, defaultdict
valueOf = { 'p': 100, 'n': 280, 'b': 320, 'r': 479, 'q': 929, 'k': 60000, 'P': 100, 'N': 280, 'B': 320, 'R': 479, 'Q': 929, 'K': 60000}
myColor = chess.WHITE
oppColor = chess.BLACK

# Use this logger variable to print messages to the console or log files.
# logger.info("message") will always print "message" to the console or log file.
# logger.debug("message") will only print "message" if verbose logging is enabled.
logger = logging.getLogger(__name__)

pst = {
    'P': (  0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
            7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
            0,   0,   0,   0,   0,   0,   0,   0),
    'N': ( -66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69),
    'B': ( -59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10),
    'R': (  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
            0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32),
    'Q': (  6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42),
    'K': (  4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18),
    'p': (  0,   0,   0,   0,   0,   0,   0,   0,
           -31,   8,  -7, -37, -36, -14,   3, -31,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -17,  16,  -2,  15,  14,   0,  15, -13,
             7,  29,  21,  44,  40,  31,  44,   7,
            78,  83,  86,  73, 102,  82,  85,  90,
	        0,   0,   0,   0,   0,   0,   0,   0),
    'n': ( -74, -23, -26, -24, -19, -35, -22, -69,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -18,  10,  13,  22,  18,  15,  11, -14,
            -1,   5,  31,  21,  22,  35,   2,   0,
            24,  24,  45,  37,  33,  41,  25,  17,
            10,  67,   1,  74,  73,  27,  62,  -2,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
 	        -66, -53, -75, -75, -10, -55, -58, -70),
    'b': ( -7,   2, -15, -12, -14, -15, -10, -10,
            19,  20,  11,   6,   7,   6,  20,  16,
            14,  25,  24,  15,   8,  25,  20,  15,
            13,  10,  17,  23,  17,  16,   0,   7,
            25,  17,  20,  34,  26,  25,  15,  10,
            -9,  39, -32,  41,  52, -10,  28, -14,
           -11,  20,  35, -42, -39,  31,   2, -22,
           -59, -78, -82, -76, -23,-107, -37, -50),
    'r': (  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32),
    'q': (   6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42),
    'k': (   4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18),
}

def sunfishValue(board: chess.Board, move, color):
    prom = "Q" # Always promote to queen to save me from migranes
    piece = board.piece_at(move.from_square)
    cap = board.piece_at(move.to_square)
    j = move.to_square
    i = move.from_square
    score = pst[str(piece)][j] - pst[str(piece)][i]
    # Capture
    if cap != None and cap.color != color:
        score += pst[cap.symbol().upper()][j]
    # Castling check detection
    if "O-O" in board.san(move) and board.gives_check(move):
        score += pst["K"][j]
    # Castling
    if piece == "K" and abs(i - j) == 2:
        score += pst["R"][(i + j) // 2]
        score -= pst["R"][56 if j < i else 64]
    # Special pawn stuff
    if piece == "P":
        if 0 <= j <= 8:
            score += pst[prom][j] - pst["P"][j]
        if move.has_legal_en_passant():
            score += pst["P"][j]
    # print(board.san(move), ": ", score)
    return score

def sunfishEval(board: chess.Board, player=True, depth=0):
    matVal = []
    legalMoves = list(board.generate_legal_moves())
    if (player == True):
        color = chess.WHITE if board.piece_at(legalMoves[0].from_square).color == chess.WHITE else chess.BLACK
        enemy_color = chess.BLACK if color == chess.WHITE else chess.WHITE
    else:
        color = chess.BLACK if board.piece_at(legalMoves[0].from_square).color == chess.WHITE else chess.WHITE
        enemy_color = chess.WHITE if color == chess.BLACK else chess.BLACK

    for move in legalMoves:
        matVal.append(0)
        matVal[len(matVal) - 1] = sunfishValue(board, move, color)

    moves = list()
    for i in range(len(legalMoves)):
        newBoard = board.copy()
        newBoard.push(legalMoves[i])

        legalOpponentMoves = list(newBoard.generate_legal_moves())
        try:
            bestResponse = legalOpponentMoves[0]
            for move in legalOpponentMoves:
                if sunfishValue(newBoard, move, enemy_color) >=\
                        sunfishValue(newBoard, bestResponse, enemy_color):
                    bestResponse = move
        except IndexError:
            bestResponse = None
        
        if bestResponse:
            newBoard.push(bestResponse)

        moves.append({
            "move":legalMoves[i].uci(),
            "response":bestResponse.uci() if bestResponse else None,
            "value":matVal[i],
            "fen":newBoard.fen(),
            "depth":depth,
            "next":[]
            })
    return moves

Entry = namedtuple("Entry", "lower upper")
MATE_LOWER = valueOf['K'] - 10 * valueOf['Q']
MATE_UPPER = valueOf['K'] + 10 * valueOf['K']

def material(board: chess.Board, player):
    legalMoves = list(board.generate_legal_moves())
    print(board.san(legalMoves[0]))
    print(chess.square_name(legalMoves[0].from_square))
    print(legalMoves[0].from_square)
    color = chess.WHITE
    if (player == True):
        color = chess.WHITE if board.piece_at(legalMoves[0].from_square).color == chess.WHITE else chess.BLACK
    else:
        color = chess.BLACK if board.piece_at(legalMoves[0].from_square).color == chess.WHITE else chess.WHITE
    print("I am playing as:", color)
    oppColor = not color
    matVal = []
    for move in legalMoves:
        #print("Move SAN: ", board.lan(move))
        #print("From square: ", chess.square_name(move.from_square))
        #print("To square: ", chess.square_name(move.to_square))
        #print("Piece at from square: ", board.piece_at(move.from_square))
        #print("Piece at to square:", board.piece_at(move.to_square))
        matVal.append(0)
        if (board.piece_at(move.from_square) != None):
            if (board.piece_at(move.from_square).color == color and board.is_attacked_by(oppColor, move.to_square) and not board.is_attacked_by(oppColor, move.from_square)):
                matVal[len(matVal) - 1] -= valueOf[board.piece_at(move.from_square).symbol()]
        
        if (board.piece_at(move.from_square) != None):
            if (board.piece_at(move.from_square).color == color and board.is_attacked_by(oppColor, move.to_square)):
                if (board.piece_at(move.from_square).symbol().lower() != "p"):
                    matVal[len(matVal) - 1] -= valueOf[board.piece_at(move.from_square).symbol()]
                
        if (board.piece_at(move.from_square) != None):
            if (board.piece_at(move.from_square).color == color and 'x' in board.san(move)) and not board.is_attacked_by(oppColor, move.to_square):
                matVal[len(matVal) - 1] += valueOf[board.piece_at(move.to_square).symbol()]
        
        if (board.piece_at(move.from_square) != None):
            if (board.piece_at(move.from_square).color == color and not board.is_attacked_by(oppColor, move.from_square)):
                matVal[len(matVal) - 1] -= (valueOf[board.piece_at(move.from_square).symbol()] / 2)
        
        if (board.piece_at(move.from_square != None)):
            if (board.piece_at(move.from_square).color == color and '#' in board.san(move)):
                matVal[len(matVal) - 1] += 999999
        
        if (board.piece_at(move.from_square != None)):
            if (board.piece_at(move.from_square).color == color and '+' in board.san(move)) and not board.is_attacked_by(oppColor, move.to_square):
                matVal[len(matVal) - 1] += 5
        
        print(board.san(move), ":", matVal[len(matVal) - 1], "")
    legalMoves = dict(zip(legalMoves, matVal))
    return legalMoves


class customEngine(MinimalEngine):
    pass

class aNaNd(customEngine):

    
    def search(self, board: chess.Board, time_limit: Limit, ponder: bool, draw_offered: bool, rootMoves: MOVE) -> PlayResult:
        """
        Choose a move using multiple different methods.

        :param board: The current position.
        :param time_limit: Conditions for how long the engine can search (e.g. we have 10 seconds and search up to depth 10).
        :param ponder: Whether the engine can ponder after playing a move.
        :param draw_offered: Whether the bot was offered a draw.
        :param rootMoves: If it is a list, the engine should only play a move that is in `root_moves`.
        :return: The move to play.
        """
        if isinstance(time_limit.time, int):
            time = time_limit.time
            inc = 0
        elif (board.turn == chess.WHITE):
            time = time_limit.white_clock if isinstance(time_limit.white_clock, int) else 0
            inc = time_limit.white_inc if isinstance(time_limit.white_inc, int) else 0
        else:
            time = time_limit.black_clock if isinstance(time_limit.black_clock, int) else 0
            inc = time_limit.black_inc if isinstance(time_limit.black_inc, int) else 0
        if (isinstance(rootMoves, list)):
            legalMoves = rootMoves
        else:
            legalMoves = list(board.legal_moves)
        for move in board.generate_legal_captures():
            print(board.piece_at(move.from_square))
            print(chess.square_name(move.from_square))
        legalMoves = sunfishEval(board, True)
        """
        tmpMoves = dict((board.san(k), v) for k, v in legalMoves.items())
        for move in list(tmpMoves.items()):
            print(move)
        """
        if ((time / 60) + inc > 10):
            # Choose a random move.
            # move = random.choice(legalMoves)
            #legalMoves = list(legalMoves.keys())
            move = max(legalMoves, key=legalMoves.get) 
            print(move)
        else:
            #legalMoves = list(legalMoves.keys())
            move = max(legalMoves, key=legalMoves.get)
            print(move)
        return PlayResult(move, None, draw_offered=draw_offered)

class ExampleEngine(MinimalEngine):
    """An example engine that all homemade engines inherit."""

    pass


# Bot names and ideas from tom7's excellent eloWorld video

class RandomMove(ExampleEngine):
    """Get a random move."""

    def search(self, board: chess.Board, *args: Any) -> PlayResult:
        """Choose a random move."""
        return PlayResult(random.choice(list(board.legal_moves)), None)


class Alphabetical(ExampleEngine):
    """Get the first move when sorted by san representation."""

    def search(self, board: chess.Board, *args: Any) -> PlayResult:
        """Choose the first move alphabetically."""
        moves = list(board.legal_moves)
        moves.sort(key=board.san)
        return PlayResult(moves[0], None)


class FirstMove(ExampleEngine):
    """Get the first move when sorted by uci representation."""

    def search(self, board: chess.Board, *args: Any) -> PlayResult:
        """Choose the first move alphabetically in uci representation."""
        moves = list(board.legal_moves)
        moves.sort(key=str)
        return PlayResult(moves[0], None)


class ComboEngine(ExampleEngine):
    """
    Get a move using multiple different methods.

    This engine demonstrates how one can use `time_limit`, `draw_offered`, and `root_moves`.
    """

    def search(self, board: chess.Board, time_limit: Limit, ponder: bool, draw_offered: bool, root_moves: MOVE) -> PlayResult:
        """
        Choose a move using multiple different methods.

        :param board: The current position.
        :param time_limit: Conditions for how long the engine can search (e.g. we have 10 seconds and search up to depth 10).
        :param ponder: Whether the engine can ponder after playing a move.
        :param draw_offered: Whether the bot was offered a draw.
        :param root_moves: If it is a list, the engine should only play a move that is in `root_moves`.
        :return: The move to play.
        """
        if isinstance(time_limit.time, int):
            my_time = time_limit.time
            my_inc = 0
        elif board.turn == chess.WHITE:
            my_time = time_limit.white_clock if isinstance(time_limit.white_clock, int) else 0
            my_inc = time_limit.white_inc if isinstance(time_limit.white_inc, int) else 0
        else:
            my_time = time_limit.black_clock if isinstance(time_limit.black_clock, int) else 0
            my_inc = time_limit.black_inc if isinstance(time_limit.black_inc, int) else 0

        possible_moves = root_moves if isinstance(root_moves, list) else list(board.legal_moves)

        if my_time / 60 + my_inc > 10:
            # Choose a random move.
            move = random.choice(possible_moves)
        else:
            # Choose the first move alphabetically in uci representation.
            possible_moves.sort(key=str)
            move = possible_moves[0]
        return PlayResult(move, None, draw_offered=draw_offered)
