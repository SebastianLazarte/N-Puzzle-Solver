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

![image](https://user-images.githubusercontent.com/58644744/132279530-5967ea99-c14e-4ce6-8df3-64574bbb3c34.jpeg)

**2.For n = 3: generate the entire state space using a computer program. For this I suggest you
select a randomly generated initial state and start expanding it, taking care not to expand nodes that were previously
expand nodes that were previously expanded. Report the number of states generated and comment.**

###### BFS
![image](https://user-images.githubusercontent.com/72448046/132274702-1b253312-c2a7-4dd6-9110-41ce22faf492.png)

![image](https://user-images.githubusercontent.com/72448046/132274737-90b90d50-6248-423f-89cf-66a8ebd1ce0b.png)



Number of states

![image](https://user-images.githubusercontent.com/72448046/132274767-b05ac3a7-1419-4142-be27-3ca1074c7b32.png)


###### ID

![image](https://user-images.githubusercontent.com/72448046/132274809-71bb216e-c990-473e-afb8-f33e4cfca302.png)

![image](https://user-images.githubusercontent.com/72448046/132274816-53b5a7e1-d47c-4ed1-9f18-d9676395b1e9.png)

**3. For n = 4: selects an initial state and a target state that can be reached by executing a set of actions (more than 8).
set of actions (more than 8). Compare execution time and space2 occupied when searching, solving and executing using BFS and Iterative
execution using BFS and Iterative Deepening.Compare them and comment, which one is faster?, which one takes less memory?, why?**


![image](https://user-images.githubusercontent.com/72448046/132280340-e722dbf6-edb2-4262-b7a8-8d92d900b223.png)

BFS is faster than ID, but BFS use more memory because it uses a queue instead of a stack like DLS thats why BFS is faster than ID and use more memory.



