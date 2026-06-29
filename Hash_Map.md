````md
# HashMap (unordered_map) in C++

## What is HashMap?

A **HashMap** is a data structure that stores data as **Key-Value pairs**.

In C++, HashMap is implemented using:

```cpp
#include <unordered_map>

unordered_map<KeyType, ValueType> mp;
```

It provides **average O(1)** time complexity for insertion, deletion, and searching.

---

# Why HashMap?

Suppose you have an array:

```cpp
nums = [4, 2, 7, 2, 5]
```

If you want to count how many times `2` appears:

### Without HashMap

Traverse the entire array.

```
Time Complexity = O(n)
```

### With HashMap

```cpp
unordered_map<int,int> freq;

freq[2] = 2;
```

```
Time Complexity = O(1) (Average)
```

---

# Real Life Example

Dictionary

```
Word      Meaning

Apple  -> Fruit
Car    -> Vehicle
Dog    -> Animal
```

Here,

```
Word    = Key

Meaning = Value
```

HashMap works exactly the same way.

---

# Declaration

```cpp
unordered_map<int,int> mp;
```

Key = int

Value = int

Example

```
1 → 100

2 → 200

3 → 300
```

---

# Basic Operations

## 1. Insert

### Method 1

```cpp
mp[1] = 100;
```

### Method 2

```cpp
mp.insert({2,200});
```

Time Complexity

```
O(1) Average
```

---

## 2. Access Value

```cpp
cout << mp[1];
```

Output

```
100
```

---

## 3. Update

```cpp
mp[1] = 500;
```

Now

```
1 → 500
```

---

## 4. Search

### Using find()

```cpp
if(mp.find(2) != mp.end())
{
    cout << "Found";
}
```

### Using count()

```cpp
if(mp.count(2))
{
    cout << "Found";
}
```

---

## 5. Delete

```cpp
mp.erase(2);
```

---

## 6. Size

```cpp
cout << mp.size();
```

---

## 7. Empty

```cpp
if(mp.empty())
{
    cout << "Empty";
}
```

---

## 8. Clear

```cpp
mp.clear();
```

---

# Traversing HashMap

## Method 1 (Recommended)

```cpp
for(auto it : mp)
{
    cout << it.first << " ";
    cout << it.second << endl;
}
```

Output

```
1 100
2 200
3 300
```

---

## Method 2

```cpp
for(auto it = mp.begin(); it != mp.end(); it++)
{
    cout << it->first << " ";
    cout << it->second << endl;
}
```

---

# Frequency Counting (Most Important)

Given

```cpp
nums = [1,2,2,3,1,2]
```

Code

```cpp
unordered_map<int,int> freq;

for(int x : nums)
{
    freq[x]++;
}
```

Output

```
1 → 2

2 → 3

3 → 1
```

Time Complexity

```
O(n)
```

---

# Character Frequency

```cpp
string s = "banana";

unordered_map<char,int> freq;

for(char c : s)
{
    freq[c]++;
}
```

Output

```
b → 1

a → 3

n → 2
```

---

# Common Functions

| Function | Description |
|----------|-------------|
| `mp[key]` | Access or Insert |
| `insert()` | Insert key-value pair |
| `erase()` | Delete key |
| `find()` | Search key |
| `count()` | Check existence |
| `size()` | Number of elements |
| `empty()` | Check if empty |
| `clear()` | Remove all elements |

---

# Important Difference

## find()

```cpp
unordered_map<int,int> mp;

if(mp.find(5) == mp.end())
{
    cout << "Not Found";
}
```

HashMap remains empty.

---

## []

```cpp
unordered_map<int,int> mp;

cout << mp[5];
```

Output

```
0
```

Now HashMap becomes

```
5 → 0
```

**Reason**

`mp[key]` inserts the key if it does not exist.

---

# unordered_map vs map

| unordered_map | map |
|---------------|-----|
| Hash Table | Red Black Tree |
| O(1) Average | O(log n) |
| Unordered | Sorted |
| Faster | Slower |
| Used in most DSA problems | Used when sorted order is required |

