
from models.problem import Problem
from models.state import State

class Sudoku(Problem):
    def __init__(self, value):
        value = list(value)
        self.comp = 0
        self.size = int(len(value)**0.5)
        self.sectors = []
        temp = int(self.size**0.5)
        for i in range(temp):
            for j in range(temp):
                s = []
                for y in range(temp):
                    for x in range(temp):
                        s.append((y + i * temp) * self.size + x + j * temp)
                self.sectors.append(s)

        value = list(value)

        print(self.size)
        print(self.sectors)
        self.initial = self.gen_state(value)

    def gen_state(self, value):
        weight = self.weight(value)
        # weight = self.weight(value) * 100  + self.size**sum([x.count(0) for x in value]) - len(self.actions_value(value))
        # weight = abs(sum([x.count(0) for x in value]) - len(self.actions_value(value)))
        # weight = sum([x.count(0) for x in value])
        # _id = sum([prime**num for prime in primes for arr in value for num in arr])

        return State(value, weight)

    def actions_value(self, value):
        result = []
        for y in range(len(value)):
            for x in range(len(value[y])):
                result += self.state_actions(value, y, x)
        return result

    def actions(self, state):
        result = []
        for y in range(len(state.value)):
            for x in range(len(state.value[y])):
                result += self.state_actions(state.value, y, x)
        return result

    def result(self, state, action):
        new_state = [y[:] for y in state.value]
        new_state[action[1]][action[2]] = action[0]

        return self.gen_state(new_state)

    def goal_test(self, state):
        for y in state.value:
            for x in y:
                if x == 0:
                    return False
        return True

    # @classmethod
    def is_explored(self, result, explored):
        for state in explored:
            if self.equal(result.value, state.value):
                return True
        return False

    def weight(self, value):

        weight = 0
        for j in range(self.size):
            flag_row = 0
            flag_col = 0
            flag_sec = 0
            for i in range(self.size):
                if not flag_row and value[j][i] == 0:
                    flag_row =  1
                if not flag_col and value[i][j] == 0:
                    flag_col = 1
                if not flag_sec and value[self.sectors[j][i][0]][self.sectors[j][i][1]] == 0:
                    flag_sec = 1

            weight += flag_row + flag_col + flag_sec
            
        return weight    

    def state_actions(self, matrix, y, x):

        total_actions = [x + 1 for x in range(self.size)]
        if matrix[y][x] in total_actions:
            return []

        if matrix[y][x] in total_actions:
            return []

        for sec in self.sectors:
            if (y, x) in sec:
                sector = sec

        if sector is None:
            return []

        actions = list(set(total_actions) - set(matrix[y]))

        for i in range(self.size):
            if matrix[i][x] in actions:
                actions.remove(matrix[i][x])
            if matrix[sector[i][0]][sector[i][1]] in actions:
                actions.remove(matrix[sector[i][0]][sector[i][1]])
            if len(actions) == 0:
                return [(action, y, x) for action in actions]

        return [(action, y, x) for action in actions]

    def equal(self, state1, state2):
        for y in range(len(state1)):
            for x in range(len(state1[y])):
                if state1[y][x] != state2[y][x]:
                    return False

        return True

    def print_state(self, state):
        for y in state:
            s = "|"
            for x in y:
                s += str(x)
            print(s + "|")

        return


        


def criteria(explored):
    result = explored[0]

    for item in explored:
        if item.weight < result.weight:
            result = item

    return result