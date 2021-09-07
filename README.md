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

![image](https://user-images.githubusercontent.com/72448046/132282286-aa7161b3-d88f-410f-b9f5-a28c943ba455.png)

Number of states: 8

###### ID

![image](https://user-images.githubusercontent.com/72448046/132282332-a2fa45f1-750e-4d90-a6c2-bad380394895.png)

Number of states: 4

**3. For n = 4: selects an initial state and a target state that can be reached by executing a set of actions (more than 8).
set of actions (more than 8). Compare execution time and space2 occupied when searching, solving and executing using BFS and Iterative
execution using BFS and Iterative Deepening.Compare them and comment, which one is faster?, which one takes less memory?, why?**


![image](https://user-images.githubusercontent.com/72448046/132282576-69c1a1ff-dd69-4cc6-90b4-493b81579844.png)

![image](https://user-images.githubusercontent.com/72448046/132282598-33337d2d-9d16-42b7-9dee-d5d99db1eb0a.png)


BFS is faster than ID, but BFS use more memory because it uses a queue instead of a stack like DLS thats why BFS is faster than ID, but ID use less memory.

## Conclusions
The fact of being able to differentiate the times and memory usage of each algorithm allows a good choice according to the program to be realized.
## Bibliography
https://github.com/mahdavipanah/pynpuzzle
https://github.com/rjoonas/AI-assignment-1
https://github.com/asarandi/n-puzzle
https://github.com/andavies/n-puzzle


