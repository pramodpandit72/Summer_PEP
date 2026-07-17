# Greedy Algorithm (DSA Notes)

# What is a Greedy Algorithm?

A **Greedy Algorithm** makes the **best possible choice at the current step** without worrying about future consequences.

The idea is:

> **Choose the locally optimal solution hoping it leads to the globally optimal solution.**

Unlike Dynamic Programming, greedy **never revisits previous decisions**.

---

# When to Use Greedy?

Greedy works when a problem has:

### 1. Greedy Choice Property
A locally optimal choice leads to the overall optimal solution.

### 2. Optimal Substructure
The optimal solution can be built from optimal solutions of subproblems.

If these properties are **not present**, Greedy may fail.

---

# How to Identify a Greedy Problem?

Look for keywords like:

- Minimum number of...
- Maximum number of...
- Earliest finish
- Smallest/Largest first
- Minimum cost
- Maximum profit
- Can we reach...
- Merge optimally
- Schedule tasks
- Non-overlapping intervals

Questions involving:

- Sorting
- Intervals
- Priority Queue
- Frequencies
- Ratios

often indicate Greedy.

---

# General Greedy Approach

```text
1. Understand the objective.
2. Find the best local choice.
3. Prove why the choice is always safe.
4. Sort if necessary.
5. Iterate and build the answer.
```

---

# Common Greedy Patterns

## 1. Sorting + Greedy

Sort elements first.

Examples:
- Activity Selection
- Merge Intervals
- Non-overlapping Intervals
- Assign Cookies

---

## 2. Earliest Finish Time

Always choose the interval that finishes first.

Used in:

- Activity Selection
- Maximum Meetings
- Non-overlapping Intervals

---

## 3. Minimum/Largest First

Choose:

- Smallest value first
- Largest value first

Examples:

- Boats to Save People
- Assign Cookies
- Minimum Platforms

---

## 4. Frequency Based

Use frequencies to make optimal decisions.

Examples:

- Reorganize String
- Task Scheduler
- Huffman Coding

---

## 5. Profit Based

Sort by profit.

Examples:

- Job Sequencing
- IPO Problem

---

## 6. Ratio Based

Sort according to:

```text
profit / weight
```

Example:

Fractional Knapsack

---

## 7. Priority Queue Greedy

Always take:

- smallest
- largest
- highest frequency

Examples:

- Furthest Building You Can Reach
- Reorganize String
- Task Scheduler

---

# Greedy vs Dynamic Programming

| Greedy | Dynamic Programming |
|---------|---------------------|
| Makes local optimal choice | Explores many choices |
| Never revisits decision | Stores previous results |
| Faster | Usually slower |
| Less memory | More memory |
| Doesn't always work | Gives optimal answer when applicable |

---

# Greedy Proof (Very Important)

In interviews, don't just say:

> "I used greedy."

Explain:

> Choosing this element first can never make the answer worse than choosing any other element.

Interviewers often ask:

**Why is Greedy correct?**

Always justify your choice.

---

# Time Complexity

Sorting based problems:

```text
O(n log n)
```

Single traversal:

```text
O(n)
```

Priority Queue:

```text
O(n log n)
```

---

# Standard Greedy Template (C++)

```cpp
sort(arr.begin(), arr.end());

for (auto &x : arr)
{
    if (canTake(x))
    {
        take(x);
    }
}
```

---

# Most Important Greedy Problems

## Easy

### Assign Cookies
LeetCode 455

Concept:
- Sort both arrays.
- Give smallest possible cookie.

---

### Lemonade Change
LeetCode 860

Concept:
- Always return larger bills first.

---

### Can Place Flowers
LeetCode 605

Concept:
- Greedily plant whenever possible.

---

### Maximum Units on a Truck
LeetCode 1710

Concept:
- Sort by units per box.

---

### Largest Perimeter Triangle
LeetCode 976

Concept:
- Sort and check triangle inequality.

---

# Medium

### Jump Game
LeetCode 55

Concept:
Maintain maximum reachable index.

---

### Jump Game II
LeetCode 45

Concept:
Greedy BFS style expansion.

---

### Gas Station
LeetCode 134

Concept:
Reset starting point whenever fuel becomes negative.

---

### Partition Labels
LeetCode 763

Concept:
Extend partition until last occurrence.

---

### Non-overlapping Intervals
LeetCode 435

Concept:
Sort by ending time.

---

### Queue Reconstruction by Height
LeetCode 406

