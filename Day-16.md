# Greedy Algorithms and Optimization

---

# What is Greedy Algorithm?

## Definition

A Greedy Algorithm is a method where we:

```text
Make the best possible choice at each step
without worrying about future consequences
```

---

# Simple Idea

```text
Take best option right now → hope it leads to global best solution
```

---

# When Greedy Works?

Greedy works only when:

## 1. Greedy Choice Property

```text
Local best choice leads to global best solution
```

## 2. Optimal Substructure

```text
Optimal solution contains optimal subsolutions
```

---

# Greedy vs DP

| Feature | Greedy | DP |
|----------|--------|----|
| Decision | One choice at a time | All possibilities |
| Backtracking | No | Yes (implicit) |
| Speed | Faster | Slower |
| Guarantee | Not always optimal | Always optimal |

---

# When to Use Greedy?

Look for:

- Maximum / Minimum optimization
- Sorting helps decision making
- “Pick best at each step”
- No need to explore all combinations

---

# Core Greedy Patterns

---

# 1. Activity Selection / Interval Scheduling

## Problem

Select maximum number of non-overlapping intervals.

---

## Idea

Always pick:

```text
Interval that finishes earliest
```

---

## Steps

1. Sort by end time
2. Pick first interval
3. Skip overlapping intervals

---

## Example

```text
(1,3), (2,4), (3,5)
```

Answer:

```text
(1,3), (3,5)
```

---

## Important LeetCode

```text
#435 Non-overlapping Intervals
#452 Minimum Number of Arrows to Burst Balloons
```

---

# 2. Fractional Knapsack (Greedy Classic)

## Idea

Pick items with highest value/weight ratio first.

---

## Key Point

Works only when:

```text
You can take fractions of items
```

---

## Steps

1. Sort by value/weight ratio
2. Take highest ratio first

---

## Note

0/1 Knapsack → DP  
Fractional Knapsack → Greedy

---

# 3. Sorting-Based Greedy

Many greedy problems start with sorting.

---

## Example Patterns

- Sort by start time
- Sort by end time
- Sort by value
- Sort by ratio

---

# 4. Jump Game Pattern

## Problem Idea

Can you reach the end?

---

## Greedy Insight

Track:

```text
Farthest reachable index
```

---

## Example

```text
[2,3,1,1,4]
```

Answer:

```text
True
```

---

## LeetCode

```text
#55 Jump Game
#45 Jump Game II
```

---

# 5. Greedy for Stocks

## Idea

Buy low, sell high.

---

## Example

```text
[7,1,5,3,6,4]
```

Profit:

```text
5 + 3 = 8
```

---

## LeetCode

```text
#121 Best Time to Buy and Sell Stock
#122 Best Time to Buy and Sell Stock II
```

---

# 6. Huffman Coding (Greedy + Heap)

## Idea

Build optimal prefix code using:

```text
Min Heap
```

---

## Steps

1. Take two smallest frequencies
2. Merge them
3. Repeat

---

## Use Case

- Compression algorithms
- File encoding

---

# 7. Greedy + Heap Pattern

Used when:

```text
Always pick best available option dynamically
```

---

## Example Problems

- Task Scheduling
- IPO Maximization
- Reorganize String

---

## LeetCode

```text
#621 Task Scheduler
#767 Reorganize String
```

---

# 8. Gas Station Problem

## Idea

Find starting point to complete circuit.

---

## Greedy Insight

If total gas < cost:

```text
Impossible
```

---

If current tank becomes negative:

```text
reset start
```

---

## LeetCode

```text
#134 Gas Station
```

---

# 9. Partitioning Greedy

## Idea

Split array/string based on conditions.

---

## Example

- Partition Labels
- Merge Intervals

---

## LeetCode

```text
#763 Partition Labels
#56 Merge Intervals
```

---

# 10. Greedy with Sorting Intervals

Very important interview pattern.

---

## Merge Intervals

### Steps

1. Sort by start time
2. Merge overlapping intervals

---

## Example

```text
(1,3), (2,6), (8,10)
```

Result:

```text
(1,6), (8,10)
```

---

# How to Identify Greedy Problems?

Look for:

- “Maximum / Minimum”
- “Best possible choice”
- “Schedule / intervals”
- “Can we reach?”
- “Optimization with sorting”

---

# Greedy Strategy Checklist

Before using greedy, ask:

```text
1. Can local choice lead to global answer?
2. Does sorting help?
3. Can I prove optimal substructure?
```

If yes → Greedy works.

---

# Common Greedy Mistakes

- Using greedy without proof
- Ignoring edge cases
- Assuming greedy works always (it doesn’t)

---

# Greedy vs DP Decision Rule

| Problem Type | Approach |
|--------------|----------|
| All possibilities needed | DP |
| Best immediate choice works | Greedy |
| Overlapping subproblems | DP |
| Sorting-based decisions | Greedy |

---

# Important LeetCode Questions

---

## Easy

- #121 Best Time to Buy and Sell Stock
- #455 Assign Cookies
- #860 Lemonade Change

---

## Medium

- #55 Jump Game
- #45 Jump Game II
- #56 Merge Intervals
- #435 Non-overlapping Intervals
- #763 Partition Labels
- #134 Gas Station

---

## Hard

- #621 Task Scheduler
- #452 Minimum Number of Arrows
- #767 Reorganize String

---

# Must-Do Greedy Questions

1. #56 Merge Intervals  
2. #435 Non-overlapping Intervals  
3. #55 Jump Game  
4. #45 Jump Game II  
5. #121 Stock Buy Sell  
6. #134 Gas Station  
7. #763 Partition Labels  
8. #621 Task Scheduler  
9. #452 Minimum Arrows  
10. #767 Reorganize String  

---

# Final Intuition

Greedy is:

```text
Smart local decision making
+ sorting
+ intuition
```

If DP is “thinking all paths”, then Greedy is:

```text
choosing the best path immediately
```