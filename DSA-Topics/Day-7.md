# Binary Search Tree (BST)

## Definition

A Binary Search Tree (BST) is a special type of Binary Tree that follows a specific rule:

```text
Left Subtree < Root < Right Subtree
```

This property makes searching very efficient.

---

## Example

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4  7 13
```

Observe:

```text
All values left of 8 are smaller than 8.
All values right of 8 are greater than 8.
```

---

# BST Properties

For every node:

```text
Left Child < Node
Right Child > Node
```

This rule must be true for the entire tree.

---

# Why BST?

In a normal Binary Tree:

```text
Search = O(n)
```

In a BST:

```text
Search = O(log n)
```

(when the tree is balanced)

---

# Search in BST

## Example

Search for:

```text
7
```

Tree:

```text
        8
       / \
      3   10
     / \
    1   6
       / \
      4   7
```

---

### Steps

```text
7 < 8 → Go Left

7 > 3 → Go Right

7 > 6 → Go Right

Found 7
```

---

## Code

```cpp
TreeNode* search(TreeNode* root, int key)
{
    if(root == nullptr || root->val == key)
        return root;

    if(key < root->val)
        return search(root->left, key);

    return search(root->right, key);
}
```

---

## Time Complexity

Balanced BST:

```text
O(log n)
```

Worst Case:

```text
O(n)
```

---

# Insertion in BST

## Example

Insert:

```text
5
```

Tree:

```text
      8
     /
    3
```

---

### Steps

```text
5 < 8 → Left

5 > 3 → Right

Insert
```

Result:

```text
      8
     /
    3
     \
      5
```

---

# Deletion in BST

Deletion is one of the most important BST operations.

---

## Case 1: Leaf Node

Delete:

```text
4
```

```text
    5
   /
  4
```

Simply remove it.

---

## Case 2: Node With One Child

```text
    5
   /
  4
 /
2
```

Delete:

```text
4
```

Connect:

```text
5 → 2
```

---

## Case 3: Node With Two Children

Example:

```text
        8
       / \
      3   10
```

Delete:

```text
8
```

---

### Solution

Replace with:

```text
Inorder Successor
```

or

```text
Inorder Predecessor
```

---

# Inorder Traversal of BST

Very Important Property.

---

## Example

BST:

```text
        8
       / \
      3   10
     / \
    1   6
```

Inorder:

```text
1 3 6 8 10
```

Notice:

```text
Sorted Order
```

---

# Important BST Interview Trick

Whenever you see:

```text
BST
```

Think:

```text
Inorder Traversal = Sorted Sequence
```

This fact is used in many interview questions.

---

# AVL Tree

## Definition

AVL Tree is a self-balancing Binary Search Tree.

It automatically keeps itself balanced after insertions and deletions.

---

# Why AVL Tree?

Normal BST can become skewed.

Example:

Insert:

```text
1 2 3 4 5
```

Normal BST:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Looks like a linked list.

---

Search Complexity:

```text
O(n)
```

which is bad.

---

# AVL Solution

AVL Tree balances itself.

Result:

```text
        3
       / \
      2   4
     /     \
    1       5
```

---

Search Complexity:

```text
O(log n)
```

---

# Balance Factor

## Definition

```text
Balance Factor
=
Height(Left Subtree)
-
Height(Right Subtree)
```

---

### Example

```text
Left Height = 3

Right Height = 2
```

Balance Factor:

```text
1
```

---

# AVL Condition

For every node:

```text
-1 ≤ Balance Factor ≤ 1
```

If not:

```text
Rotation Required
```

---

# Rotations in AVL Tree

AVL uses rotations to maintain balance.

---

# 1. Right Rotation (LL Case)

Before:

```text
      30
     /
    20
   /
  10
```

After Rotation:

```text
      20
     /  \
   10   30
```

---

# 2. Left Rotation (RR Case)

Before:

```text
10
  \
   20
     \
      30
```

After:

```text
      20
     /  \
   10   30
