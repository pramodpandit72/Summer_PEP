# Binary Search Patterns

## Definition

Binary Search is an algorithm used to find an element efficiently in a sorted array.

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves.

Because of this, it is much faster than Linear Search.

---

## Why Binary Search?

Suppose an array contains:

```text
1 3 5 7 9 11 13 15
```

Find 11.

### Linear Search

Check:

```text
1 → 3 → 5 → 7 → 9 → 11
```

Time Complexity:

```text
O(n)
```

---

### Binary Search

Check middle element first.

```text
Middle = 7
```

11 is greater than 7.

Ignore the left half.

Search only in:

```text
9 11 13 15
```

Again find middle.

This process continues until the element is found.

Time Complexity:

```text
O(log n)
```

---

# Basic Binary Search

## Code

```cpp
int binarySearch(vector<int>& arr, int target)
{
    int low = 0;
    int high = arr.size() - 1;

    while(low <= high)
    {
        int mid = low + (high - low) / 2;

        if(arr[mid] == target)
            return mid;

        else if(arr[mid] < target)
            low = mid + 1;

        else
            high = mid - 1;
    }

    return -1;
}
```

---

## Time Complexity

```text
O(log n)
```

---

## Space Complexity

```text
O(1)
```

---

# Binary Search Patterns

In interviews, Binary Search is rarely asked in its basic form.

Most questions are based on patterns.

---

# Pattern 1: Search in Sorted Array

### Example

Find target in sorted array.

```text
LeetCode #704
Binary Search
```

This is the basic pattern.

---

# Pattern 2: Lower Bound

## Definition

Find the first position where a number is greater than or equal to target.

---

### Example

Array

```text
1 2 4 4 4 7 9
```

Target = 4

Answer:

```text
Index = 2
```

First occurrence of 4.

---

## Code

```cpp
int lowerBound(vector<int>& arr, int target)
{
    int low = 0;
    int high = arr.size() - 1;

    int ans = arr.size();

    while(low <= high)
    {
        int mid = low + (high - low) / 2;

        if(arr[mid] >= target)
        {
            ans = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return ans;
}
```

---

# Pattern 3: Upper Bound

## Definition

Find first element strictly greater than target.

---

### Example

Array

```text
1 2 4 4 4 7 9
```

Target = 4

Answer:

```text
Index = 5
```

Element 7.

---

# Pattern 4: First Occurrence

## Example

```text
1 2 4 4 4 4 7
```

Find first occurrence of 4.

Answer:

```text
Index = 2
```

---

# Pattern 5: Last Occurrence

## Example

```text
1 2 4 4 4 4 7
```

Find last occurrence of 4.

Answer:

```text
Index = 5
```

---

# Pattern 6: Count Occurrences

Find:

```text
Last Occurrence - First Occurrence + 1
```

---

### Example

```text
1 2 4 4 4 4 7
```

Count of 4:

```text
5 - 2 + 1 = 4
```

---

# Pattern 7: Search Insert Position

## Problem

If target does not exist, find where it should be inserted.

---

### Example

```text
1 3 5 6
```

Target:

```text
2
```

Answer:

```text
Index = 1
```

---

### LeetCode

```text
#35 Search Insert Position
```

---

# Pattern 8: Binary Search on Answer

## Important Pattern

Sometimes the answer itself is not present in the array.

Instead, we search for the answer value.

This is called:

```text
Binary Search on Answer
```

or

```text
Parametric Search
```

Very common in interviews.

---

# Parametric Search

## Definition

Parametric Search means:

Instead of searching an element,
we search the minimum or maximum possible answer that satisfies a condition.

---

## Key Idea

Convert the problem into:

```text
Can this answer work?
```

If yes:

```text
Try smaller answer
```

or

```text
Try larger answer
```

depending on the problem.

---

# When to Use Parametric Search?

Look for words like:

- Minimum Possible
- Maximum Possible
- Largest Value
- Smallest Value
- Optimize
- Minimize
- Maximize

These are strong hints.

---

# Generic Template

```cpp
int low = minimumPossible;
int high = maximumPossible;

while(low <= high)
{
    int mid = low + (high - low) / 2;

    if(isPossible(mid))
    {
        ans = mid;
        high = mid - 1;
    }
    else
    {
        low = mid + 1;
    }
}
```

---

# Example 1: Koko Eating Bananas

### LeetCode #875

---

## Problem

Koko has banana piles.

Find minimum eating speed so that all bananas are eaten within H hours.

---

