

import sys

from a_star import a_star
from models.puzzle import Puzzle, criteria

puzzle = Puzzle(sys.argv[1])

print(a_star(puzzle, criteria))