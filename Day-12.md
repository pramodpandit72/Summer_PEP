# Graphs III – MST (Minimum Spanning Tree) & DSU (Union Find)

---

# Spanning Tree

## Definition

A Spanning Tree of a graph is:

```text
A subgraph that includes all vertices
AND
is connected
AND
has no cycles
```

---

## Key Points

- Contains all nodes
- Has exactly:

```text
V - 1 edges
```

- No cycles

---

## Example

Graph:

```text
A --- B
|   / |
|  /  |
C --- D
```

A spanning tree:

```text
A --- B
|
C --- D
```

---

# Minimum Spanning Tree (MST)

## Definition

A Minimum Spanning Tree is a spanning tree with:

```text
Minimum total edge weight
```

---

## Where Used?

- Network design (cables, roads)
- Cost minimization
- Clustering problems

---

# MST Algorithms

There are two main algorithms:

---

## 1. Kruskal’s Algorithm (Most Important)

## 2. Prim’s Algorithm

We will focus more on Kruskal + DSU (very important for interviews)

---

# Kruskal’s Algorithm

## Idea

- Sort edges by weight
- Pick smallest edge
- Avoid cycles using DSU

---

# Steps of Kruskal

### Step 1

Sort all edges by weight.

---

### Step 2

Pick edges one by one.

---

### Step 3

If adding edge does NOT form a cycle → include it.

Else → skip it.

---

# Why DSU?

We need to detect cycles efficiently.

DSU helps answer:

```text
Are two nodes already connected?
```

---

# DSU (Disjoint Set Union)

## Definition

DSU is a data structure used to manage disjoint sets.

It supports:

- Union (merge sets)
- Find (find parent of set)

---

# Basic Idea

Each node belongs to a group.

We merge groups when needed.

---

# DSU Operations

---

## 1. Find Parent

Find representative of a node.

---

## 2. Union

Merge two sets.

---

# DSU with Path Compression

## Optimization

Flattens tree structure.

So future queries become faster.

---

# DSU Code (C++)

```cpp
class DSU
{
public:
    vector<int> parent, rank;

    DSU(int n)
    {
        parent.resize(n);
        rank.resize(n, 0);

        for(int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x)
    {
        if(parent[x] == x)
            return x;

        return parent[x] = find(parent[x]);
    }

    void unite(int a, int b)
    {
        int pa = find(a);
        int pb = find(b);

        if(pa == pb)
            return;

        if(rank[pa] < rank[pb])
            parent[pa] = pb;

        else if(rank[pa] > rank[pb])
            parent[pb] = pa;

        else
        {
            parent[pb] = pa;
            rank[pa]++;
        }
    }
};
```

---

# Time Complexity

Almost constant:

```text
O(α(n)) ≈ O(1)
```

(α is inverse Ackermann function)

---

# Kruskal Algorithm Code

```cpp
int spanningTree(int V,
                 vector<vector<int>> edges)
{
    DSU dsu(V);

    sort(edges.begin(), edges.end(),
        [](auto &a, auto &b)
        {
            return a[2] < b[2];
        });

    int mstWeight = 0;

    for(auto &e : edges)
    {
        int u = e[0];
        int v = e[1];
        int w = e[2];

        if(dsu.find(u) != dsu.find(v))
        {
            dsu.unite(u, v);
            mstWeight += w;
        }
    }

    return mstWeight;
}
```

---

# Time Complexity

```text
O(E log E)
```

(for sorting edges)

---

# Prim’s Algorithm

## Idea

Start from any node and grow MST step by step.

Always pick:

```text
Minimum weight edge from visited set
```

---

# Data Structure

```text
Min Heap (Priority Queue)
```

---

# Prim’s Algorithm Code

```cpp
int prim(int V,
         vector<pair<int,int>> adj[])
{
    vector<int> vis(V, 0);

    priority_queue<
        pair<int,int>,
        vector<pair<int,int>>,
        greater<pair<int,int>>
    > pq;

    pq.push({0, 0});

    int sum = 0;

    while(!pq.empty())
    {
        auto it = pq.top();
        pq.pop();

        int wt = it.first;
        int node = it.second;

        if(vis[node])
            continue;

        vis[node] = 1;
        sum += wt;

        for(auto nbr : adj[node])
        {
            int adjNode = nbr.first;
            int edgeWt = nbr.second;

            if(!vis[adjNode])
                pq.push({edgeWt, adjNode});
        }
    }

    return sum;
}
```

---

# Kruskal vs Prim

| Feature | Kruskal | Prim |
|----------|---------|------|
| Strategy | Edge-based | Node-based |
| Data Structure | DSU | Heap |
| Best for | Sparse graph | Dense graph |
| Complexity | O(E log E) | O(E log V) |

---

# DSU Applications

---

## 1. Cycle Detection in Graph

If:

```text
find(u) == find(v)
```

Cycle exists.

---

## 2. Connected Components

Count number of unique parents.

---

## 3. Kruskal MST

Main use case.

---

## 4. Dynamic Connectivity

Online graph queries.

---

# Important Patterns

Whenever you see:

- Connect components
- Merge groups
- Check cycle
- Minimum cost connections

Think:

```text
DSU + Kruskal
```

---

# MST Real-Life Analogy

Imagine:

```text
Connecting cities with minimum cable cost
```

Goal:

- Connect all cities
- Minimum cost
- No cycles

---

# Important LeetCode Questions

---

## Easy

### 1. Find if Path Exists in Graph
LeetCode #1971

Concept:
- DSU

⭐⭐ Must Do

---

## Medium

### 2. Number of Provinces
LeetCode #547

Concept:
- DSU / DFS

⭐⭐⭐ Must Do

---

### 3. Redundant Connection
LeetCode #684

Concept:
- Cycle Detection using DSU

⭐⭐⭐ Very Important

---

### 4. Accounts Merge
LeetCode #721

Concept:
- DSU + Strings

⭐⭐⭐ Interview Favorite

---

### 5. Most Stones Removed with Same Row or Column
LeetCode #947

Concept:
- DSU

---

# MST Problems

### 6. Min Cost to Connect All Points
LeetCode #1584

Concept:
- Kruskal / Prim

⭐⭐⭐ Must Do

---

### 7. Connecting Cities With Minimum Cost
Similar MST pattern

---

# Hard

### 8. Optimize Water Distribution in a Village
LeetCode #1168

Concept:
- MST + DSU

⭐⭐⭐ Top Interview Question

---

# Must-Do Interview Questions

1. Number of Provinces (#547)
2. Redundant Connection (#684)
3. Accounts Merge (#721)
4. Min Cost to Connect All Points (#1584)
5. Most Stones Removed (#947)
6. Optimize Water Distribution (#1168)

These questions cover the most important DSU, Kruskal, Prim, and MST patterns used in coding interviews.