```

---

# 3. Left Right Rotation (LR Case)

Combination of:

```text
Left Rotation
+
Right Rotation
```

---

# 4. Right Left Rotation (RL Case)

Combination of:

```text
Right Rotation
+
Left Rotation
```

---

# AVL Complexity

| Operation | Complexity |
|------------|------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

---

# Segment Tree

## Definition

A Segment Tree is a special tree used for range queries.

It helps answer queries efficiently on arrays.

---

# Why Segment Tree?

Suppose:

```text
Array:
1 3 5 7 9 11
```

Query:

```text
Sum from index 1 to 4
```

---

## Brute Force

```cpp
for(i=l;i<=r;i++)
```

Complexity:

```text
O(n)
```

---

If there are:

```text
100000 queries
```

This becomes very slow.

---

# Segment Tree Solution

Query Complexity:

```text
O(log n)
```

Update Complexity:

```text
O(log n)
```

---

# Segment Tree Structure

Array:

```text
1 3 5 7
```

Tree:

```text
           16
         /    \
        4      12
       / \    /  \
      1  3   5   7
```

Each node stores information about a range.

---

# Range Covered

```text
Node Root
=
[0,3]
```

Left Child:

```text
[0,1]
```

Right Child:

```text
[2,3]
```

---

# Segment Tree Applications

Used for:

- Range Sum Query
- Range Minimum Query
- Range Maximum Query
- Range XOR Query
- Frequency Queries

---

# Building Segment Tree

### Idea

Divide array into halves recursively.

Store answer of child nodes in parent.

---

### Complexity

```text
O(n)
```

---

# Query Operation

Find:

```text
Sum(L,R)
```

Only visit relevant nodes.

---

### Complexity

```text
O(log n)
```

---

# Update Operation

Change:

```text
arr[i] = newValue
```

Update only affected nodes.

---

### Complexity

```text
O(log n)
```

---

# When Should You Use Segment Tree?

Use when:

- Multiple range queries exist.
- Array values change frequently.
- Need fast updates and queries.

---

# Difference Between Prefix Sum and Segment Tree

| Feature | Prefix Sum | Segment Tree |
|----------|------------|-------------|
| Query | O(1) | O(log n) |
| Update | O(n) | O(log n) |
| Dynamic Updates | Poor | Excellent |

---

# Interview Tips

### Use BST When

- Data needs ordered storage.
- Searching is frequent.

---

### Use AVL When

- Guaranteed O(log n) operations are required.
- Tree must stay balanced.

---

### Use Segment Tree When

- Range Queries + Updates are involved.

---

# Important LeetCode Questions

## BST Questions

### 1. Search in a Binary Search Tree
LeetCode #700

Concept:
- BST Search

⭐⭐ Must Do

---

### 2. Insert into a Binary Search Tree
LeetCode #701

Concept:
- BST Insertion

---

### 3. Validate Binary Search Tree
LeetCode #98

Concept:
- BST Properties

⭐⭐⭐ Very Important

---

### 4. Kth Smallest Element in BST
LeetCode #230

Concept:
- Inorder Traversal

⭐⭐ Frequently Asked

---

### 5. Lowest Common Ancestor of BST
LeetCode #235

Concept:
- BST Optimization

⭐⭐ Must Do

---

# AVL Related Practice

AVL is rarely asked directly on LeetCode.

Instead practice:

- Tree Height
- Balanced Binary Tree
- BST Insert/Delete

---

### 6. Balanced Binary Tree
LeetCode #110

Concept:
- AVL Idea

⭐⭐ Important

---

# Segment Tree Questions

### 7. Range Sum Query - Mutable
LeetCode #307

Concept:
- Segment Tree

⭐⭐⭐ Must Do

---

### 8. Range Minimum Query
(Common Segment Tree Pattern)

---

### 9. Count of Smaller Numbers After Self
LeetCode #315

Concept:
- Segment Tree / BIT

⭐⭐ Frequently Asked

---

### 10. My Calendar I
LeetCode #729

Concept:
- Segment Tree Concept

---

# Must-Do Interview Questions

1. Search in BST (#700)
2. Validate BST (#98)
3. Kth Smallest Element in BST (#230)
4. Lowest Common Ancestor of BST (#235)
5. Balanced Binary Tree (#110)
6. Range Sum Query - Mutable (#307)
7. Count of Smaller Numbers After Self (#315)

These questions cover the most important BST, AVL Tree concepts, and Segment Tree fundamentals commonly asked in coding interviews.