Concept:
Sort by height descending.

---

### Boats to Save People
LeetCode 881

Concept:
Two pointers after sorting.

---

### Bag of Tokens
LeetCode 948

Concept:
Two pointers + Greedy decisions.

---

### Reorganize String
LeetCode 767

Concept:
Max Heap.

---

### Task Scheduler
LeetCode 621

Concept:
Greedy using frequencies.

---

# Hard

### Candy
LeetCode 135

Concept:
Two passes.

---

### Insert Interval
LeetCode 57

Concept:
Merge while traversing.

---

### Minimum Number of Refueling Stops
LeetCode 871

Concept:
Max Heap.

---

### Course Schedule III
LeetCode 630

Concept:
Sort by deadline + Max Heap.

---

### Furthest Building You Can Reach
LeetCode 1642

Concept:
Min Heap.

---

# Classic Greedy Problems (Interview)

## Activity Selection

Choose activities with:

- Earliest ending time.

Time:

```text
O(n log n)
```

---

## Fractional Knapsack

Sort by:

```text
profit / weight
```

Take fractional items.

Time:

```text
O(n log n)
```

---

## Job Sequencing

Sort jobs by:

- Profit descending

Place each job before deadline.

Time:

```text
O(n log n)
```

---

## Huffman Coding

Always merge:

- Two smallest frequencies.

Uses:

- Min Heap

Time:

```text
O(n log n)
```

---

# Tips to Solve Greedy Problems

✅ Check if sorting helps.

✅ Ask:

> What is the best choice I can make now?

✅ Try proving why changing this choice cannot improve the answer.

✅ Think about intervals.

✅ Think about frequencies.

✅ Think about heaps.

---

# Common Mistakes

❌ Applying greedy without proof.

❌ Sorting in the wrong order.

❌ Ignoring edge cases.

❌ Forgetting that greedy does **not** always give the optimal answer.

---

# Interview Questions

## Theory

1. What is a Greedy Algorithm?
2. Difference between Greedy and Dynamic Programming.
3. What is the Greedy Choice Property?
4. What is Optimal Substructure?
5. Why does Greedy fail for some problems?
6. Give an example where Greedy works.
7. Give an example where Greedy fails.
8. Explain the correctness of your Greedy solution.
9. How do you identify a Greedy problem?
10. Why is sorting frequently used in Greedy algorithms?

---

## Coding

### Easy

- LeetCode 455 — Assign Cookies
- LeetCode 605 — Can Place Flowers
- LeetCode 860 — Lemonade Change
- LeetCode 1710 — Maximum Units on a Truck
- LeetCode 976 — Largest Perimeter Triangle

---

### Medium

- LeetCode 55 — Jump Game
- LeetCode 45 — Jump Game II
- LeetCode 134 — Gas Station
- LeetCode 435 — Non-overlapping Intervals
- LeetCode 452 — Minimum Number of Arrows to Burst Balloons
- LeetCode 763 — Partition Labels
- LeetCode 406 — Queue Reconstruction by Height
- LeetCode 881 — Boats to Save People
- LeetCode 621 — Task Scheduler
- LeetCode 767 — Reorganize String
- LeetCode 948 — Bag of Tokens

---

### Hard

- LeetCode 135 — Candy
- LeetCode 57 — Insert Interval
- LeetCode 630 — Course Schedule III
- LeetCode 871 — Minimum Number of Refueling Stops
- LeetCode 1642 — Furthest Building You Can Reach

---

# Cheat Sheet

| Pattern | Technique |
|----------|-----------|
| Activity Selection | Sort by end time |
| Fractional Knapsack | Sort by value/weight |
| Job Sequencing | Sort by profit |
| Jump Game | Max reachable index |
| Gas Station | Running fuel balance |
| Intervals | Sort by end/start |
| Task Scheduler | Frequency counting |
| Huffman Coding | Min Heap |
| Course Schedule III | Max Heap |
| Refueling Stops | Max Heap |
| Boats to Save People | Sorting + Two Pointers |
| Assign Cookies | Sorting + Two Pointers |

---

# Key Takeaways

- Greedy makes the **best local decision** at every step.
- It works only if the **Greedy Choice Property** and **Optimal Substructure** hold.
- Sorting and heaps are common tools in Greedy solutions.
- Always justify **why the greedy choice is correct** during interviews.
- If a greedy strategy cannot be proven, consider **Dynamic Programming** instead.