# Trees Fundamentals

## Definition

A Tree is a hierarchical data structure made up of nodes connected by edges.

Unlike arrays and linked lists (which are linear), trees store data in a hierarchical structure.

---

## Real Life Example

Think of a family tree:

```text
Grandfather
   /    \
 Father  Uncle
  /
You
```

This is a tree structure.

---

# Basic Terminology

Consider the following tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

---

## Root Node

The topmost node of the tree.

```text
1
```

is the root node.

---

## Parent Node

A node having child nodes.

Example:

```text
1
```

is parent of:

```text
2 and 3
```

---

## Child Node

Nodes connected below a parent.

Example:

```text
2 and 3
```

are children of:

```text
1
```

---

## Leaf Node

A node with no children.

Example:

```text
4, 5, 3
```

---

## Sibling Nodes

Nodes having the same parent.

Example:

```text
2 and 3
```

---

## Edge

Connection between two nodes.

Example:

```text
1 → 2
```

is an edge.

---

## Depth

Number of edges from root to a node.

Example:

```text
Depth(1) = 0
Depth(2) = 1
Depth(4) = 2
```

---

## Height of Tree

Number of edges in the longest path from root to leaf.

Example:

```text
        1
       / \
      2   3
     /
    4
```

Height = 2

---

# Why Trees?

Trees are used in:

- File Systems
- Databases
- Search Engines
- Operating Systems
- Hierarchical Data Storage
- Compilers

---

# Binary Tree

## Definition

A Binary Tree is a tree where each node can have at most:

```text
2 children
```

They are called:

```text
Left Child
Right Child
```

---

## Example

```text
        1
       / \
      2   3
     / \
    4   5
```

This is a Binary Tree.

---

# Binary Tree Node Structure

## C++ Code

```cpp
class TreeNode
{
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int data)
    {
        val = data;
        left = nullptr;
        right = nullptr;
    }
};
```

---

# Types of Binary Trees

---

## 1. Full Binary Tree

Every node has either:

```text
0 children
or
2 children
```

Example:

```text
      1
     / \
    2   3
```

---

## 2. Perfect Binary Tree

All leaf nodes are at the same level.

Every internal node has 2 children.

Example:

```text
        1
       / \
      2   3
     / \ / \
    4 5 6 7
```

---

## 3. Complete Binary Tree

All levels are completely filled except possibly the last level.

Last level is filled from left to right.

Example:

```text
        1
       / \
      2   3
     / \ /
    4 5 6
```

---

## 4. Skewed Binary Tree

Every node has only one child.

Example:

```text
1
 \
  2
   \
    3
     \
      4
```

Looks like a linked list.

---

# Tree Traversals

## Definition

Traversal means visiting every node exactly once.

---

# Types of Traversals

There are two main categories:

### DFS (Depth First Search)

- Preorder
- Inorder
- Postorder

### BFS (Breadth First Search)

- Level Order Traversal

---

# DFS Traversals

---

## 1. Preorder Traversal

### Rule

```text
Root
Left
Right
```

---

### Example

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

Traversal:

```text
1 2 4 5 3
```

---

## Code

```cpp
void preorder(TreeNode* root)
{
    if(root == nullptr)
        return;

    cout << root->val << " ";

    preorder(root->left);

    preorder(root->right);
}
```

---

## Time Complexity

```text
O(n)
```

---

# 2. Inorder Traversal

## Rule

```text
Left
Root
Right
```

---

### Example

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

Traversal:

```text
4 2 5 1 3
```

---

## Code

```cpp
void inorder(TreeNode* root)
{
    if(root == nullptr)
        return;

    inorder(root->left);

    cout << root->val << " ";

    inorder(root->right);
}
```

---

## Time Complexity

```text
O(n)
```

---

# 3. Postorder Traversal

## Rule

```text
Left
Right
Root
```

---

### Example

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

Traversal:

```text
4 5 2 3 1
```

---

## Code

```cpp
void postorder(TreeNode* root)
{
    if(root == nullptr)
        return;

    postorder(root->left);

    postorder(root->right);

    cout << root->val << " ";
}
```

---

## Time Complexity

```text
O(n)
```

---

# Easy Way to Remember

For a node:

```text
      Root
      /  \
   Left Right
```

### Preorder

```text
Root Left Right
```

---

### Inorder

```text
Left Root Right
```

---

### Postorder

```text
Left Right Root
```

---

# Level Order Traversal (BFS)

## Definition

Visit nodes level by level.

---

### Example

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text
1 2 3 4 5
```

---

# Why Queue?

BFS processes nodes in FIFO order.

Queue is perfect for this.

---

## Code

```cpp
void levelOrder(TreeNode* root)
{
    if(root == nullptr)
        return;

    queue<TreeNode*> q;

    q.push(root);

    while(!q.empty())
    {
        TreeNode* node = q.front();
        q.pop();

        cout << node->val << " ";

        if(node->left)
            q.push(node->left);

        if(node->right)
            q.push(node->right);
    }
}
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

---

# Recursive Nature of Trees

One of the most important concepts.

Every subtree is itself a tree.

Example:

```text
        1
       / \
      2   3
```

Node 2 forms a tree.

Node 3 forms a tree.

Because of this property, recursion is heavily used in tree problems.

---

# Common Tree Interview Questions

Most tree problems are based on:

- Traversals
- Recursion
- Height
- Diameter
- Balanced Trees
- Path Problems
- Lowest Common Ancestor (LCA)

You will study these in advanced tree topics.

---

# Important LeetCode Questions

## Easy

### 1. Binary Tree Inorder Traversal
LeetCode #94

Concept:
- Inorder Traversal

⭐⭐ Must Do

---

### 2. Binary Tree Preorder Traversal
LeetCode #144

Concept:
- Preorder Traversal

---

### 3. Binary Tree Postorder Traversal
LeetCode #145

Concept:
- Postorder Traversal

---

### 4. Maximum Depth of Binary Tree
LeetCode #104

Concept:
- Recursion

⭐⭐ Must Do

---

### 5. Same Tree
LeetCode #100

Concept:
- Tree Comparison

---

# Medium

### 6. Binary Tree Level Order Traversal
LeetCode #102

Concept:
- BFS

⭐⭐⭐ Very Important

---

### 7. Binary Tree Right Side View
LeetCode #199

Concept:
- Level Order Traversal

---

### 8. Count Good Nodes in Binary Tree
LeetCode #1448

Concept:
- DFS

---

### 9. Path Sum II
LeetCode #113

Concept:
- DFS + Backtracking

---

### 10. Zigzag Level Order Traversal
LeetCode #103

Concept:
- BFS

---

# Hard

### 11. Serialize and Deserialize Binary Tree
LeetCode #297

Concept:
- DFS / BFS

⭐⭐⭐ Frequently Asked

---

### 12. Binary Tree Maximum Path Sum
LeetCode #124

Concept:
- Advanced DFS

⭐⭐⭐ Top Interview Question

---

# Must-Do Interview Questions

1. Binary Tree Inorder Traversal (#94)
2. Binary Tree Preorder Traversal (#144)
3. Binary Tree Postorder Traversal (#145)
4. Maximum Depth of Binary Tree (#104)
5. Same Tree (#100)
6. Binary Tree Level Order Traversal (#102)
7. Zigzag Level Order Traversal (#103)
8. Binary Tree Right Side View (#199)
9. Serialize and Deserialize Binary Tree (#297)
10. Binary Tree Maximum Path Sum (#124)

These questions cover the most important Tree Fundamentals, Traversals, DFS, and BFS patterns commonly asked in coding interviews.