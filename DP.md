# Dynamic Programming (DP) - DSA Notes

> **Language:** C++  
> **Platform:** LeetCode / Coding Interviews

---

# What is Dynamic Programming?

**Dynamic Programming (DP)** is an optimization technique used to solve problems by **breaking them into smaller overlapping subproblems** and storing their results to avoid repeated computation.

Instead of solving the same subproblem multiple times, DP computes it **once** and reuses the answer.

---

# When to Use DP?

A problem can be solved using DP if it has:

### 1. Overlapping Subproblems

The same subproblems are solved repeatedly.

Example:

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
```

Here, `fib(3)` is computed multiple times.

---

### 2. Optimal Substructure

The optimal solution can be built using the optimal solutions of smaller subproblems.

Example:

```text
Shortest Path
Knapsack
Longest Common Subsequence
```

---

# DP Workflow

```text
1. Define the state.
2. Write the recurrence relation.
3. Identify the base case.
4. Decide computation order.
5. Optimize space if possible.
```

---

# How to Identify a DP Problem?

Common keywords:

- Maximum / Minimum
- Count the number of ways
- Longest
- Shortest
- Can we reach...
- Possible or not
- Subsequence
- Subarray
- Partition
- Path
- Profit
- Coins
- Steps

If recursion has repeated calculations, think about DP.

---

# Components of DP

## 1. State

Represents the subproblem.

Example:

```cpp
dp[i]
```

Meaning:

> Answer using first `i` elements.

Examples:

```cpp
dp[i][j]
```

Meaning:

> Answer considering indices `(i, j)`.

---

## 2. Transition (Recurrence)

Relationship between states.

Example:

```cpp
dp[i] = dp[i-1] + dp[i-2];
```

---

## 3. Base Case

Smallest valid problem.

Example:

```cpp
dp[0] = 0;
dp[1] = 1;
```

---

# DP Approaches

## 1. Memoization (Top-Down)

Uses recursion + cache.

### Steps

```text
Recursion
+
Store answers
+
Reuse answers
```

Example:

```cpp
int solve(int n)
{
    if(n <= 1)
        return n;

    if(dp[n] != -1)
        return dp[n];

    return dp[n] = solve(n-1) + solve(n-2);
}
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

## 2. Tabulation (Bottom-Up)

Build answers from smaller states.

Example:

```cpp
dp[0] = 0;
dp[1] = 1;

for(int i = 2; i <= n; i++)
    dp[i] = dp[i-1] + dp[i-2];
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

## 3. Space Optimization

Store only required previous states.

Example:

```cpp
int prev2 = 0;
int prev1 = 1;

for(int i = 2; i <= n; i++)
{
    int curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
}
```

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# Memoization vs Tabulation

| Memoization | Tabulation |
|-------------|------------|
| Top-Down | Bottom-Up |
| Uses recursion | Uses loops |
| Easy to write | Faster in practice |
| Stack space required | No recursion stack |
| Solves only needed states | Computes all states |

---

# General DP Template

### Memoization

```cpp
int solve(...)
{
    if(baseCase)
        return answer;

    if(dp[state] != -1)
        return dp[state];

    return dp[state] = transition;
}
```

---

### Tabulation

```cpp
Initialize base cases

for(each state)
{
    dp[state] = transition;
}

