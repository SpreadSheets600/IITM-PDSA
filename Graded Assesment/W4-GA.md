# Graded Assignment 4

Q1 )
For a directed acyclic graph G with n nodes and m edges, what is the asymptotic complexity of efficient algorithms for topological sorting of G ,  using adjacency matrix and adjacency list
representations, respectively?<br><br>
A1 ) $O(n^2),\space O(n+m)$
__________________________________________________________________________________________________________________________
Q2 ) The total number of edges that a complete undirected graph with n vertices can have is _______

[A complete graph is a simple undirected graph in which every pair of vertices is connected by a unique edge.]<br><br>
A2 ) $\frac{n(n-1)}{2}$
__________________________________________________________________________________________________________________________
Q3 )
In the given directed graph, removing one edge e makes it a directed acyclic graph. Which of the following can be the possible values of e ?
</br>
![W4G3](https://github.com/NebulaTris/pdsa-iitm/assets/94922914/bcc5df2c-de7b-4ee8-9497-70fd628934ee)
</br>
A3 )
- [x] 2 -> 4
- [x] 4 -> 1
- [x] 1 -> 2
__________________________________________________________________________________________________________________________
Q4 )
Given below is a function for traversing the graph using BFS(breadth-first search). For which of the following graphs will the function BFS_adjList(vertices, AList) always traverse the complete graph?<br>
![W4G4](https://github.com/NebulaTris/pdsa-iitm/assets/94922914/a63f1272-c6d1-4c4d-9513-62b5072d8ef1)
<br>
A4 ) Connected undirected graphs.
__________________________________________________________________________________________________________________________
Q5 )
Select all the possible topological sorted sequence(s) for the graph given below.</br>
![W4G5](https://github.com/NebulaTris/pdsa-iitm/assets/94922914/28d69ec1-eae0-4522-af5f-1474288ecb23)
 </br>
A5 )
- [x] 0, 5, 4, 6, 1, 2, 3
- [x] 5, 6, 4, 0, 1, 2, 3
- [x] 6, 0, 5, 4, 1, 2, 3
- [x] 6, 5, 4, 0, 1, 2, 3
__________________________________________________________________________________________________________________________
Q6 )
Which of the following graph can be sorted using topological sort?
 </br></br>
A6 )</br>
![W4G6 d](https://github.com/NebulaTris/pdsa-iitm/assets/94922914/ebccb982-ebf5-47b6-8c79-054b746bf95b)

__________________________________________________________________________________________________________________________
Q7 )
Consider a directed graph G with 90 edges with the least number of vertices possible. What will be the number of vertices in graph G 
 </br></br>
A7 )
10
__________________________________________________________________________________________________________________________
Q8 )
We want to represent the graph G mentioned in previous question, in memory either as an Adjacency matrix or Adjacency list. Assume that each cell in the adjacency matrix takes 4 bytes of memory and each edge representation in the adjacency list occupies 8 bytes of memory(you can ignore all other factors that occupy memory). 
What will be the amount of memory required to represent graph G using Adjacency matrix and Adjacency List respectively? (This is follow up question for question 7)
 </br></br>
A8 )
400 bytes, 720 bytes
__________________________________________________________________________________________________________________________
Q9 )
> I: BFS can be used to find the shortest path between two vertices in an unweighted graph.<br>
> II: DFS can be used to find the shortest path between two vertices in an unweighted graph.<br>

Which of the following options is correct?
</br>

A9 )
I is true, II is false.
__________________________________________________________________________________________________________________________
Q10 )
An undirected graph G has 17 vertices. The sum of the degrees of all the vertices in G is D. The number of vertices of even degree in G is K, Which of these values are possible for D and K?
</br></br>
A10 )
D = 42, K = 9
__________________________________________________________________________________________________________________________
Q11 )
A king’s summer house is being rewired. The house has 11 rooms. To avoid wires getting entangled and creating short circuits, the electricians have been asked to observe the following rules. 

* Room 1 must be rewired before rooms 3 and 4. 
* Room 2 must be rewired before room 6. 
* Room 3 must be rewired before room 5. 
* Room 5 must be rewired before rooms 8 and 9. 
* Room 6 must be rewired before room 7. 
* Room 7 must be rewired before room 5. 
* Room 8 must be rewired before room 10. 
* Room 9 must be rewired before room 11. 

It takes one full day to rewire a room. There are enough electricians to rewire as many rooms as can be rewired in parallel, keeping in mind the constraints above. What is the minimum number of days required to complete the job?
</br></br>
A11 )
6
__________________________________________________________________________________________________________________________
Q12 )
We have an undirected graph `G` with `7` vertices. We write down the degrees of all vertices in `G` in descending order. Which of the following is a possible listing of the degrees?

7, 6, 6, 5, 4, 1, 1
6, 6, 6, 3, 2, 2, 1
5, 3, 3, 2, 2, 1, 1
5, 3, 3, 3, 3, 2, 1

</br></br>
A12 )
5, 3, 3, 3, 3, 2, 1
__________________________________________________________________________________________________________________________
Q13 )

![image](https://github.com/user-attachments/assets/80e1d59f-ad38-401d-b9ff-15f0f67ff323)
If we run Breadth First Search(BFS) on the given graph starting from vertex A , which of the following is the order of visiting the nodes?

Note: Assume that when a node has multiple neighbours, BFS visits them alphabetically.
</br></br>
A13 )
A B C G E F D H
__________________________________________________________________________________________________________________________
Q14 )

Consider a simple undirected connected graph G with 65 edges with the least number of vertices possible. What will be the number of vertices in graph G?
</br</br>
A14 ) 12
__________________________________________________________________________________________________________________________
Q15 )

![image](https://github.com/user-attachments/assets/cb65a676-f643-42ad-a981-44b441ce97c9)
How many connected components remain the above graph if the edges (5,9), (4,7), (1,7), (1,5) and (2,9) are deleted ?
</br></br>
A15 ) 3
__________________________________________________________________________________________________________________________
