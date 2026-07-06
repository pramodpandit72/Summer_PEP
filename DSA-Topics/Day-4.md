# Linked Lists

## Definition

A Linked List is a linear data structure where elements are stored in separate memory locations and connected using pointers.

Unlike arrays:

- Arrays store elements in contiguous memory.
- Linked Lists store elements anywhere in memory and connect them using links.

Each element is called a **Node**.

---

# Structure of a Node

A node contains:

1. Data
2. Pointer to next node

```text
+------+------+
| Data | Next |
+------+------+
```

---

## C++ Node Structure

```cpp
class Node
{
public:
    int data;
    Node* next;

    Node(int val)
    {
        data = val;
        next = nullptr;
    }
};
```

---

# Example

Linked List:

```text
10 -> 20 -> 30 -> 40 -> NULL
```

Visualization:

```text
+----+     +----+     +----+     +----+
|10  | --> |20  | --> |30  | --> |40  |
+----+     +----+     +----+     +----+
```

---

# Why Use Linked List?

### Array Problem

Suppose array size is fixed.

```cpp
int arr[100];
```

If size becomes larger, resizing is costly.

---

### Linked List Advantage

- Dynamic Size
- Easy Insertion
- Easy Deletion

---

# Types of Linked Lists

## 1. Singly Linked List

Each node points to the next node.

```text
10 -> 20 -> 30 -> NULL
```

---

## 2. Doubly Linked List

Each node has:

- Previous Pointer
- Next Pointer

```text
NULL <- 10 <-> 20 <-> 30 -> NULL
```

---

## 3. Circular Linked List

Last node points to first node.

```text
10 -> 20 -> 30
^           |
|___________|
```

---

# Traversal

## Definition

Visiting every node once.

### Code

```cpp
Node* temp = head;

while(temp != nullptr)
{
    cout << temp->data << " ";
    temp = temp->next;
}
```

---

## Time Complexity

```text
O(n)
```

---

# Insertion Operations

---

# Insert at Beginning

### Example

Before:

```text
10 -> 20 -> 30
```

After inserting 5:

```text
5 -> 10 -> 20 -> 30
```

---

### Code

```cpp
Node* newNode = new Node(5);

newNode->next = head;

head = newNode;
```

---

## Time Complexity

```text
O(1)
```

---

# Insert at End

### Example

Before

```text
10 -> 20 -> 30
```

After

```text
10 -> 20 -> 30 -> 40
```

---

### Code

```cpp
Node* temp = head;

while(temp->next != nullptr)
{
    temp = temp->next;
}

temp->next = new Node(40);
```

---

## Time Complexity

```text
O(n)
```

---

# Deletion Operations

---

# Delete First Node

### Example

Before

```text
10 -> 20 -> 30
```

After

```text
20 -> 30
```

---

### Code

```cpp
Node* temp = head;

head = head->next;

delete temp;
```

---

## Time Complexity

```text
O(1)
```

---

# Delete Last Node

### Example

Before

```text
10 -> 20 -> 30
```

After

```text
10 -> 20
```

---

### Code

```cpp
Node* temp = head;

while(temp->next->next != nullptr)
{
    temp = temp->next;
}

delete temp->next;

temp->next = nullptr;
```

---

## Time Complexity

```text
O(n)
```

---

# Linked List vs Array

| Feature | Array | Linked List |
|----------|--------|------------|
| Memory | Continuous | Non-Continuous |
| Access | O(1) | O(n) |
| Insert Front | O(n) | O(1) |
| Delete Front | O(n) | O(1) |
| Dynamic Size | No | Yes |

---

# Fast and Slow Pointer Technique

## Definition

Fast-Slow Pointer is a very important Linked List pattern.

We use:

- Slow Pointer → moves 1 step
- Fast Pointer → moves 2 steps

```text
slow = slow->next
fast = fast->next->next
```

This technique helps solve many Linked List problems efficiently.

---

# Why Use Fast-Slow Pointers?

Without it:

Many problems require:

```text
O(n²)
```

With Fast-Slow:

```text
O(n)
```

---

# Pattern 1: Find Middle Node

## Problem

Find middle node of linked list.

### Example

```text
1 -> 2 -> 3 -> 4 -> 5
```

Answer:

```text
3
```

---

## Idea

Move:

```text
Slow = 1 step
Fast = 2 steps
```

When fast reaches end:

```text
Slow reaches middle
```

---

### Code

```cpp
Node* slow = head;
Node* fast = head;

while(fast != nullptr && fast->next != nullptr)
{
    slow = slow->next;
    fast = fast->next->next;
}

return slow;
```

---

## Time Complexity

```text
O(n)
```

---

# Pattern 2: Detect Cycle

## Problem

Check if linked list contains a cycle.

### Example

```text
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

---

## Floyd Cycle Detection Algorithm

Also called:

```text
Tortoise and Hare Algorithm
```

---

## Idea

If cycle exists:

Fast pointer will eventually meet slow pointer.

---

### Code

```cpp
Node* slow = head;
Node* fast = head;

