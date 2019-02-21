
import sys

from a_star import a_star
from models.sudoku import Sudoku, criteria


sudoku = Sudoku(sys.argv[1])

# print(sudoku.actions(sudoku.initial))

print(a_star(sudoku, criteria))

