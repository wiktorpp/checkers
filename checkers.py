from sys import *

startBoard = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0]
]

def asciifyBoard(board):
    ret = ""
    ret += "╔═╦═╦═╦═╦═╦═╦═╦═╗\n"
    for i in board:
        ret += "║"
        for j in i:
            if j == 0:
                ret += " "
            if j == 1:
                ret += "1"
            if j == 2:
                ret += "2"
            ret += "│"
        ret = ret[:-1]
        ret += "║\n╠"
        for j in range(len(i)):
            ret += "─┼"
        ret = ret[:-1]
        ret += "╣\n"
    ret = ret[:-18]
    ret += "╚"
    for j in range(len(i)):
        ret += "═╩"
    ret = ret[:-1]
    ret += "╝"
    return ret