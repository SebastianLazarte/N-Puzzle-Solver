import time
import sys
import warnings
import math
import timeit
from solver import Solver
from board import Board
warnings.filterwarnings('ignore')


def GoalBoard(size):
    goalBoard = []
    array = [i for i in range(1, size * size)]
    array.append(0)
    for i in range(size):
        aux = []
        for j in range(size):
            aux.append(array[i * size + j])
        goalBoard.append(aux)
    return goalBoard


def InitialBoard(initialBoard, goalBoard):
    size = len(initialBoard)
    size = int(math.sqrt(size))
    initialState = []
    goalState = []
    for i in range(size):
        aux = []
        secondAux = []
        for j in range(size):
            aux.append(initialBoard[i * size + j])
            secondAux.append(goalBoard[i * size + j])
        initialState.append(aux)
        goalState.append(secondAux)
    return initialState, goalState

def mapperList(list_):
    return list(map(int,list_))

def readTxtFile(name,limit):
    data=[]
    aux=1
    with open(str(name)+".txt") as fname:
        for line in fname:
            if limit == aux:
                data.extend(line.split())
            aux = aux + 1
    return data



def readFile(name):
    initialBoard = []
    goalBoard = []
    initialBoard=readTxtFile(name,1)
    goalBoard = readTxtFile(name,2)
    initialBoard = mapperList(initialBoard)
    goalBoard = mapperList(goalBoard)
    return InitialBoard(initialBoard, goalBoard)

def printInfoDFSandID(count1,step1,finalTime1,initialTime1,nodeSize1,count,step,finalTime,initialTime,nodeSize):
    print("BFS - Number of nodes is: " + str(count1))
    print("BFS - Total number of steps: " + str(step1))
    print("BFS - Total search time elapsed: "+ str(finalTime1- initialTime1)+" seconds")
    print("BFS - Memoria ocupada: " + str(nodeSize1 * count1) + " bytes")
    print("ID - Number of  nodes is: " + str(count))
    print("ID - Total number of steps: " + str(step))
    print("ID - Total search time elapsed: "+ str(finalTime- initialTime)+" seconds")
    print("ID - Use of memory: " + str(nodeSize * count) + " bytes")

def printInfo(count,step,finalTime,initialTime,nodeSize):
    print("Number of nodes is: " + str(count))
    print("Total number of steps: " + str(step))
    print("Total search time elapsed: " + str(finalTime - initialTime)+" seconds")
    print("Use of memory: " + str(nodeSize * count) + " bytes")

