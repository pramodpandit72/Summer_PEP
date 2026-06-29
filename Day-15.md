# Dynamic Programming II – Advanced Patterns

---

# Recap of DP I

You already know:

- Memoization (Top-Down)
- Tabulation (Bottom-Up)
- Basic problems (Fibonacci, Climbing Stairs, House Robber)

Now we move to **advanced DP patterns used in interviews**.

---

# 1. 0/1 Knapsack Pattern

## Definition

You are given items with:

```text
weight + value
```

You must decide:

```text
Take or Not Take (each item once)
```

---

## Key Idea

At each item:

```text
1. Take it
2. Don’t take it
```

---

## State Definition

```text
dp[i][w] = maximum value using first i items with capacity w
```

---

## Transition

```text
dp[i][w] =
max(
    dp[i-1][w],
    value[i] + dp[i-1][w - weight[i]]
)
```

---

## Important LeetCode

```text
#416 Partition Equal Subset Sum
#494 Target Sum
#322 Coin Change
```

---

# 2. Subset DP Pattern

## Idea

We decide:

```text
Include or exclude elements
```

---

## Example Problems

### Partition Equal Subset Sum

We check if array can be split into two equal sums.

---

## State

```text
dp[i][sum]
```

---

## Optimization

Often reduced to:

```text
1D DP (space optimization)
```

---

# 3. Unbounded Knapsack Pattern

## Difference from 0/1 Knapsack

In Unbounded Knapsack:

```text
You can take an item multiple times
```

---

## Example

Coin Change problem.

---

## State

```text
dp[w] = minimum coins to make sum w
```

---

## Important Problems

```text
#322 Coin Change
#518 Coin Change II
```

---

# 4. Longest Increasing Subsequence (LIS)

## Definition

Find longest strictly increasing subsequence.

---

## Example

```text
10 9 2 5 3 7 101 18
```

Answer:

```text
2 3 7 101
```

Length = 4

---

## DP State

```text
dp[i] = length of LIS ending at i
```

---

## Transition

```text
dp[i] = max(dp[i], dp[j] + 1)
if arr[j] < arr[i]
```

---

## Complexity

```text
O(n^2)
```

---

## Optimized Approach

```text
Binary Search + DP → O(n log n)
```

---

## Important LeetCode

```text
#300 Longest Increasing Subsequence
```

---

# 5. Longest Common Subsequence (LCS)

## Definition

Find common subsequence between two strings.

---

## Example

```text
text1 = abcde
text2 = ace
```

Answer:

```text
ace
```

Length = 3

---

## State

```text
dp[i][j]
= LCS of first i characters of text1 and first j of text2
```

---

## Transition

```text
if text1[i] == text2[j]:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

---

## Important Problems

```text
#1143 Longest Common Subsequence
#583 Delete Operation for Two Strings
#712 Minimum ASCII Delete Sum
```

---

# 6. Edit Distance Pattern

## Definition

Minimum operations to convert one string to another.

Operations:

```text
Insert
Delete
Replace
```

---

## State

```text
dp[i][j]
```

---

## Transition

```text
if same:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] =
    1 + min(
        insert,
        delete,
        replace
    )
```

---

## Important LeetCode

```text
#72 Edit Distance
```

---

# 7. Matrix DP

## Idea

DP applied on grids.

---

## Common Directions

```text
Up
Left
Diagonal
```

---

## Example Problems

### 1. Unique Paths

```text
#62
```

---

### 2. Minimum Path Sum

```text
#64
```

---

### 3. Maximal Square

```text
#221
```

---

## State

```text
dp[i][j] = best answer at cell (i,j)
```

---

# 8. Interval DP

## Definition

DP over ranges or intervals.

---

## Idea

Solve for:

```text
dp[i][j]
```

where i to j is a range.

---

## Example Problems

### Matrix Chain Multiplication

(Not on LeetCode but very important)

---

### Burst Balloons

```text
#312
```

---

## Pattern

```text
Try every possible partition
```

---

# 9. Bitmask DP

## Definition

DP using binary representation of state.

---

## Use Case

When:

```text
n is small (≤ 20)
```

and we need to track visited elements.

---

## Example Problems

### Traveling Salesman Problem (TSP)

---

### LeetCode

```text
#847 Shortest Path Visiting All Nodes
```

---

# 10. DP on Trees

## Idea

Apply DP on tree structure.

---

## Example

House Robber III:

```text
#337
```

---

## State

```text
take node
not take node
```

---

# How to Identify Advanced DP?

Look for:

- “All possible ways”
- “Minimum cost with constraints”
- “Choose or skip multiple times”
- “Substring / subsequence problems”
- “Range-based decisions”
- “Graph + state”

---

# DP Patterns Summary

| Pattern | Example |
|----------|--------|
| 0/1 Knapsack | Subset Sum |
| Unbounded Knapsack | Coin Change |
| LIS | Increasing sequence |
| LCS | String matching |
| Edit Distance | String transformation |
| Matrix DP | Grid paths |
| Interval DP | Burst Balloons |
| Bitmask DP | TSP |
| Tree DP | House Robber III |

---

# Important LeetCode Questions

---

## Knapsack / Subset

- #416 Partition Equal Subset Sum
- #494 Target Sum
- #322 Coin Change
- #518 Coin Change II

---

## LIS

- #300 Longest Increasing Subsequence

---

## LCS

- #1143 Longest Common Subsequence
- #583 Delete Operation for Two Strings
- #72 Edit Distance

---

## Grid DP

- #62 Unique Paths
- #64 Minimum Path Sum
- #221 Maximal Square

---

## Advanced

- #312 Burst Balloons (Interval DP)
- #847 Shortest Path Visiting All Nodes (Bitmask DP)
- #337 House Robber III (Tree DP)

---

# Must-Do DP Problems (Interview List)

1. #322 Coin Change  
2. #300 Longest Increasing Subsequence  
3. #1143 Longest Common Subsequence  
4. #72 Edit Distance  
5. #62 Unique Paths  
6. #64 Minimum Path Sum  
7. #312 Burst Balloons  
8. #847 Shortest Path Visiting All Nodes  
9. #337 House Robber III  
10. #416 Partition Equal Subset Sum  

---

# Final Advice

Advanced DP is not about memorizing formulas.

It is about:

```text
Recognizing patterns + defining state correctly
```

If you master patterns, DP becomes easy in interviews.