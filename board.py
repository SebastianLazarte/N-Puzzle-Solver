import copy
import random
import warnings
warnings.filterwarnings('ignore')


class Board:
    def __init__(self, initialState, father=None, action=None):
        self.initialState = initialState
        self.size = len(initialState)
        self.father = father
        self.action = action

    def neighbour(self, parent_register=False):
        boars_neighbours = []
        for i in range(self.size):
            for j in range(self.size):
                if(self.initialState[i][j] == 0):
                    if(j-1 >= 0):
                        aux = copy.deepcopy(self.initialState)
                        aux[i][j-1], aux[i][j] = aux[i][j], aux[i][j-1]
                        boars_neighbours.append(Board(aux, self, 'Left')) if parent_register else boars_neighbours.append(Board(aux))
                    if(i - 1 >= 0):
                        aux = copy.deepcopy(self.initialState)
                        aux[i - 1][j], aux[i][j] = aux[i][j], aux[i - 1][j]
                        boars_neighbours.append(Board(aux, self, 'Up')) if parent_register else boars_neighbours.append(Board(aux))
                    if(i+1 < self.size):
                        aux = copy.deepcopy(self.initialState)
                        aux[i+1][j], aux[i][j] = aux[i][j], aux[i+1][j]
                        boars_neighbours.append(Board(aux, self, 'Down')) if parent_register else boars_neighbours.append(Board(aux))
                    if(j+1 < self.size):
                        aux = copy.deepcopy(self.initialState)
                        aux[i][j+1], aux[i][j] = aux[i][j], aux[i][j+1]
                        boars_neighbours.append(Board(aux, self, 'Right')) if parent_register else boars_neighbours.append(Board(aux))
        return boars_neighbours

    def generate_random_initial_state(self, limit):
        puzzle = self
        for number in range(limit):
            puzzle = random.choice(puzzle.neighbour())
        return puzzle

    def generate_initial_state(self, initialstate):
        puzzle = self
        puzzle = initialstate
        return puzzle

    def path(self):
        nodeActual, path = self, []
        while nodeActual:
            path.append(nodeActual)
            nodeActual = nodeActual.father
        return list(reversed(path))
        
    def printState(self):
        for row in self.initialState:
            print(row)

    def itsSolved(self):
        size = self.size**2
        return self.__repr__() == (' '.join(map(str, range(1, size))) + ' 0')
    def __repr__(self):
        return ' '.join(map(str, self))
    def __iter__(self):
        for row in self.initialState:
            yield from row

   