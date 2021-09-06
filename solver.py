import collections
from typing import Counter
import warnings
warnings.filterwarnings('ignore')


class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def create_path(node, line, state):
        for path in node.neighbour(parent_register=True):
            if path.__repr__() not in state:
                line.appendleft(path)
                state.add(path.__repr__())

    def BFS(self):
        count = 1
        line = collections.deque([self.puzzle])
        state = set()
        state.add(self.puzzle.__repr__())
        num = 0
        while line:
            count =  count + 1
            node = line.pop()
            if node.itsSolved():
                return node.path(),count
            Solver.create_path(node, line, state)

    def iterative_deepening(self):
        i = 1
        
        while i < 200000:
            result,count = self.dls_no_recursive(i)
            if result == 'CUTOFF':
                i = i + 1
            else:
                i = 200000
        return result,count

    def dls_no_recursive(self, limit):
        count = 1
        stack = collections.deque([self.puzzle])
        state = set()
        state.add(self.puzzle.__repr__())
        while limit > 0 and stack:
            count = count + 1
            node = stack.popleft()
            if node.itsSolved():
                return node.path(),count
            limit = limit - 1
            Solver.create_path(node, stack, state)
        if limit == 0 and node.itsSolved() == False:
            return 'CUTOFF',count
