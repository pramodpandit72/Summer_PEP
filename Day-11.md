# Graphs II – Shortest Paths & Dijkstra Algorithm

---

# Shortest Path in Graph

## Definition

Shortest path means:

```text
Minimum distance / minimum cost between two nodes
```

---

## Types of Shortest Path Problems

### 1. Unweighted Graph

- All edges have same weight (usually 1)
- Use: **BFS**

```text
Time: O(V + E)
```

---

### 2. Weighted Graph (Non-negative weights)

- Edge weights ≥ 0
- Use: **Dijkstra’s Algorithm**

---

### 3. Weighted Graph (Negative weights)

- Use: **Bellman-Ford Algorithm** (not covered here yet)

---

# Dijkstra’s Algorithm

## Definition

Dijkstra’s Algorithm finds the shortest path from a source node to all other nodes in a weighted graph.

It works only when:

```text
All edge weights are non-negative
```

---

# Idea (Greedy)

Always pick the node with the smallest known distance first.

Then relax its neighbors.

---

# Relaxation Concept

If:

```text
dist[u] + weight(u → v) < dist[v]
```

Then update:

```text
dist[v] = dist[u] + weight
```

---

# Example Graph

```text
      (1)
   2 /   \ 4
    A     B
     \   /
     1\ /1
       C
```

Source = A

---

## Step-by-step idea

```text
Start: A = 0, others = ∞

A → update neighbors

Pick smallest unvisited node

Repeat
```

---

# Data Structure Used

```text
Priority Queue (Min Heap)
```

Because we always want the smallest distance node first.

---

# Why Min Heap?

We need:

```text
Extract minimum distance node in O(log V)
```

---

# Dijkstra Algorithm Steps

## Step 1

Initialize distances:

```text
dist[source] = 0
others = ∞
```

---

## Step 2

Push source into min heap.

---

## Step 3

While heap not empty:

- Take node with smallest distance
- Relax all neighbors

---

## Step 4

Update distances if shorter path found.

---

# Dijkstra Code (C++)

```cpp
vector<int> dijkstra(int V,
                     vector<pair<int,int>> adj[],
                     int src)
{
    vector<int> dist(V, INT_MAX);

    priority_queue<
        pair<int,int>,
        vector<pair<int,int>>,
        greater<pair<int,int>>
    > pq;

    dist[src] = 0;

    pq.push({0, src});

    while(!pq.empty())
    {
        int d = pq.top().first;
        int node = pq.top().second;

        pq.pop();

        for(auto it : adj[node])
        {
            int adjNode = it.first;
            int wt = it.second;

            if(d + wt < dist[adjNode])
            {
                dist[adjNode] = d + wt;

                pq.push({dist[adjNode], adjNode});
            }
        }
    }

    return dist;
}
```

---

# Time Complexity

```text
O((V + E) log V)
```

---

# Space Complexity

```text
O(V)
```

---

# Why Dijkstra Works

Because:

```text
Once a node is picked with smallest distance,
its shortest path is finalized.
```

This is greedy property.

---

# Important Observations

## 1. Node can be pushed multiple times

Yes, but we ignore outdated entries.

---

## 2. Greedy choice is safe

Because weights are non-negative.

---

# Dijkstra Variations

---

## 1. Single Source Shortest Path (SSSP)

Find shortest path from one source to all nodes.

---

## 2. Shortest Path to a Specific Node

Stop early when target is reached.

---

## 3. Grid Shortest Path

Used in:

- Maze problems
- Matrix shortest path

---

# BFS vs Dijkstra

| Feature | BFS | Dijkstra |
|----------|-----|----------|
| Edge Weight | 1 only | Any non-negative |
| Data Structure | Queue | Min Heap |
| Complexity | O(V+E) | O((V+E) log V) |

---

# When to Use What?

## Use BFS when:

```text
All edges = 1
```

Examples:

- Shortest path in maze (unweighted)
- Minimum moves problems

---

## Use Dijkstra when:

```text
Edges have different weights
```

Examples:

- Road networks
- Cost-based paths
- Flight prices

---

# Grid Dijkstra (Very Important)

Used when:

```text
Each cell has cost
```

Example:

```text
Minimum cost path in matrix
```

---

# Common Pattern

Convert grid → graph

Then apply Dijkstra.

---

# Important LeetCode Problems

---

## Easy

### 1. Network Delay Time
LeetCode #743

Concept:
- Dijkstra

⭐⭐ Must Do

---

### 2. Path With Minimum Effort
LeetCode #1631

Concept:
- Grid Dijkstra

⭐⭐⭐ Very Important

---

# Medium

### 3. Cheapest Flights Within K Stops
LeetCode #787

Concept:
- Modified Dijkstra / BFS

⭐⭐⭐ Interview Favorite

---

### 4. Find the City With the Smallest Number of Neighbors
LeetCode #1334

Concept:
- All-pairs shortest path idea

---

### 5. Swim in Rising Water
LeetCode #778

Concept:
- Dijkstra on grid

⭐⭐⭐ Hard but important

---

# Hard

### 6. Minimum Cost to Make at Least One Valid Path in a Grid
LeetCode #1368

Concept:
- 0-1 weighted Dijkstra

⭐⭐⭐ Top Interview Question

---

### 7. Reconstruct Itinerary (sometimes graph + priority queue)
LeetCode #332

Concept:
- Priority queue + DFS

---

# Must-Do Interview Questions

1. Network Delay Time (#743)
2. Path With Minimum Effort (#1631)
3. Cheapest Flights Within K Stops (#787)
4. Swim in Rising Water (#778)
5. Minimum Cost Path in Grid (#1368)

These questions cover the most important shortest path patterns using BFS + Dijkstra, which are very frequently asked in coding interviews.