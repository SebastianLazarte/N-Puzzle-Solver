import copy
import collections
import random
import time
import sys
import warnings
import queue
import math
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
    size = math.sqrt(size)
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


def BFS(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    print("Puzzle a resolver")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.process_time()
    path,count = solver.BFS()
    finalTime = time.process_time()
    step = 0
    nodeSize = 0
    for node in path:
        nodeSize = sys.getsizeof(node)
        if node.father is not None:
            print(node.action)
        node.printState()
        print()
        step = step + 1
    print("Numero de nodos es: " + str(count))
    print("Total de numero de pasos: " + str(step))
    print("Total de tiempo Transcurrido en la busqueda: " + str(finalTime - initialTime)+" segundos")
    print("Memoria ocupada: " + str(nodeSize * count) + " bytes")
    initialTime = 0
    finalTime = 0

def ID(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    print("Puzzle a resolver")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.process_time()
    path,count = solver.iterative_deepening()
    finalTime = time.process_time()
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
        print("Numero de nodos es: " + str(count))
        print("Total de numero de pasos: "+str(step))
        print("Total de tiempo Transcurrido en la busqueda: "+ str(finalTime- initialTime)+" segundos")
        print("Memoria ocupada: " + str(nodeSize * count) + " bytes")


def BFS_ID(size):
    puzzle = Board(GoalBoard(size))
    puzzle = puzzle.generate_random_initial_state(100)
    #puzzle = [[1,2,3],[4,5,7],[0,6,8]]
    print("Puzzle a resolver")
    puzzle.printState()
    print("Steps")
    solver = Solver(puzzle)
    initialTime = time.process_time()
    path,count = solver.iterative_deepening()
    finalTime = time.process_time()
    nodeSize = 0

    initialTime1 = time.process_time()
    path1,count1 = solver.BFS()
    finalTime1 = time.process_time()
    nodeSize1 = 0
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
        
    print("BFS - Numero de nodos: " + str(count1))
    print("BFS - Total de numero de pasos: " + str(step1))
    print("BFS - Total de tiempo Transcurrido en la busqueda: "+ str(finalTime1- initialTime1)+" segundos")
    print("BFS - Memoria ocupada: " + str(nodeSize1 * count) + " bytes")
    print("ID - Numero de nodos: " + str(count))
    print("ID - Total de numero de pasos: " + str(step))
    print("ID - Total de tiempo Transcurrido en la busqueda: "+ str(finalTime- initialTime)+" segundos")
    print("ID - Memoria ocupada: " + str(nodeSize * count) + " bytes")

def main():
    option = 0
    size = 0
    while(option != 4):
        print("1.- Enter the board size")
        print("2.- Solve the board by means of BFS")
        print("3.- Solve the board using Iterative Deepening")
        print("4.- Solve the board using BFS and Iterative Deepening")
        option = input()
        if option == '1':
            print("Please enter the board size")
            size = input()
            if int(size) < 0:
                print("size has to be greater than zero")
        if option == '2':
            print("BFS resolver")
            if int(size) < 0:
                print("Error input")
            else:
                BFS(int(size))
                print()
        if option == '3':
            print("Iterative Deepening resolver")
            if int(size) < 0:
                print("Error input")
            else:
                ID(int(size))
                print()
        if option == '4':
            print("BFS and Iterative Deepening resolver")
            if int(size) < 0:
                print("Error input")
            else:
                BFS_ID(int(size))
                print()


if __name__=='__main__':
    main()