while(fast && fast->next)
{
    slow = slow->next;
    fast = fast->next->next;

    if(slow == fast)
        return true;
}

return false;
```

---

## Time Complexity

```text
O(n)
```

---

# Pattern 3: Find Start of Cycle

## Problem

Find the node where cycle begins.

---

### Example

```text
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

Answer:

```text
3
```

---

## Trick

After slow and fast meet:

Move one pointer to head.

Move both one step at a time.

The meeting point becomes the cycle start.

---

### LeetCode

```text
#142 Linked List Cycle II
```

---

# Pattern 4: Find Length of Cycle

## Idea

After detecting cycle:

Keep moving until you return to the same node.

Count steps.

---

### Example

Cycle:

```text
3 -> 4 -> 5 -> 3
```

Length:

```text
3
```

---

# Pattern 5: Happy Number

This is actually a Fast-Slow Pointer problem.

### LeetCode #202

---

## Idea

Generate next number repeatedly.

Use:

```text
Slow = 1 jump
Fast = 2 jumps
```

Detect cycle.

---

# Pattern 6: Find Nth Node From End

## Problem

Find kth node from end.

### Example

```text
1 -> 2 -> 3 -> 4 -> 5
```

k = 2

Answer:

```text
4
```

---

## Idea

Move fast pointer k steps ahead.

Then move both together.

When fast reaches end:

Slow reaches answer.

---

### Code

```cpp
Node* slow = head;
Node* fast = head;

for(int i = 0; i < k; i++)
{
    fast = fast->next;
}

while(fast)
{
    slow = slow->next;
    fast = fast->next;
}

return slow;
```

---

## Time Complexity

```text
O(n)
```

---

# Pattern 7: Check Palindrome Linked List

### Example

```text
1 -> 2 -> 2 -> 1
```

Answer:

```text
True
```

---

## Steps

1. Find middle using Fast-Slow.
2. Reverse second half.
3. Compare both halves.

---

### LeetCode

```text
#234 Palindrome Linked List
```

---

# Pattern 8: Reorder List

### Example

Before

```text
1 -> 2 -> 3 -> 4 -> 5
```

After

```text
1 -> 5 -> 2 -> 4 -> 3
```

---

## Steps

1. Find middle.
2. Reverse second half.
3. Merge both lists.

---

### LeetCode

```text
#143 Reorder List
```

---

# How to Identify Fast-Slow Pointer Questions?

Look for words like:

- Middle Node
- Cycle Detection
- Circular List
- Loop
- Nth Node From End
- Palindrome Linked List
- Reorder List

These are strong hints.

---

# Important LeetCode Questions

## Easy

### 1. Linked List Cycle
LeetCode #141

Concept:
- Floyd Cycle Detection

⭐⭐ Must Do

---

### 2. Middle of the Linked List
LeetCode #876

Concept:
- Fast-Slow Pointer

⭐⭐ Must Do

---

### 3. Remove Linked List Elements
LeetCode #203

Concept:
- Basic Linked List

---

### 4. Reverse Linked List
LeetCode #206

Concept:
- Fundamental Linked List

⭐⭐ Must Do

---

### 5. Palindrome Linked List
LeetCode #234

Concept:
- Fast-Slow Pointer

⭐⭐ Frequently Asked

---

# Medium

### 6. Linked List Cycle II
LeetCode #142

Concept:
- Find Cycle Start

⭐⭐⭐ Very Important

---

### 7. Remove Nth Node From End
LeetCode #19

Concept:
- Two Pointers

⭐⭐⭐ Must Do

---

### 8. Reorder List
LeetCode #143

Concept:
- Fast-Slow + Reverse

⭐⭐⭐ Interview Favorite

---

### 9. Odd Even Linked List
LeetCode #328

Concept:
- Pointer Manipulation

---

### 10. Swap Nodes in Pairs
LeetCode #24

Concept:
- Linked List Manipulation

---

### 11. Add Two Numbers
LeetCode #2

Concept:
- Linked List Basics

⭐⭐ Frequently Asked

---

### 12. Partition List
LeetCode #86

Concept:
- Linked List Rearrangement

---

# Hard

### 13. Reverse Nodes in k-Group
LeetCode #25

Concept:
- Advanced Linked List

⭐⭐⭐ Top Interview Question

---

### 14. Merge k Sorted Lists
LeetCode #23

Concept:
- Linked List + Heap

⭐⭐ Frequently Asked

---

# Must-Do Interview Questions

1. Reverse Linked List (#206)
2. Middle of Linked List (#876)
3. Linked List Cycle (#141)
4. Linked List Cycle II (#142)
5. Remove Nth Node From End (#19)
6. Palindrome Linked List (#234)
7. Reorder List (#143)
8. Add Two Numbers (#2)
9. Reverse Nodes in K-Group (#25)
10. Merge K Sorted Lists (#23)

These questions cover almost all important Linked List and Fast-Slow Pointer patterns asked in coding interviews.