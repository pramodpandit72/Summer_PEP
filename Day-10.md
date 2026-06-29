# Graphs

## Definition

A Graph is a data structure used to represent relationships between objects.

A graph consists of:

```text
1. Vertices (Nodes)
2. Edges (Connections)
```

---

## Example

```text
A ----- B
|       |
|       |
C ----- D
```

Here:

```text
Vertices = A, B, C, D

Edges = (A,B), (A,C), (B,D), (C,D)
```

---

# Real Life Examples

### Social Media

```text
User → Friends
```

---

### Google Maps

```text
Cities → Roads
```

---

### Computer Networks

```text
Computers → Connections
```

---

### Flight Routes

```text
Airports → Flights
```

---

# Terminology

## Vertex (Node)

A single point in a graph.

Example:

```text
A
```

---

## Edge

Connection between two nodes.

Example:

```text
A ---- B
```

---

## Degree

Number of edges connected to a node.

Example:

```text
A ---- B
|
|
C
```

Degree of A:

```text
2
```

---

# Types of Graphs

---

## 1. Undirected Graph

Edges work both ways.

```text
A ---- B
```

Means:

```text
A → B

B → A
```

---

## 2. Directed Graph

Edges have direction.

```text
A → B
```

Means:

```text
A can reach B

B cannot necessarily reach A
```

---

## 3. Weighted Graph

Edges contain weights.

```text
A --5-- B
```

Weight:

```text
5
```

---

## 4. Unweighted Graph

No weights.

```text
A ---- B
```

---

# Graph Representation

Most important topic before BFS and DFS.

---

# Adjacency List

Most commonly used.

---

## Example

Graph:

```text
1 -- 2
|    |
|    |
3 -- 4
```

---

Adjacency List:

```cpp
1 -> 2,3

2 -> 1,4

3 -> 1,4

4 -> 2,3
```

---

## Code

```cpp
vector<int> adj[n + 1];

adj[1].push_back(2);
adj[2].push_back(1);
```

---

## Space Complexity

```text
O(V + E)
```

Best for interviews.

---

# BFS (Breadth First Search)

## Definition

BFS visits nodes level by level.

It explores all neighbors first before moving deeper.

---

# Data Structure Used

```text
Queue
```

because BFS follows FIFO order.

---

# Example

Graph:

```text
        1
      /   \
     2     3
    / \
   4   5
```

---

BFS Traversal:

```text
1 2 3 4 5
```

Level by level.

---

# BFS Algorithm

### Step 1

Visit source node.

---

### Step 2

Push into queue.

---

### Step 3

Process neighbors.

---

### Step 4

Repeat until queue becomes empty.

---

# BFS Code

```cpp
void bfs(int start,
         vector<int> adj[],
         int n)
{
    vector<int> vis(n + 1, 0);

    queue<int> q;

    q.push(start);

    vis[start] = 1;

    while(!q.empty())
    {
        int node = q.front();

        q.pop();

        cout << node << " ";

        for(auto nbr : adj[node])
        {
            if(!vis[nbr])
            {
                vis[nbr] = 1;

                q.push(nbr);
            }
        }
    }
}
```

---

# BFS Complexity

### Time

```text
O(V + E)
```

---

### Space

```text
O(V)
```

---

# Applications of BFS

- Shortest Path (Unweighted Graph)
- Level Order Traversal
- Social Network Problems
- Connected Components
- Flood Fill

---

# DFS (Depth First Search)

## Definition

DFS explores as deep as possible before backtracking.

---

# Data Structure Used

```text
Recursion Stack
```

or

```text
Stack
```

---

# Example

Graph:

```text
        1
      /   \
     2     3
    / \
   4   5
```

---

Possible DFS:

```text
1 2 4 5 3
```

---

# DFS Algorithm

### Step 1

Visit current node.

---

### Step 2

Visit an unvisited neighbor.

---

### Step 3

Keep going deeper.

---

### Step 4

Backtrack when no neighbor remains.

---

# DFS Recursive Code

```cpp
void dfs(int node,
         vector<int> adj[],
         vector<int>& vis)
{
    vis[node] = 1;

    cout << node << " ";

    for(auto nbr : adj[node])
    {
        if(!vis[nbr])
        {
            dfs(nbr, adj, vis);
        }
    }
}
```

---

# Calling DFS

