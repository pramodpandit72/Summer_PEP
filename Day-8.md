# Heap

## Definition

A Heap is a special type of Complete Binary Tree that follows a specific property.

Heaps are mainly used to efficiently find:

- Largest element
- Smallest element
- Top K elements
- Priority-based processing

---

# Complete Binary Tree

Before understanding Heap, know this:

A Complete Binary Tree is a tree where:

- All levels are completely filled except possibly the last level.
- Last level is filled from left to right.

Example:

```text
        10
       /  \
      20   30
     / \
    40 50
```

This is a Complete Binary Tree.

---

# Types of Heap

There are two types:

## 1. Max Heap

### Property

Parent is always greater than or equal to its children.

```text
Parent >= Children
```

Example:

```text
        50
       /  \
      30   40
     / \   /
    10 20 35
```

Notice:

```text
50 > 30,40
30 > 10,20
40 > 35
```

Largest element is always at the root.

---

## 2. Min Heap

### Property

Parent is always smaller than or equal to its children.

```text
Parent <= Children
```

Example:

```text
        10
       /  \
      20   30
     / \   /
    40 50 35
```

Smallest element is always at the root.

---

# Heap Representation

Heaps are usually stored in arrays.

Example:

```text
        10
       /  \
      20   30
     / \
    40 50
```

Array:

```text
[10,20,30,40,50]
```

---

# Parent and Child Formula

For index i:

### Left Child

```text
2*i + 1
```

### Right Child

```text
2*i + 2
```

### Parent

```text
(i-1)/2
```

---

# Heap Operations

---

## Insert

Add a new element.

After insertion:

```text
Heapify Up
```

to maintain heap property.

---

### Example

Insert:

```text
60
```

```text
        50
       /  \
      30   40
```

After insertion:

```text
        60
       /  \
      50   40
     /
    30
```

---

## Time Complexity

```text
O(log n)
```

---

# Delete Root

Remove:

- Largest element in Max Heap
- Smallest element in Min Heap

After deletion:

```text
Heapify Down
```

---

## Time Complexity

```text
O(log n)
```

---

# Peek

Access root element.

---

### Time Complexity

```text
O(1)
```

---

# Priority Queue

## Definition

Priority Queue is a data structure built using Heap.

Elements are processed according to priority rather than insertion order.

---

# STL Priority Queue

Include:

```cpp
#include <queue>
```

---

## Max Heap (Default)

```cpp
priority_queue<int> pq;
```

---

### Example

```cpp
pq.push(10);
pq.push(50);
pq.push(20);

cout << pq.top();
```

Output:

```text
50
```

Largest element appears first.

---

# Common Operations

### Insert

```cpp
pq.push(x);
```

---

### Remove Top

```cpp
pq.pop();
```

---

### Top Element

```cpp
pq.top();
```

---

### Size

```cpp
pq.size();
```

---

### Empty

```cpp
pq.empty();
```

---

# Min Heap in C++

## Syntax

```cpp
priority_queue<
    int,
    vector<int>,
    greater<int>
> pq;
```

---

### Example

```cpp
pq.push(10);
pq.push(5);
pq.push(20);
```

Top:

```text
5
```

Smallest element appears first.

---

# Complexity of Priority Queue

| Operation | Complexity |
|------------|------------|
| Push | O(log n) |
| Pop | O(log n) |
| Top | O(1) |

---

# Top-K Problems

## Definition

Top-K Problems ask us to find:

```text
K largest elements
```

or

```text
K smallest elements
```

efficiently.

These are extremely common in interviews.

---

# Why Not Sort?

Example:

```text
n = 100000
k = 10
```

Sorting:

```text
O(n log n)
```

Expensive.

---

Heap Solution:

```text
O(n log k)
```

Much better.

---

# Pattern 1: K Largest Elements

## Problem

Find:

```text
3 largest elements
```

Array:

```text
1 5 12 2 11 7
```

Answer:

```text
12 11 7
```

---

## Approach

Use Min Heap of size K.

### Steps

1. Insert element.
2. If heap size exceeds K:
   remove smallest element.

At the end:

Heap contains K largest elements.

---

## Complexity

```text
O(n log k)
```

---

# Pattern 2: K Smallest Elements

## Approach

Use Max Heap of size K.

---

### Example

```text
1 5 12 2 11 7
```

K = 3

Answer:

```text
1 2 5
```

---

## Complexity

```text
O(n log k)
```

---

# Pattern 3: Kth Largest Element

