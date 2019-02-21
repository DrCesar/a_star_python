


class State:

    def __init__(self, value, weight=0):
        self.value = value
        self.weight = weight
        self.actions = []

    def __str__(self):
        return "Value: %s, Weight: %s" % (self.value, self.weight)


    