---

# Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Access | O(1) | O(n) |

---

# When to Use HashMap?

Use HashMap for:

- Frequency Counting
- Fast Searching
- Store Key-Value Pairs
- Detect Duplicates
- Prefix Sum Problems
- Sliding Window Problems
- Two Sum Pattern
- Character Counting
- Store First/Last Index
- Visited Elements

---

# Common Interview Patterns

## 1. Frequency Counting

```cpp
unordered_map<int,int> freq;
```

---

## 2. Store First Index

```cpp
unordered_map<int,int> firstIndex;
```

---

## 3. Prefix Sum

```cpp
unordered_map<int,int> prefix;
```

---

## 4. Character Counting

```cpp
unordered_map<char,int> freq;
```

---

## 5. Visited

```cpp
unordered_map<int,bool> visited;
```

---

# Common Mistakes

## Wrong

```cpp
if(mp[key])
```

This may insert a new key.

---

## Correct

```cpp
if(mp.find(key) != mp.end())
```

or

```cpp
if(mp.count(key))
```

---

# Interview Tips

- Use `unordered_map` when order does not matter.
- Use `map` when sorted order is required.
- Frequency counting is the most common use of HashMap.
- Prefer `find()` or `count()` to check if a key exists.
- Remember that `mp[key]` inserts the key if it does not exist.

---

# LeetCode Practice Questions

## Easy (Must Do)

| Problem No. | Problem Name |
|-------------|--------------|
| #1 | Two Sum ⭐⭐⭐⭐⭐ |
| #217 | Contains Duplicate ⭐⭐⭐⭐ |
| #242 | Valid Anagram ⭐⭐⭐⭐ |
| #349 | Intersection of Two Arrays |
| #350 | Intersection of Two Arrays II |
| #1207 | Unique Number of Occurrences |
| #389 | Find the Difference |
| #383 | Ransom Note |

---

## Easy–Medium

| Problem No. | Problem Name |
|-------------|--------------|
| #205 | Isomorphic Strings ⭐⭐⭐⭐ |
| #290 | Word Pattern |
| #202 | Happy Number |
| #594 | Longest Harmonious Subsequence |

---

## Medium (Most Important)

| Problem No. | Problem Name |
|-------------|--------------|
| #49 | Group Anagrams ⭐⭐⭐⭐⭐ |
| #347 | Top K Frequent Elements ⭐⭐⭐⭐⭐ |
| #128 | Longest Consecutive Sequence ⭐⭐⭐⭐⭐ |
| #560 | Subarray Sum Equals K ⭐⭐⭐⭐⭐ |
| #523 | Continuous Subarray Sum |
| #525 | Contiguous Array |
| #554 | Brick Wall |
| #1497 | Check If Array Pairs Are Divisible by k |

---

## Sliding Window + HashMap

| Problem No. | Problem Name |
|-------------|--------------|
| #3 | Longest Substring Without Repeating Characters ⭐⭐⭐⭐⭐ |
| #567 | Permutation in String ⭐⭐⭐⭐ |
| #438 | Find All Anagrams in a String ⭐⭐⭐⭐ |
| #76 | Minimum Window Substring ⭐⭐⭐⭐⭐ |
| #904 | Fruit Into Baskets |

---

## Advanced

| Problem No. | Problem Name |
|-------------|--------------|
| #454 | 4Sum II |
| #710 | Random Pick with Blacklist |
| #146 | LRU Cache ⭐⭐⭐⭐⭐ |
| #460 | LFU Cache |
| #706 | Design HashMap |

---

# Placement Priority (Solve in Order)

1. #1 Two Sum
2. #217 Contains Duplicate
3. #242 Valid Anagram
4. #49 Group Anagrams
5. #347 Top K Frequent Elements
6. #128 Longest Consecutive Sequence
7. #560 Subarray Sum Equals K
8. #3 Longest Substring Without Repeating Characters
9. #438 Find All Anagrams in a String
10. #76 Minimum Window Substring
11. #146 LRU Cache
12. #706 Design HashMap
````
