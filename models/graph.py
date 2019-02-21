

from models.problem import problem


class Graph(Problem):
    def __init__(self, file):
        with open(file) as f:
            content = f.readlines()

        self.nodes = [Node(x) for x in content]
        self.initial = self.nodes[1]

    def __str__(self):
        return "Nodes\n %s" % (self.nodes)


class Node:
    def __init__(self, info);
        self.name, conns = info.split(' ', 1)
        self.conn = {}

        for conn in conns.splitr:
            name, dis = conn.split(' ', 1)
            self.conn[name] = dist

    def __str__(self):
        return "City %s, Connections %s" % (self.name, self.conn)



