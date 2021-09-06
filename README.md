# N-Puzzle-Solver

## Problem Description

It consists of implementing a computer program to solve the (n^2 - 1)-puzzle using the BFS and Iterative deepening algorithms.

## Solution Description

Two classes were used: Board, Solver

Board performs all actions that involve the board, such as: generate random initial state and change the states

Solver contains the algoritms y create the paths.

## BFS
BFS scans the network by levels. It guarantees to find the shortest path to a goal (optimality & completness).
It starts from the initial state, visits and expands the nodes until it reaches the goal state. 

## ID(Iterative Deepening)
Has the advantages of BFS and DFS 
Memory requirements are linear (DFS) Guarantees an optimal solution (if exists) (BFS)

##Experiments & Results

![image](https://user-images.githubusercontent.com/72448046/132264608-524bd951-c8a6-4a1c-ac6c-e1c4e8883389.png)