```cpp
vector<int> vis(n + 1, 0);

dfs(1, adj, vis);
```

---

# DFS Complexity

### Time

```text
O(V + E)
```

---

### Space

```text
O(V)
```

(recursion stack)

---

# BFS vs DFS

| Feature | BFS | DFS |
|----------|------|------|
| Data Structure | Queue | Stack/Recursion |
| Traversal | Level Wise | Depth Wise |
| Shortest Path | Yes (Unweighted) | No |
| Memory | More | Less |

---

# Connected Components

## Definition

A Connected Component is a group of nodes where every node can reach every other node.

---

## Example

Graph:

```text
1 -- 2 -- 3

4 -- 5

6
```

Components:

```text
{1,2,3}

{4,5}

{6}
```

Total:

```text
3 Connected Components
```

---

# Finding Connected Components

## Idea

Run DFS/BFS from every unvisited node.

Every new DFS/BFS represents a new component.

---

# DFS Solution

```cpp
int count = 0;

for(int i = 1; i <= n; i++)
{
    if(!vis[i])
    {
        dfs(i, adj, vis);

        count++;
    }
}
```

---

# Complexity

```text
O(V + E)
```

---

# Important Graph Pattern

Whenever you see:

```text
Number of Groups

Number of Provinces

Number of Islands

Connected Networks

Friend Circles
```

Think:

```text
Connected Components
```

---

# Number of Islands Concept

Grid:

```text
1 1 0

0 1 0

1 0 1
```

Components:

```text
Island 1

Island 2

Island 3
```

Answer:

```text
3
```

This is a graph problem solved using DFS/BFS.

---

# BFS on Grid

Very important for interviews.

Directions:

```cpp
int dx[4] = {-1, 1, 0, 0};

int dy[4] = {0, 0, -1, 1};
```

Used for:

- Number of Islands
- Flood Fill
- Rotten Oranges
- Shortest Path in Grid

---

# DFS on Grid

Same concept.

Move:

```text
Up
Down
Left
Right
```

and mark visited cells.

---

# How to Identify BFS Problems?

Look for:

- Minimum Steps
- Shortest Path
- Level Order
- Nearest Distance
- Multi Source Expansion

These usually indicate BFS.

---

# How to Identify DFS Problems?

Look for:

- Connected Components
- Islands
- Reachability
- Cycles
- Backtracking Style Traversal

These usually indicate DFS.

---

# Important LeetCode Questions

## Easy

### 1. Find if Path Exists in Graph
LeetCode #1971

Concept:
- BFS / DFS

⭐⭐ Must Do

---

### 2. Flood Fill
LeetCode #733

Concept:
- DFS/BFS

⭐⭐ Important

---

# Medium

### 3. Number of Provinces
LeetCode #547

Concept:
- Connected Components

⭐⭐⭐ Must Do

---

### 4. Number of Islands
LeetCode #200

Concept:
- DFS/BFS

⭐⭐⭐ Very Important

---

### 5. Rotting Oranges
LeetCode #994

Concept:
- Multi Source BFS

⭐⭐⭐ Frequently Asked

---

### 6. Clone Graph
LeetCode #133

Concept:
- Graph Traversal

---

### 7. Keys and Rooms
LeetCode #841

Concept:
- DFS

---

### 8. Max Area of Island
LeetCode #695

Concept:
- DFS

⭐⭐ Important

---

### 9. Pacific Atlantic Water Flow
LeetCode #417

Concept:
- BFS / DFS

---

# Hard

### 10. Word Ladder
LeetCode #127

Concept:
- BFS

⭐⭐⭐ Top Interview Question

---

### 11. Shortest Path in Binary Matrix
LeetCode #1091

Concept:
- BFS

⭐⭐ Frequently Asked

---

# Must-Do Interview Questions

1. Find if Path Exists in Graph (#1971)
2. Flood Fill (#733)
3. Number of Provinces (#547)
4. Number of Islands (#200)
5. Rotting Oranges (#994)
6. Max Area of Island (#695)
7. Clone Graph (#133)
8. Keys and Rooms (#841)
9. Word Ladder (#127)
10. Shortest Path in Binary Matrix (#1091)

These questions cover the most important BFS, DFS, Graph Traversal, Grid Traversal, and Connected Components patterns commonly asked in coding interviews.