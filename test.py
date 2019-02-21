
import datetime
import time
import sys
from models.sudoku2 import Sudoku


sector1 = [(0, 0), (0, 1), (1, 0), (1, 1)]
sector2 = [(0, 2), (0, 3), (1, 2), (1, 3)]
sector3 = [(2, 0), (2, 1), (3, 0), (3, 1)]
sector4 = [(2, 2), (2, 3), (3, 2), (3, 3)]


sectors = []
size = 0
matrix = []

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

a = [["1", ".", "3", "."], [".", "2", ".", "4"], [".", ".", "2", "."], [".", "3", ".", "1"]]
b = [["1", ".", "3", "."], [".", "2", ".", "4"], [".", ".", "2", "."], [".", "3", ".", "1"]]
value = [[1, 0, 3, 0], [0, 2, 0, 4], [0, 0, 2, 0], [0, 3, 0, 1]]

def state_actions(matrix, y, x):
    global size

    total_actions = ['1', '2', '3', '4']
    if matrix[y][x] in total_actions:
        return []

    # sector = []
    for sec in sectors:
        if (y, x) in sec:
            sector = sec

    if sector is None:
        return []

    actions = list(set(total_actions) - set(matrix[y]))

    for i in range(size):
        if matrix[i][x] in actions:
            actions.remove(matrix[i][x])
        if matrix[sector[i][0]][sector[i][1]] in actions:
            actions.remove(matrix[sector[i][0]][sector[i][1]])
        if len(actions) == 0:
            return [(action, y, x) for action in actions]

    return [(action, y, x) for action in actions]


def actions(state):
    result = []
    for y in range(len(state)):
        for x in range(len(state[y])):
            result += state_actions(state, y, x)
    return result

def result(state, action):
    new_state = [y[:] for y in state]
    new_state[action[1]][action[2]] = action[0]

    return new_state


def not_in(result, states):
    for state in states:
        if equal(result, state):
            return False

    return True

def equal(state1, state2):
    for y in range(len(state1)):
        for x in range(len(state1[y])):
            if state1[y][x] != state2[y][x]:
                return False

    return True


def weight(value):
    global size, sectors

    print(value)

    weight = 0
    for j in range(size):
        flag_row = 0
        flag_col = 0
        flag_sec = 0
        for i in range(size):
            if not flag_row and value[j][i] == 0:
                flag_row =  1
            if not flag_col and value[i][j] == 0:
                flag_col = 1
            if not flag_sec and value[sectors[j][i][0]][sectors[j][i][1]] == 0:
                flag_sec = 1

        print(flag_row, flag_col, flag_sec)
        weight += flag_row + flag_col + flag_sec
        
    return weight  

def weight2(value):
    global size, sectors

    print(value)

    weight = 0
    for j in range(size):
        flag_row = 0
        flag_col = 0
        flag_sec = 0
        for i in range(size):
            if value[j][i] == 0:
                flag_row += 1
            if value[i][j] == 0:
                flag_col += 1
            if value[sectors[j][i][0]][sectors[j][i][1]] == 0:
                flag_sec += 1

        print(flag_row, flag_col, flag_sec)
        weight += flag_row + flag_col + flag_sec
        
    return weight   

def gen_id(value):
    global size, sectors
    ids = 1
    for j in range(size):
        temp = 1
        for i in range(size):
            temp = temp * primes[i]**matrix[sectors[j][i][0]][sectors[j][i][1]] 
        ids = ids * primes[j]**temp

    return ids

def init():
    global size, sectors

    value = sys.argv[1]

    size = int(len(value)**0.5)
    print(size)
    if size != 9 and size != 4:
        return "Error invalid size"

    temp = int(size **0.5)
    for i in range(temp):
        for j in range(temp):
            s = []
            for y in range(temp):
                for x in range(temp):
                    s.append((y + i * temp, x + j * temp))
            sectors.append(s)

    # print(sectors)

    for j in range(size):
        temp = []
        for i in range(size):
            if value[i + j*size] == '.':
                temp.append(0)
            else:
                temp.append(int(value[i + j*size]))
        matrix.append(temp)

    print(weight2(matrix))
    # a = time.time()
    # x = "333333333333333333333333333333333333333333333" == "33333333333333333333333333333333333333333333342"
    # b = time.time()
    # print(b-a)

    # a = time.time()
    # y = equal(matrix, matrix)
    # b = time.time()
    # print(b - a)
    # states = [matrix]
    # for i in range(10):
    #     print(i, '---------------------------------------- --------------------')
    #     state =  states[0]
    #     actionst = actions(state)
    #     print(actionst)
    #     for action in actionst:
    #         results = result(state, action)
    #         if not_in(results, states):
    #             states.append(results)
    #         print(state, action, results, len(actions(results)))
    #         print("\n")

    #     states.remove(state)


sudoku = Sudoku(sys.argv[1])
