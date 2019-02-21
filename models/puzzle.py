

from models.problem import Problem
from models.state import State



class Puzzle(Problem):

    def __init__(self, value):
        value = list(value)
        value = [x if x != '.' else '0' for x in value]
        print(value)
        self.size = int(len(value)**0.5)
        self.initial = self.gen_state(value)
        print(self.initial)


    def gen_state(self, value):
        result = State(value)
        result.weight = self.weight(result)

        return result


    def weight(self, state):
        result = 0
        for i, c in enumerate(state.value):
            exp_pos = (int(c, 16) - 1) % 16
            result += abs(i / self.size - exp_pos / self.size) + abs(i % self.size - exp_pos % self.size)

        return int(result)

    def actions(self, state):
        result = []
        pos = state.value.index('0')
        if pos - self.size > -1:
            result.append((pos - self.size, state.value[pos - self.size], pos, '0'))
        if (pos + 1) % self.size != 0:
            result.append((pos + 1, state.value[pos + 1], pos, '0'))
        if pos + self.size < 16:
            result.append((pos + self.size, state.value[pos + self.size], pos, '0'))
        if (pos - 1) % self.size != 3:
            result.append((pos - 1, state.value[pos - 1], pos, '0'))

        return result

    def result(self, state, action):
        value = state.value[:]
        value[action[0]] = action[1]
        value[action[2]] = action[3]

        return self.gen_state(value)

    def goal_test(self, state):
        return state.weight == 0

    def is_explored(self, result, explored):
        for state in explored:
            if state.value == state.value:
                return True

        return False


def criteria(explored):
    result = explored[0]

    for item in explored:
        if item.weight < result.weight:
            result = item

    return result