## Example

```text
3 2 1 5 6 4
```

K = 2

Answer:

```text
5
```

---

## Approach

Maintain Min Heap of size K.

Top element becomes answer.

---

### LeetCode

```text
#215 Kth Largest Element in an Array
```

---

# Pattern 4: Kth Smallest Element

Use Max Heap of size K.

---

# Pattern 5: Top K Frequent Elements

## Example

```text
1 1 1 2 2 3
```

K = 2

Answer:

```text
1 2
```

---

## Steps

### Step 1

Store frequencies using HashMap.

```cpp
unordered_map<int,int>
```

---

### Step 2

Use Heap based on frequency.

---

### LeetCode

```text
#347 Top K Frequent Elements
```

---

# Pattern 6: Top K Frequent Words

Same idea as frequency elements.

---

### LeetCode

```text
#692 Top K Frequent Words
```

---

# Pattern 7: Merge K Sorted Lists

Very popular interview question.

---

### Idea

Keep smallest node from each list inside Min Heap.

Always process minimum element.

---

### LeetCode

```text
#23 Merge K Sorted Lists
```

---

# Pattern 8: K Closest Points to Origin

## Example

Points:

```text
(1,3)
(-2,2)
```

K = 1

Answer:

```text
(-2,2)
```

because distance is smaller.

---

### LeetCode

```text
#973 K Closest Points to Origin
```

---

# Pattern 9: K Closest Elements

Given sorted array.

Find K closest numbers.

---

### LeetCode

```text
#658 Find K Closest Elements
```

---

# Pattern 10: Median from Data Stream

Very Important Interview Question.

---

## Idea

Use:

### Max Heap

Stores smaller half.

### Min Heap

Stores larger half.

---

Result:

Median can be found quickly.

---

### LeetCode

```text
#295 Find Median from Data Stream
```

---

# How to Identify Heap Problems?

Look for words like:

- K Largest
- K Smallest
- Top K
- Highest Priority
- Closest Elements
- Closest Points
- Stream Data
- Running Median

These are strong hints.

---

# Heap vs Sorting

| Feature | Heap | Sorting |
|----------|---------|---------|
| Top K | Better | Slower |
| Entire Order Needed | No | Yes |
| Complexity | O(n log k) | O(n log n) |

---

# Interview Tips

### Use Heap When

- Need largest element repeatedly.
- Need smallest element repeatedly.
- Need Top K results.
- Need priority-based processing.

---

### Use Min Heap When

- Need smallest value first.
- Need K largest elements.

---

### Use Max Heap When

- Need largest value first.
- Need K smallest elements.

---

# Important LeetCode Questions

## Easy

### 1. Last Stone Weight
LeetCode #1046

Concept:
- Max Heap

⭐⭐ Must Do

---

### 2. Kth Largest Element in a Stream
LeetCode #703

Concept:
- Min Heap

⭐⭐ Important

---

# Medium

### 3. Kth Largest Element in an Array
LeetCode #215

Concept:
- Top K

⭐⭐⭐ Must Do

---

### 4. Top K Frequent Elements
LeetCode #347

Concept:
- Heap + HashMap

⭐⭐⭐ Very Important

---

### 5. K Closest Points to Origin
LeetCode #973

Concept:
- Heap

⭐⭐ Frequently Asked

---

### 6. Find K Closest Elements
LeetCode #658

Concept:
- Heap / Binary Search

---

### 7. Task Scheduler
LeetCode #621

Concept:
- Priority Queue

⭐⭐ Interview Favorite

---

### 8. Sort Characters By Frequency
LeetCode #451

Concept:
- Heap

---

# Hard

### 9. Find Median from Data Stream
LeetCode #295

Concept:
- Two Heaps

⭐⭐⭐ Top Interview Question

---

### 10. Merge K Sorted Lists
LeetCode #23

Concept:
- Min Heap

⭐⭐⭐ Must Do

---

### 11. Sliding Window Median
LeetCode #480

Concept:
- Advanced Heap

---

# Must-Do Interview Questions

1. Last Stone Weight (#1046)
2. Kth Largest Element in Array (#215)
3. Top K Frequent Elements (#347)
4. K Closest Points to Origin (#973)
5. Task Scheduler (#621)
6. Merge K Sorted Lists (#23)
7. Find Median from Data Stream (#295)
8. Kth Largest Element in Stream (#703)

These questions cover almost all important Heap, Priority Queue, and Top-K patterns asked in coding interviews.