return dp[lastState];
```

---

# Types of DP

---

# 1. Linear DP

State depends on previous indices.

Examples:

- Fibonacci
- Climbing Stairs
- House Robber
- Min Cost Climbing Stairs
- Decode Ways

---

# 2. 0/1 Knapsack DP

Each item is used at most once.

State:

```cpp
dp[i][w]
```

Problems:

- 0/1 Knapsack
- Partition Equal Subset Sum
- Target Sum
- Last Stone Weight II

---

# 3. Unbounded Knapsack

Items can be chosen multiple times.

Problems:

- Coin Change
- Coin Change II
- Rod Cutting
- Integer Break

---

# 4. Longest Increasing Subsequence (LIS)

State:

```cpp
dp[i]
```

Problems:

- LIS
- Number of LIS
- Russian Doll Envelopes

---

# 5. Longest Common Subsequence (LCS)

State:

```cpp
dp[i][j]
```

Problems:

- LCS
- Edit Distance
- Delete Operation
- Distinct Subsequences

---

# 6. Grid DP

Move in a grid.

Problems:

- Unique Paths
- Minimum Path Sum
- Triangle
- Cherry Pickup

---

# 7. Interval DP

State:

```cpp
dp[l][r]
```

Problems:

- Burst Balloons
- Matrix Chain Multiplication
- Palindrome Partitioning II

---

# 8. Partition DP

Split array/string into parts.

Problems:

- Partition Array
- Word Break
- Palindrome Partitioning

---

# 9. Bitmask DP

Used when `n` is small (usually ≤ 20).

State:

```cpp
dp[mask]
```

Problems:

- Traveling Salesman
- Assignment Problem

---

# 10. Digit DP

State based on digits of a number.

Problems:

- Count numbers with constraints
- Sum of digits
- Digit restrictions

---

# Most Important DP Problems

## Easy

### Fibonacci Number
LeetCode 509

---

### Climbing Stairs
LeetCode 70

---

### Min Cost Climbing Stairs
LeetCode 746

---

### House Robber
LeetCode 198

---

### Tribonacci Number
LeetCode 1137

---

# Medium

### House Robber II
LeetCode 213

---

### Coin Change
LeetCode 322

---

### Coin Change II
LeetCode 518

---

### Longest Increasing Subsequence
LeetCode 300

---

### Longest Common Subsequence
LeetCode 1143

---

### Partition Equal Subset Sum
LeetCode 416

---

### Target Sum
LeetCode 494

---

### Decode Ways
LeetCode 91

---

### Unique Paths
LeetCode 62

---

### Minimum Path Sum
LeetCode 64

---

### Edit Distance
LeetCode 72

---

### Word Break
LeetCode 139

---

### Perfect Squares
LeetCode 279

---

### Integer Break
LeetCode 343

---

# Hard

### Burst Balloons
LeetCode 312

---

### Distinct Subsequences
LeetCode 115

---

### Palindrome Partitioning II
LeetCode 132

---

### Cherry Pickup
LeetCode 741

---

### Regular Expression Matching
LeetCode 10

---

# DP State Design Tips

Ask these questions:

### What changes?

Examples:

```text
Index
Capacity
Current Sum
Previous Choice
Remaining Moves
Position
Mask
```

These become your DP state.

---

# Common DP Transitions

## Take / Not Take

```cpp
ans = max(
    take,
    notTake
);
```

---

## Include / Exclude

```cpp
pick
skip
```

---

## Move

```cpp
Up
Down
Left
Right
Diagonal
```

---

## Previous State

```cpp
dp[i] depends on dp[i-1]
```

---

# Time Complexity

| DP Type | Complexity |
|----------|------------|
| 1D DP | O(n) |
| Grid DP | O(n × m) |
| Knapsack | O(n × W) |
| LCS | O(n × m) |
| Interval DP | O(n³) |
| Bitmask DP | O(2ⁿ × n) |

---

# Common Mistakes

❌ Wrong DP state.

❌ Incorrect base case.

❌ Forgetting memoization.

❌ Wrong iteration order in tabulation.

❌ Array index out of bounds.

❌ Using recursion when iterative DP is simpler.

---

# DP vs Greedy

| Dynamic Programming | Greedy |
|---------------------|---------|
| Explores multiple choices | Chooses one local best choice |
| Always finds optimal answer (if modeled correctly) | May fail for some problems |
| Stores subproblem results | No storage of subproblems |
| Usually higher time and memory | Usually faster and simpler |

---

# Interview Questions

## Theory

1. What is Dynamic Programming?
2. When should DP be used?
3. Difference between DP and Recursion.
4. Difference between Memoization and Tabulation.
5. What are overlapping subproblems?
6. What is optimal substructure?
7. How do you design a DP state?
8. How do you convert recursion into DP?
9. How do you optimize DP space?
10. DP vs Greedy — when would you choose each?

---

## Coding

### Beginner

- LeetCode 509 — Fibonacci Number
- LeetCode 70 — Climbing Stairs
- LeetCode 746 — Min Cost Climbing Stairs
- LeetCode 198 — House Robber
- LeetCode 1137 — Tribonacci Number

---

### Intermediate

- LeetCode 213 — House Robber II
- LeetCode 322 — Coin Change
- LeetCode 518 — Coin Change II
- LeetCode 300 — Longest Increasing Subsequence
- LeetCode 1143 — Longest Common Subsequence
- LeetCode 416 — Partition Equal Subset Sum
- LeetCode 494 — Target Sum
- LeetCode 91 — Decode Ways
- LeetCode 62 — Unique Paths
- LeetCode 64 — Minimum Path Sum
- LeetCode 72 — Edit Distance
- LeetCode 139 — Word Break
- LeetCode 343 — Integer Break

---

### Advanced

- LeetCode 312 — Burst Balloons
- LeetCode 115 — Distinct Subsequences
- LeetCode 132 — Palindrome Partitioning II
- LeetCode 741 — Cherry Pickup
- LeetCode 10 — Regular Expression Matching

---

# DP Cheat Sheet

| Pattern | Example Problems |
|----------|------------------|
| Linear DP | Fibonacci, House Robber |
| Grid DP | Unique Paths, Minimum Path Sum |
| 0/1 Knapsack | Knapsack, Target Sum |
| Unbounded Knapsack | Coin Change, Rod Cutting |
| LIS | Longest Increasing Subsequence |
| LCS | LCS, Edit Distance |
| Interval DP | Burst Balloons, MCM |
| Partition DP | Word Break, Palindrome Partitioning |
| Bitmask DP | Traveling Salesman |
| Digit DP | Counting Digit Problems |

---

# Key Takeaways

- DP is used when a problem has **Overlapping Subproblems** and **Optimal Substructure**.
- The most important step is designing the **DP state**.
- Follow the order: **State → Transition → Base Case → Computation Order → Space Optimization**.
- Learn common patterns (Linear, Knapsack, LIS, LCS, Grid, Interval, Partition, Bitmask, Digit DP) rather than memorizing solutions.
- Many recursive solutions can be optimized into DP using **Memoization** or **Tabulation**.