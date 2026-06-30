# Graphs IV – Topological Sort & SCC (Strongly Connected Components)

---

# Topological Sort

## Definition

Topological Sort is a linear ordering of nodes in a **Directed Acyclic Graph (DAG)** such that:

```text
For every directed edge u → v,
u appears before v in the ordering
```

---

## Important Condition

Topological Sort is only possible if:

```text
Graph has NO cycles (DAG only)
```

---

## Example

```text
5 → 0 → 2 → 3
     ↓
     1
```

One valid topological order:

```text
5 4 0 2 3 1
```

(There can be multiple correct answers)

---

# Where Topological Sort is Used

- Course prerequisites
- Task scheduling
- Build systems (Makefiles)
- Dependency resolution
- Compiler ordering

---

# Method 1: Kahn’s Algorithm (BFS)

## Idea

Use **indegree (incoming edges count)**.

Nodes with indegree 0 come first.

---

## Steps

### Step 1: Compute indegree

```text
indegree[v] = number of incoming edges
```

---

### Step 2: Push all indegree 0 nodes into queue

---

### Step 3: Process queue

- Pop node
- Add to answer
- Reduce indegree of neighbors
- If indegree becomes 0 → push to queue

---

## Code (Kahn’s Algorithm)

```cpp
vector<int> topoSort(int V, vector<int> adj[])
{
    vector<int> indegree(V, 0);

    for(int i = 0; i < V; i++)
    {
        for(auto it : adj[i])
            indegree[it]++;
    }

    queue<int> q;

    for(int i = 0; i < V; i++)
    {
        if(indegree[i] == 0)
            q.push(i);
    }

    vector<int> topo;

    while(!q.empty())
    {
        int node = q.front();
        q.pop();

        topo.push_back(node);

        for(auto it : adj[node])
        {
            indegree[it]--;

            if(indegree[it] == 0)
                q.push(it);
        }
    }

    return topo;
}
```

---

## Time Complexity

```text
O(V + E)
```

---

## Cycle Detection Trick

If:

```text
topo.size() != V
```

👉 Graph has a cycle

---

# Method 2: DFS Based Topological Sort

## Idea

- Go deep first
- Push node after visiting all neighbors
- Reverse the result

---

## Code

```cpp
void dfs(int node,
         vector<int> adj[],
         vector<int>& vis,
         stack<int>& st)
{
    vis[node] = 1;

    for(auto it : adj[node])
    {
        if(!vis[it])
            dfs(it, adj, vis, st);
    }

    st.push(node);
}

vector<int> topoSort(int V, vector<int> adj[])
{
    vector<int> vis(V, 0);
    stack<int> st;

    for(int i = 0; i < V; i++)
    {
        if(!vis[i])
            dfs(i, adj, vis, st);
    }

    vector<int> topo;

    while(!st.empty())
    {
        topo.push_back(st.top());
        st.pop();
    }

    return topo;
}
```

---

## Time Complexity

```text
O(V + E)
```

---

# BFS vs DFS Toposort

| Method | Idea | Data Structure |
|--------|------|---------------|
| Kahn’s Algorithm | indegree (BFS) | Queue |
| DFS Method | postorder | Stack |

---

# Strongly Connected Components (SCC)

---

## Definition

A Strongly Connected Component is a subgraph where:

```text
Every node is reachable from every other node
```

(Directed graph only)

---

## Example

```text
1 → 2 → 3
↑    ↓
4 ←———
```

SCC = {1,2,3,4}

---

## Another Example

```text
1 → 2 → 3

4 → 5
```

SCCs:

```text
{1}, {2}, {3}, {4,5}
```

---

# Why SCC?

Used in:

- Social networks (mutual connections)
- Web pages linking
- Deadlock detection
- Dependency cycles
- Graph compression

---

# Kosaraju’s Algorithm (Most Important SCC Algorithm)

---

## Idea

We do 3 steps:

---

## Step 1: Topological Order (DFS finish time)

Store nodes in stack based on finish time.

---

## Step 2: Reverse Graph

Reverse all edges.

---

## Step 3: DFS on reversed graph

Process nodes in stack order.

Each DFS = one SCC

---

# Kosaraju Code

```cpp
void dfs1(int node,
          vector<int> adj[],
          vector<int>& vis,
          stack<int>& st)
{
    vis[node] = 1;

    for(auto it : adj[node])
    {
        if(!vis[it])
            dfs1(it, adj, vis, st);
    }

    st.push(node);
}
```

---

## Reverse Graph

```cpp
vector<int> rev[V];

for(int i = 0; i < V; i++)
{
    for(auto it : adj[i])
    {
        rev[it].push_back(i);
    }
}
```

---

## Second DFS

```cpp
void dfs2(int node,
          vector<int> rev[],
          vector<int>& vis)
{
    vis[node] = 1;

    for(auto it : rev[node])
    {
        if(!vis[it])
            dfs2(it, rev, vis);
    }
}
```

---

## Full Kosaraju

```cpp
int kosaraju(int V, vector<int> adj[])
{
    vector<int> vis(V, 0);
    stack<int> st;

    for(int i = 0; i < V; i++)
    {
        if(!vis[i])
            dfs1(i, adj, vis, st);
    }

    vector<int> rev[V];

    for(int i = 0; i < V; i++)
    {
        for(auto it : adj[i])
            rev[it].push_back(i);
    }

    fill(vis.begin(), vis.end(), 0);

    int countSCC = 0;

    while(!st.empty())
    {
        int node = st.top();
        st.pop();

        if(!vis[node])
        {
            dfs2(node, rev, vis);
            countSCC++;
        }
    }

    return countSCC;
}
```

---

## Time Complexity

```text
O(V + E)
```

---

# Intuition Behind Kosaraju

1. First DFS gives finishing order
2. Reverse graph flips directions
3. Second DFS finds components

---

# Strongly Connected Components vs Connected Components

| Feature | SCC | Connected Components |
|--------|-----|---------------------|
| Graph Type | Directed | Undirected |
| Reachability | Two-way | One-way |
| Algorithm | Kosaraju / Tarjan | DFS / BFS |

---

# Important Graph Patterns

Whenever you see:

- Dependencies
- Ordering tasks
- Cycles in directed graph
- Build sequence
- Course schedule

Think:

```text
Topological Sort
```

---

When you see:

- Mutual reachability
- Cycle groups
- Graph compression
- Directed cycles

Think:

```text
SCC (Kosaraju / Tarjan)
```

---

# Important LeetCode Questions

---

## Topological Sort

### 1. Course Schedule
LeetCode #207

Concept:
- Cycle detection + Kahn

⭐⭐⭐ Must Do

---

### 2. Course Schedule II
LeetCode #210

Concept:
- Topological Order

⭐⭐⭐ Very Important

---

### 3. Alien Dictionary
LeetCode #269

Concept:
- Toposort on custom graph

---

### 4. Parallel Courses
LeetCode #1136

Concept:
- BFS Toposort

---

# SCC / Advanced Graph

### 5. Critical Connections in a Network
LeetCode #1192

Concept:
- Bridge + SCC idea

⭐⭐⭐ Hard

---

### 6. Minimum Height Trees
LeetCode #310

Concept:
- Graph layering

---

# Must-Do Interview Questions

1. Course Schedule (#207)
2. Course Schedule II (#210)
3. Alien Dictionary (#269)
4. Parallel Courses (#1136)
5. Critical Connections (#1192)

These cover the most important Topological Sort and SCC concepts used in interviews and competitive programming.
```