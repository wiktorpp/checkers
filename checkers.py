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
board = startBoard
aviableMovesPrompt = \
"┌     ┐\n" + \
" \   / \n" + \
"  1 2  \n" + \
"  4 3  \n" + \
" /   \\\n" + \
"└     ┘"

def asciifyBoard():
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

def move(x, y, direction):
    pass

def strToCoords(string):
    if string[0].isupper() == True:
        x = ord(string[0]) - 64
    elif string[0].islower():
        x = ord(string[0]) - 96
    else:
        raise Exception("Invalid coordinates")
    y = int(string[1])
    return [x, y]

def coordsToStr(x, y):
    return chr(65 + x) + str(y + 1)