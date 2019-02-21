

import sys

# print(sys.argv)

# s = "A (Z, 75) (B, 80)(x,20)"

# print(s.split(')'))


def a_star(problem, criteria):
    frontier = [problem.initial]
    explored = []

    cont = 0

    while True:
        if len(frontier):
            # x = input()
            state = criteria(frontier)
            frontier.remove(state)
            cont += 1
            explored.append(state)

            print(state)


            if problem.goal_test(state):
                print(cont)
                return state

            for action in problem.actions(state):
                result = problem.result(state, action)

                if not problem.is_explored(result, explored):
                    # new_path = Path([])
                    # new_path.extendFrom(path)
                    # new_path.addStep(result)
                    if not is_in(result, frontier):
                        frontier.append(result)

        else:
            return False



def is_in(result, states):
    for state in states:
        if equal(result.value, state.value):
            return True
    return False


def equal(state1, state2):
    for y in range(len(state1)):
        for x in range(len(state1[y])):
            if state1[y][x] != state2[y][x]:
                return False

    return True