# Advanced Arrays

## Definition

Advanced Array techniques are methods used to solve array problems efficiently.

Instead of checking every possible combination (Brute Force), we use optimized approaches to reduce time complexity.

These techniques are very common in:

- Coding Interviews
- LeetCode Problems
- Competitive Programming

---

# Common Advanced Array Concepts

## 1. Two Pointers

### Definition

Two pointers are two variables used to traverse an array from different positions.

Usually:

- One pointer starts from the beginning.
- Another starts from the end.

### Example

Find if an array contains two numbers whose sum is equal to a target.

```cpp
vector<int> arr = {1,2,3,4,5};
int target = 7;
```

```cpp
int left = 0;
int right = arr.size() - 1;

while(left < right)
{
    int sum = arr[left] + arr[right];

    if(sum == target)
        break;
    else if(sum < target)
        left++;
    else
        right--;
}
```

### Time Complexity

```text
O(n)
```

---

## 2. Kadane's Algorithm

### Definition

Used to find the Maximum Sum Subarray.

Instead of checking all subarrays, we keep track of the current sum and maximum sum.

### Example

```cpp
vector<int> arr = {-2,1,-3,4,-1,2,1,-5,4};
```

### Code

```cpp
int currSum = 0;
int maxSum = INT_MIN;

for(int x : arr)
{
    currSum += x;

    maxSum = max(maxSum, currSum);

    if(currSum < 0)
        currSum = 0;
}
```

### Time Complexity

```text
O(n)
```

---

## 3. Difference Array

### Definition

Used when multiple range updates are required.

Instead of updating every element in a range, we update only boundary positions.

### Example

Add 5 to all elements from index 2 to 6.

Normal approach:

```text
O(n)
```

Difference Array:

```text
O(1)
```

per update.

---

# Prefix Sum Technique

## Definition

Prefix Sum stores the sum of all elements from index 0 to i.

### Formula

```text
prefix[i] = prefix[i-1] + arr[i]
```

---

## Example

Array:

```text
1 2 3 4 5
```

Prefix Sum:

```text
1 3 6 10 15
```

---

## Code

```cpp
vector<int> prefix(n);

prefix[0] = arr[0];

for(int i = 1; i < n; i++)
{
    prefix[i] = prefix[i-1] + arr[i];
}
```

---

## Range Sum Query

### Problem

Find sum from index L to R.

Array:

```text
1 2 3 4 5
```

Find sum from index 1 to 3.

Normal Method:

```text
2 + 3 + 4 = 9
```

Time Complexity:

```text
O(n)
```

---

### Using Prefix Sum

Formula:

```text
Sum(L,R) = prefix[R] - prefix[L-1]
```

Example:

```text
prefix[3] - prefix[0]
=
10 - 1
=
9
```

### Time Complexity

```text
O(1)
```

---

# Prefix Maximum

## Definition

Stores maximum element from index 0 to i.

### Example

Array:

```text
3 7 2 10 5
```

Prefix Maximum:

```text
3 7 7 10 10
```

---

# Prefix Minimum

## Definition

Stores minimum element from index 0 to i.

### Example

```text
3 7 2 10 5
```

Prefix Minimum:

```text
3 3 2 2 2
```

---

# Suffix Sum Technique

## Definition

Suffix Sum stores sum from index i to last index.

### Formula

```text
suffix[i] = suffix[i+1] + arr[i]
```

---

## Example

Array

```text
1 2 3 4 5
```

Suffix Sum

```text
15 14 12 9 5
```

---

## Code

```cpp
vector<int> suffix(n);

suffix[n-1] = arr[n-1];

for(int i = n-2; i >= 0; i--)
{
    suffix[i] = suffix[i+1] + arr[i];
}
```

---

# Suffix Maximum

Array

```text
3 7 2 10 5
```

Suffix Maximum

```text
10 10 10 10 5
```

---

# Suffix Minimum

Array

```text
3 7 2 10 5
```

Suffix Minimum

```text
2 2 2 5 5
```

---

# Why Prefix and Suffix Arrays are Useful

They help solve problems involving:

- Range Queries
- Left Side Information
- Right Side Information
- Product Arrays
- Rain Water Trapping
- Equilibrium Index

Very common in interviews.

---

# Sliding Window Technique

## Definition

Sliding Window is used when we need information about a continuous subarray or substring.

Instead of recalculating every subarray, we move a window efficiently.

---

# Fixed Size Sliding Window

## Problem

Find maximum sum subarray of size K.

Array:

```text
1 4 2 10 23 3 1 0 20
```

K = 4

---

## Brute Force

Check every subarray.

Time Complexity:

```text
O(n*k)
```

---

## Sliding Window

### Idea

