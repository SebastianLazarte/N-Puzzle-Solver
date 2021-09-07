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

## Experiments & Results
1.For n = 2: generate the entire state space manually on a sheet of paper (or a word document).
word document). Scan this sheet (or take a naked picture of it) and include it in your report. How many states are they?

![image](https://user-images.githubusercontent.com/72448046/132264608-524bd951-c8a6-4a1c-ac6c-e1c4e8883389.png)

2.For n = 3: generate the entire state space using a computer program. For this I suggest you
select a randomly generated initial state and start expanding it, taking care not to expand nodes that were previously
expand nodes that were previously expanded. Report the number of states generated and comment.
comment.

![image](https://user-images.githubusercontent.com/72448046/132272167-8dddccdb-4efa-4072-b4a4-5fb6eb85ed22.png)

![image](https://user-images.githubusercontent.com/72448046/132272196-ced56267-3551-4c69-b02b-698bf9434749.png)

![image](https://user-images.githubusercontent.com/72448046/132272210-73c358ad-f9dc-4140-937e-818c88c1fec5.png)