### Observation

Speed can be:

```text
1 banana/hour
```

to

```text
maxPile bananas/hour
```

---

### Check Function

```cpp
Can Koko finish with speed = mid ?
```

If yes:

```text
Try smaller speed
```

If no:

```text
Increase speed
```

---

### Complexity

```text
O(n log(maxPile))
```

---

# Example 2: Capacity To Ship Packages

### LeetCode #1011

---

## Problem

Find minimum ship capacity.

---

### Search Space

```text
max(weight)
```

to

```text
sum(weight)
```

---

### Check Function

```cpp
Can all packages be shipped
within D days?
```

---

# Example 3: Allocate Minimum Number of Pages

Interview Favorite

---

## Problem

Books contain pages.

Allocate books among students.

Minimize maximum pages assigned to a student.

---

### Search Space

```text
max(book)
```

to

```text
sum(books)
```

---

### Check Function

```cpp
Can allocation happen
with maximum pages = mid ?
```

---

# Example 4: Aggressive Cows

Very Popular Interview Question

---

## Problem

Place cows in stalls.

Maximize minimum distance.

---

### Search Space

```text
1
```

to

```text
lastStall - firstStall
```

---

### Check Function

```cpp
Can we place all cows
with distance = mid ?
```

---

If yes:

```text
Try larger distance
```

---

# How to Identify Parametric Search?

Ask:

### Question 1

Is the answer numeric?

```text
Yes
```

---

### Question 2

Can I check whether a value works?

```text
Yes
```

---

### Question 3

If a value works, do all larger or smaller values also work?

This property is called:

```text
Monotonicity
```

If yes,

Use Binary Search on Answer.

---

# Monotonic Property

## Example

Koko Eating Bananas

```text
Speed = 4 → Not Possible
Speed = 5 → Possible
Speed = 6 → Possible
Speed = 7 → Possible
```

Notice:

```text
False False False True True True
```

or

```text
True True True False False
```

This monotonic pattern is required for Parametric Search.

---

# Interview Tips

Use Normal Binary Search when:

- Array is sorted
- Need to find an element

---

Use Lower Bound / Upper Bound when:

- Duplicates exist
- Need first or last occurrence

---

Use Parametric Search when:

- Need minimum answer
- Need maximum answer
- Need optimization
- Monotonic condition exists

---

# Important LeetCode Questions

## Easy

### 1. Binary Search
LeetCode #704

### 2. Search Insert Position
LeetCode #35

### 3. First Bad Version
LeetCode #278

---

# Medium

### 4. Find First and Last Position of Element
LeetCode #34

Concept:
- First Occurrence
- Last Occurrence

⭐⭐ Very Common

---

### 5. Search in Rotated Sorted Array
LeetCode #33

Concept:
- Modified Binary Search

⭐⭐ Frequently Asked

---

### 6. Koko Eating Bananas
LeetCode #875

Concept:
- Parametric Search   (hours += (p + k - 1) / k;)

⭐⭐⭐ Must Do

---

### 7. Capacity To Ship Packages Within D Days
LeetCode #1011

Concept:
- Binary Search on Answer

⭐⭐⭐ Must Do

---

### 8. Find Peak Element
LeetCode #162

Concept:
- Binary Search Pattern

---

### 9. Single Element in a Sorted Array
LeetCode #540

Concept:
- Binary Search Trick

---

### 10. Minimum Number of Days to Make m Bouquets
LeetCode #1482

Concept:
- Parametric Search

⭐⭐ Very Popular

---

# Hard

### 11. Median of Two Sorted Arrays
LeetCode #4

Concept:
- Advanced Binary Search

⭐⭐⭐ Top Interview Question

---

### 12. Split Array Largest Sum
LeetCode #410

Concept:
- Parametric Search

⭐⭐⭐ Must Do

---

### 13. Find Minimum in Rotated Sorted Array II
LeetCode #154

Concept:
- Binary Search with Duplicates

---

# Must-Do Interview Questions

1. Binary Search (#704)
2. Search Insert Position (#35)
3. Find First and Last Position (#34)
4. Search in Rotated Sorted Array (#33)
5. Find Peak Element (#162)
6. Koko Eating Bananas (#875)
7. Capacity To Ship Packages (#1011)
8. Minimum Days to Make Bouquets (#1482)
9. Split Array Largest Sum (#410)
10. Median of Two Sorted Arrays (#4)

These 10 questions cover almost all major Binary Search and Parametric Search patterns asked in coding interviews.