def BFS(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    print("Puzzle to be solved")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.time()
    path,count = solver.BFS()
    finalTime = time.time()
    step = 0
    nodeSize = 0
    for node in path:
        nodeSize = sys.getsizeof(node)
        if node.father is not None:
            print(node.action)
        node.printState()
        print()
        step = step + 1
    printInfo(count,step,finalTime,initialTime,nodeSize)
    

def ID(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    print("Puzzle to be solved")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.time()
    path,count = solver.iterative_deepening()
    finalTime = time.time()
    step = 0
    nodeSize = 0
    if path == 'CUTOFF':
        print("Solution not found within these limits")
    else:
        for node in path:
            nodeSize = sys.getsizeof(node)
            if node.father is not None:
                print(node.action)
            node.printState()
            print()
            step = step + 1

    printInfo(count,step,finalTime,initialTime,nodeSize)


def BFS_ID(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    #puzzle = [[1,2,3],[4,5,7],[0,6,8]]
    print("Puzzle to be solved")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.time()
    path,count = solver.iterative_deepening()
    finalTime = time.process_time()
    #nodeSize = 0

    initialTime1 = time.time()
    path1,count1 = solver.BFS()
    finalTime1 = time.time()
    #nodeSize1 = 0
    step = 0
    step1 = 0
    if path == 'CUTOFF':
        print("Solution not found within these limits")
    else:
        for node in path:
            nodeSize = sys.getsizeof(node)
            step = step + 1
        for node in path1:
            nodeSize1 = sys.getsizeof(node)
            step1 = step1+1 
    printInfoDFSandID(count1,step1,finalTime1,initialTime1,nodeSize1,count,step,finalTime,initialTime,nodeSize)

def BFSFILE(state):
    initialState = state[0]
    goalState = state[1]
    puzzle = Board(goalState)
    puzzle = puzzle.generate_initial_state(Board(initialState))
    print("Puzzle to be solved")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.time()
    path,count = solver.BFS()
    finalTime = time.time()
    step = 0
    nodeSize = 0
    for node in path:
        nodeSize = sys.getsizeof(node)
        if node.father is not None:
                print(node.action)
        node.printState()
        print()
        step = step + 1
    printInfo(count,step,finalTime,initialTime,nodeSize)

def IDFILE(state):
    initialState = state[0]
    goalState = state[1]
    puzzle = Board(goalState)
    puzzle = puzzle.generate_initial_state(Board(initialState))
    print("Puzzle to be solved")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.time()
    path,count = solver.iterative_deepening()
    finalTime = time.time()
    step = 0
    nodeSize = 0
    for node in path:
        nodeSize = sys.getsizeof(node)
        if node.father is not None:
                print(node.action)
        node.printState()
        print()
        step = step + 1

    printInfo(count,step,finalTime,initialTime,nodeSize)

def BFS_IDFILE(state):
    initialState = state[0]
    goalState = state[1]
    puzzle = Board(goalState)
    puzzle = puzzle.generate_initial_state(Board(initialState))
    print("Puzzle to be solved")
    puzzle.printState()
    solver = Solver(puzzle)
    
    initialTime1 = time.time()
    path1,count1 = solver.BFS()
    finalTime1 = time.time()
    nodeSize1 = 0
    initialTime = time.time()
    path,count = solver.iterative_deepening()
    finalTime = time.time()
    
    nodeSize = 0
    step = 0
    step1 = 0
    if path == 'CUTOFF':
        print("Solution not found within these limits")
    else:
        for node in path:
            nodeSize = sys.getsizeof(node)
            if node.father is not None:
                print(node.action)
            node.printState()
            print()
            step = step + 1
        for node in path1:
            if node.father is not None:
                print(node.action)
            node.printState()
            print()
            nodeSize1 = sys.getsizeof(node)
            step1 = step1+1

    printInfoDFSandID(count1,step1,finalTime1,initialTime1,nodeSize1,count,step,finalTime,initialTime,nodeSize)

def fileMain():
    print("Enter the name of the text file")
    name = input()
    print("1.- Solve the board using BFS")
    print("2.- Solve the board using Iterative Deepening")
    print("3.- Solve the board using BFS and Iterative Deepening")
    option = input()
    state = readFile(name)
    if option == '1':
        print("BFS solver")
        BFSFILE(state)
        print()
    if option == '2':
        print("ID solver")
        IDFILE(state)
        print()
    if option == '3':
        print("BFS & ID solver")
        BFS_IDFILE(state)
        print()

def main():
    option = 0
    size = 0
    while(option != 5):
        print("1.- Enter the board size")
        print("2.- Solve the board using of BFS")
        print("3.- Solve the board using Iterative Deepening")
        print("4.- Solve the board using BFS and Iterative Deepening")
        print("5.- Enter values ​​from text")
        option = input()
        if option == '1':
            print("Please enter the board size")
            size = input()
            if int(size) < 0:
                print("size has to be greater than zero")
        if option == '2':
            print("BFS solver")
            if int(size) < 0:
                print("Error input")
            else:
                BFS(int(size))
                print()
        if option == '3':
            print("Iterative Deepening solver")
            if int(size) < 0:
                print("Error input")
            else:
                ID(int(size))
                print()
        if option == '4':
            print("BFS & ID solver")
            if int(size) < 0:
                print("Error input")
            else:
                BFS_ID(int(size))
                print()
        if option == '5':
            fileMain()


if __name__=='__main__':
    main()