1. Calculate first window sum.
2. Remove left element.
3. Add new right element.
4. Move window.

---

### Code

```cpp
int windowSum = 0;

for(int i = 0; i < k; i++)
{
    windowSum += arr[i];
}

int maxSum = windowSum;

for(int i = k; i < n; i++)
{
    windowSum += arr[i];
    windowSum -= arr[i-k];

    maxSum = max(maxSum, windowSum);
}
```

---

### Time Complexity

```text
O(n)
```

---

# Variable Size Sliding Window

## Definition

Window size changes according to conditions.

Used for:

- Longest Substring
- Smallest Subarray
- At Most K Distinct Elements
- Character Replacement Problems

---

## Example

Find smallest subarray with sum ≥ target.

### Idea

Expand right pointer.

If condition satisfies:

- Update answer.
- Shrink left pointer.

---

### Template

```cpp
int left = 0;

for(int right = 0; right < n; right++)
{
    // expand window

    while(condition)
    {
        // shrink window
        left++;
    }
}
```

---

# When to Think About Sliding Window?

If the problem contains words like:

- Subarray
- Substring
- Consecutive Elements
- Continuous Segment
- Window of Size K

Then Sliding Window is usually a good approach.

---

# Interview Tips

### Use Prefix Sum When

- Multiple range sum queries exist.
- Need cumulative information.

---

### Use Suffix Array When

- Need information from right side.
- Need left-right comparison.

---

### Use Sliding Window When

- Problem involves contiguous elements.
- Window can move efficiently.

---

# Important LeetCode Questions

## Easy

### 1. Two Sum
LeetCode #1

Concept:
- Arrays
- Hashing

---

### 2. Best Time to Buy and Sell Stock
LeetCode #121

Concept:
- Prefix Minimum

---

### 3. Running Sum of 1D Array
LeetCode #1480

Concept:
- Prefix Sum

---

### 4. Find Pivot Index
LeetCode #724

Concept:
- Prefix + Suffix

---

### 5. Maximum Average Subarray I
LeetCode #643

Concept:
- Fixed Sliding Window

---

# Medium

### 6. Maximum Subarray
LeetCode #53

Concept:
- Kadane's Algorithm

⭐ Very Frequently Asked

---

### 7. Product of Array Except Self
LeetCode #238

Concept:
- Prefix + Suffix

⭐ Top Interview Question

---

### 8. Subarray Sum Equals K
LeetCode #560

Concept:
- Prefix Sum + HashMap

⭐ Very Important

---

### 9. Longest Consecutive Sequence
LeetCode #128

Concept:
- Arrays + Hashing

---

### 10. Container With Most Water
LeetCode #11

Concept:
- Two Pointers

⭐ Frequently Asked

---

### 11. Longest Repeating Character Replacement
LeetCode #424

Concept:
- Variable Sliding Window

⭐ Interview Favorite

---

### 12. Permutation in String
LeetCode #567

Concept:
- Sliding Window

---

### 13. Minimum Size Subarray Sum
LeetCode #209

Concept:
- Variable Sliding Window

---

### 14. Fruit Into Baskets
LeetCode #904

Concept:
- Variable Sliding Window

---

### 15. Longest Substring Without Repeating Characters
LeetCode #3

Concept:
- Sliding Window + HashMap

⭐ One of the Most Asked Questions

---

# Hard

### 16. Sliding Window Maximum
LeetCode #239

Concept:
- Monotonic Queue

⭐ Very Important

---

### 17. Trapping Rain Water
LeetCode #42

Concept:
- Prefix/Suffix
- Two Pointers

⭐⭐ Extremely Popular

---

### 18. Minimum Window Substring
LeetCode #76

Concept:
- Advanced Sliding Window

⭐⭐ Frequently Asked in Big Tech

---

### 19. First Missing Positive
LeetCode #41

Concept:
- Advanced Array Manipulation

---

### 20. Maximum Sum Circular Subarray
LeetCode #918

Concept:
- Kadane's Algorithm

---

# Must-Do Interview Questions (Highest Priority)

1. Two Sum (#1)
2. Best Time to Buy and Sell Stock (#121)
3. Maximum Subarray (#53)
4. Product of Array Except Self (#238)
5. Find Pivot Index (#724)
6. Subarray Sum Equals K (#560)
7. Container With Most Water (#11)
8. Longest Substring Without Repeating Characters (#3)
9. Sliding Window Maximum (#239)
10. Trapping Rain Water (#42)
11. Minimum Window Substring (#76)
12. Longest Repeating Character Replacement (#424)

If you master these 12 questions, you'll cover around 80% of the most common interview patterns related to Arrays, Prefix/Suffix, and Sliding Window.