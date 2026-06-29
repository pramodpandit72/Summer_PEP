# Stacks

## Definition

A Stack is a linear data structure that follows the:

```text
LIFO (Last In First Out)
```

This means:

- The last element inserted is removed first.
- The first element inserted is removed last.

---

## Real Life Example

Think of a stack of plates.

```text
Plate 3  <- Top
Plate 2
Plate 1
```

If you remove a plate, you remove the top plate first.

---

## Stack Operations

### Push

Insert an element.

```cpp
st.push(10);
```

---

### Pop

Remove the top element.

```cpp
st.pop();
```

---

### Top

Access the top element.

```cpp
st.top();
```

---

### Empty

Check whether stack is empty.

```cpp
st.empty();
```

---

### Size

Get number of elements.

```cpp
st.size();
```

---

## STL Stack

```cpp
#include <stack>

stack<int> st;
```

---

## Example

```cpp
stack<int> st;

st.push(10);
st.push(20);
st.push(30);

cout << st.top();
```

Output:

```text
30
```

---

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Top | O(1) |
| Empty | O(1) |

---

# Applications of Stack

- Function Calls
- Undo Operations
- Browser History
- Expression Evaluation
- Parentheses Matching
- Next Greater Element
- Monotonic Stack Problems

---

# Queues

## Definition

A Queue is a linear data structure that follows:

```text
FIFO (First In First Out)
```

This means:

- First inserted element is removed first.
- Last inserted element is removed last.

---

## Real Life Example

Queue at a ticket counter.

```text
A -> B -> C -> D
```

A came first.

A will leave first.

---

# Queue Operations

### Push

Insert at rear.

```cpp
q.push(10);
```

---

### Pop

Remove from front.

```cpp
q.pop();
```

---

### Front

Access first element.

```cpp
q.front();
```

---

### Back

Access last element.

```cpp
q.back();
```

---

## STL Queue

```cpp
#include <queue>

queue<int> q;
```

---

## Example

```cpp
queue<int> q;

q.push(10);
q.push(20);
q.push(30);

cout << q.front();
```

Output:

```text
10
```

---

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Front | O(1) |
| Back | O(1) |

---

# Deque (Double Ended Queue)

## Definition

A deque allows insertion and deletion from both ends.

---

## STL

```cpp
deque<int> dq;
```

---

### Operations

```cpp
dq.push_front(10);

dq.push_back(20);

dq.pop_front();

dq.pop_back();
```

---

# Priority Queue

## Definition

A Priority Queue always keeps the highest priority element at the top.

In C++:

```cpp
priority_queue<int> pq;
```

By default:

```text
Max Heap
```

---

## Example

```cpp
pq.push(10);
pq.push(50);
pq.push(20);
```

Top:

```text
50
```

---

## Min Heap

```cpp
priority_queue<
    int,
    vector<int>,
    greater<int>
> pq;
```

---

# Monotonic Stack

## Definition

A Monotonic Stack is a stack whose elements remain in increasing or decreasing order.

It is mainly used to find:

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element

efficiently.

---

# Why Monotonic Stack?

Consider:

```text
4 5 2 10 8
```

Find next greater element for every number.

Brute Force:

```text
O(n²)
```

Monotonic Stack:

```text
O(n)
```

---

# Increasing Monotonic Stack

Elements remain in increasing order.

Example:

```text
1 3 5 7
```

Before inserting a smaller value:

Pop larger elements if needed.

---

# Decreasing Monotonic Stack

Elements remain in decreasing order.

Example:

```text
9 7 5 3
```

Before inserting a larger value:

Pop smaller elements.

---

# Next Greater Element (NGE)

## Problem

For every element, find the first greater element on the right.

---

## Example

```text
Array:
4 5 2 10 8
```

Output:

```text
5 10 10 -1 -1
```

---

## Brute Force

For each element:

Search right side.

Complexity:

```text
O(n²)
```

---

## Monotonic Stack Approach

### Idea

Traverse from right to left.

Remove all smaller elements.

Top becomes answer.

---

## Code

```cpp
vector<int> ans(n);

stack<int> st;

for(int i = n - 1; i >= 0; i--)
{
    while(!st.empty() &&
          st.top() <= arr[i])
    {
        st.pop();
    }

    if(st.empty())
        ans[i] = -1;
    else
        ans[i] = st.top();

    st.push(arr[i]);
}
```

---

## Time Complexity

```text
O(n)
```

---

# Next Smaller Element (NSE)

## Problem

Find first smaller element on the right.

---

### Example

```text
4 5 2 10 8
```

Output:

```text
2 2 -1 8 -1
```

---

## Idea

Use increasing monotonic stack.

---

