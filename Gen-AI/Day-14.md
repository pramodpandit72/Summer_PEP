# Dynamic Programming (DP) I – Introduction

---

# What is Dynamic Programming?

## Definition

Dynamic Programming is a technique used to solve problems by:

```text
Breaking them into smaller overlapping subproblems
AND
Storing results to avoid recomputation
```

---

# Simple Idea

If you solve the same problem again and again:

```text
DON’T recompute it
STORE it once
REUSE it
```

---

# Why DP?

Without DP:

```text
Exponential time (very slow)
```

With DP:

```text
Polynomial time (fast)
```

---

# Real Life Analogy

Think of calculating Fibonacci numbers:

```text
fib(5)
```

You compute:

```text
fib(4) + fib(3)
```

But fib(3) is computed multiple times.

DP stores it once.

---

# When to Use DP?

Use DP when:

- Overlapping subproblems exist
- Optimal substructure exists

---

## 1. Overlapping Subproblems

Same subproblem repeats.

Example:

```text
Fibonacci
Knapsack
Climbing Stairs
```

---

## 2. Optimal Substructure

Optimal solution depends on optimal solutions of subproblems.

---

# DP vs Recursion

| Feature | Recursion | DP |
|----------|-----------|----|
| Repetition | Yes | No |
| Speed | Slow | Fast |
| Storage | No | Yes |

---

# Types of DP

---

## 1. Memoization (Top-Down)

- Recursive solution
- Store answers in cache

---

## 2. Tabulation (Bottom-Up)

- Iterative approach
- Build solution from base cases

---

# Fibonacci Example

---

## Problem

```text
fib(n) = fib(n-1) + fib(n-2)
```

---

## Recursive Solution (Bad)

```cpp
int fib(int n)
{
    if(n <= 1)
        return n;

    return fib(n-1) + fib(n-2);
}
```

Time:

```text
O(2^n)
```

---

# Memoization (DP 1)

## Idea

Store computed results.

---

## Code

```cpp
int fib(int n, vector<int>& dp)
{
    if(n <= 1)
        return n;

    if(dp[n] != -1)
        return dp[n];

    return dp[n] = fib(n-1, dp) + fib(n-2, dp);
}
```

---

## Time Complexity

```text
O(n)
```

---

# Tabulation (DP 2)

## Code

```cpp
int fib(int n)
{
    vector<int> dp(n+1);

    dp[0] = 0;
    dp[1] = 1;

    for(int i = 2; i <= n; i++)
    {
        dp[i] = dp[i-1] + dp[i-2];
    }

    return dp[n];
}
```

---

## Time Complexity

```text
O(n)
```

---

# Space Optimization

We don’t need full array.

---

## Code

```cpp
int fib(int n)
{
    if(n <= 1)
        return n;

    int prev2 = 0;
    int prev1 = 1;

    for(int i = 2; i <= n; i++)
    {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
}
```

---

## Space Complexity

```text
O(1)
```

---

# Steps to Solve DP Problems

---

## Step 1: Identify DP

Check:

- Repetition
- Overlapping subproblems
- Choices

---

## Step 2: Define State

Example:

```text
dp[i] = answer for i-th index
```

---

## Step 3: Transition

How current depends on previous states.

---

## Step 4: Base Case

Smallest known values.

---

## Step 5: Optimize (optional)

Reduce space complexity.

---

# Classic DP Problems (Beginner)

---

## 1. Climbing Stairs

### Problem

You can take:

```text
1 step or 2 steps
```

Find ways to reach top.

---

### Relation

```text
dp[i] = dp[i-1] + dp[i-2]
```

Same as Fibonacci.

---

### LeetCode

```text
#70 Climbing Stairs
```

---

## 2. Min Cost Climbing Stairs

```text
#746
```

---

## 3. House Robber

### Idea

You cannot rob adjacent houses.

---

### Relation

```text
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

---

### LeetCode

```text
#198 House Robber
```

---

## 4. House Robber II

Circular array version.

```text
#213
```

---

## 5. Fibonacci Variants

Many interview questions are variations of Fibonacci.

---

# DP Patterns You Must Know

---

## 1. Linear DP

Example:

- Fibonacci
- Climbing Stairs
- House Robber

---

## 2. Choice DP

At every step:

```text
Take or Not Take
```

---

## 3. State Transition DP

Current depends on previous states.

---

## 4. Optimization DP

Reduce time or space.

---

# How to Identify DP Problems?

Look for:

- "Number of ways"
- "Minimum / Maximum"
- "Count combinations"
- "Optimal result"
- "Choices at each step"

---

# Important LeetCode Questions

---

## Easy

### 1. Climbing Stairs
LeetCode #70

⭐⭐⭐ Must Do

---

### 2. Fibonacci Number
LeetCode #509

---

## Medium

### 3. Min Cost Climbing Stairs
LeetCode #746

⭐⭐ Important

---

### 4. House Robber
LeetCode #198

⭐⭐⭐ Very Important

---

### 5. House Robber II
LeetCode #213

⭐⭐⭐ Interview Favorite

---

### 6. Delete and Earn
LeetCode #740

---

### 7. Maximum Subarray (Kadane’s Algorithm)
LeetCode #53

(Not DP strictly, but DP-style thinking)

---

## Hard

### 8. Word Break
LeetCode #139

---

### 9. Decode Ways
LeetCode #91

---

# Must-Do DP Problems

1. Climbing Stairs (#70)
2. Fibonacci (#509)
3. House Robber (#198)
4. House Robber II (#213)
5. Min Cost Climbing Stairs (#746)
6. Maximum Subarray (#53)
7. Word Break (#139)
8. Decode Ways (#91)

---

# Final Intuition

DP is just:

```text
Recursion + Memoization = Optimization
```

If recursion is repeating work → DP will help you save it.

---