# Previous Greater Element (PGE)

## Problem

Find first greater element on left.

---

### Example

```text
4 5 2 10 8
```

Output:

```text
-1 -1 5 -1 10
```

---

# Previous Smaller Element (PSE)

## Problem

Find first smaller element on left.

---

### Example

```text
4 5 2 10 8
```

Output:

```text
-1 4 -1 2 2
```

---

# How to Identify Monotonic Stack Problems?

Look for phrases like:

- Next Greater
- Next Smaller
- Previous Greater
- Previous Smaller
- Nearest Greater
- Nearest Smaller
- First Larger on Left/Right

These are direct hints.

---

# Largest Rectangle in Histogram

## Very Important Interview Problem

### Example

```text
2 1 5 6 2 3
```

---

## Goal

Find largest rectangular area.

---

## Concept

For every bar:

Find:

- Previous Smaller Element
- Next Smaller Element

Width:

```text
right - left - 1
```

Area:

```text
height × width
```

---

### LeetCode

```text
#84 Largest Rectangle in Histogram
```

---

# Trapping Rain Water

## Idea

Store:

- Left Maximum
- Right Maximum

Water:

```text
min(leftMax,rightMax) - height
```

Can also be solved using stack.

---

### LeetCode

```text
#42 Trapping Rain Water
```

---

# Daily Temperatures

## Problem

For each day find when a warmer day occurs.

---

### Example

```text
73 74 75 71 69 72 76 73
```

Output:

```text
1 1 4 2 1 1 0 0
```

---

## Concept

Next Greater Element.

---

### LeetCode

```text
#739 Daily Temperatures
```

---

# Stock Span Problem

## Problem

Find consecutive previous days with smaller prices.

---

### Example

```text
100 80 60 70 60 75 85
```

Output:

```text
1 1 1 2 1 4 6
```

---

## Concept

Previous Greater Element.

---

### LeetCode

```text
#901 Online Stock Span
```

---

# Monotonic Queue

## Definition

A Queue maintaining increasing or decreasing order.

Mostly used in:

```text
Sliding Window Maximum
```

---

### LeetCode

```text
#239 Sliding Window Maximum
```

---

# Interview Tips

### Use Stack When

- Need reverse order processing.
- Need matching brackets.
- Need undo operations.
- Need nearest greater/smaller element.

---

### Use Queue When

- FIFO behavior is needed.
- BFS in graphs.
- Scheduling tasks.

---

### Use Monotonic Stack When

- Need nearest greater/smaller element.
- Need range information.
- Need O(n) optimization from O(n²).

---

# Important LeetCode Questions

## Easy

### 1. Valid Parentheses
LeetCode #20

Concept:
- Stack Basics

⭐⭐ Must Do

---

### 2. Implement Queue using Stacks
LeetCode #232

Concept:
- Stack

---

### 3. Implement Stack using Queues
LeetCode #225

Concept:
- Queue

---

### 4. Next Greater Element I
LeetCode #496

Concept:
- Monotonic Stack

⭐⭐ Must Do

---

# Medium

### 5. Daily Temperatures
LeetCode #739

Concept:
- Next Greater Element

⭐⭐⭐ Very Important

---

### 6. Decode String
LeetCode #394

Concept:
- Stack

---

### 7. Asteroid Collision
LeetCode #735

Concept:
- Stack Simulation

---

### 8. Online Stock Span
LeetCode #901

Concept:
- Monotonic Stack

⭐⭐⭐ Interview Favorite

---

### 9. Next Greater Element II
LeetCode #503

Concept:
- Circular Monotonic Stack

---

### 10. Remove K Digits
LeetCode #402

Concept:
- Monotonic Stack

⭐⭐ Frequently Asked

---

# Hard

### 11. Largest Rectangle in Histogram
LeetCode #84

Concept:
- Previous Smaller
- Next Smaller

⭐⭐⭐ Must Do

---

### 12. Trapping Rain Water
LeetCode #42

Concept:
- Stack / Two Pointers

⭐⭐⭐ Top Interview Question

---

### 13. Sliding Window Maximum
LeetCode #239

Concept:
- Monotonic Queue

⭐⭐⭐ Very Important

---

# Must-Do Interview Questions

1. Valid Parentheses (#20)
2. Next Greater Element I (#496)
3. Daily Temperatures (#739)
4. Online Stock Span (#901)
5. Remove K Digits (#402)
6. Largest Rectangle in Histogram (#84)
7. Trapping Rain Water (#42)
8. Sliding Window Maximum (#239)
9. Asteroid Collision (#735)
10. Decode String (#394)

These questions cover almost all major Stack, Queue, and Monotonic Stack patterns asked in coding interviews.