# Hashing

## Definition

Hashing is a technique used to store and retrieve data very quickly.

It uses a special function called a:

```text
Hash Function
```

which converts data into an index (location).

This allows searching, insertion, and deletion in very little time.

---

## Why Hashing?

Suppose you want to check whether a number exists.

Array:

```text
1 5 7 10 15
```

### Linear Search

```text
O(n)
```

Need to check elements one by one.

---

### Hashing

Store elements in a hash table.

Search:

```text
O(1)
```

(Average Case)

Much faster.

---

# Hash Function

## Definition

A Hash Function converts a key into an index.

Example:

```text
Key = 25
```

Hash Function:

```text
25 % 10 = 5
```

Store value at index:

```text
5
```

---

# Hash Table

## Definition

A Hash Table stores data using hashing.

Example:

```text
Index    Value

0
1
2
3
4
5        25
6
7
8
9
```

---

# Collision

## Definition

A collision occurs when two keys produce the same hash value.

Example:

```text
15 % 10 = 5

25 % 10 = 5
```

Both want index 5.

This creates a collision.

---

# Collision Handling

Common methods:

### 1. Chaining

Store multiple values in the same bucket.

```text
Index 5

15 -> 25 -> 35
```

---

### 2. Open Addressing

Find another empty location.

---

# Frequency Counting

One of the most important applications of hashing.

---

## Example

Array:

```text
1 2 2 3 3 3
```

Frequency:

```text
1 → 1

2 → 2

3 → 3
```

---

## Code

```cpp
unordered_map<int,int> freq;

for(int x : arr)
{
    freq[x]++;
}
```

---

# Maps

## Definition

Map stores:

```text
Key → Value
```

pairs.

Example:

```text
Roll Number → Student Name
```

---

# Ordered Map

## STL Syntax

```cpp
map<int,string> mp;
```

---

## Example

```cpp
mp[1] = "Rahul";

mp[2] = "Aman";

mp[3] = "Neha";
```

---

## Output

Stored in sorted order of keys.

```text
1 Rahul

2 Aman

3 Neha
```

---

# Operations

### Insert

```cpp
mp[1] = "Rahul";
```

---

### Find

```cpp
mp.find(1);
```

---

### Erase

```cpp
mp.erase(1);
```

---

### Count

```cpp
mp.count(1);
```

Returns:

```text
1 if exists

0 otherwise
```

---

# Complexity

```text
O(log n)
```

because map uses a Balanced BST internally.

---

# Unordered Map

## Definition

Hash Table based Map.

---

## Syntax

```cpp
unordered_map<int,int> mp;
```

---

# Complexity

Average:

```text
O(1)
```

Worst:

```text
O(n)
```

---

# Difference Between Map and Unordered Map

| Feature | map | unordered_map |
|----------|------|---------------|
| Storage | Sorted | Unsorted |
| Search | O(log n) | O(1) Avg |
| Internal DS | BST | Hash Table |

---

# Sets

## Definition

A Set stores:

```text
Unique Elements Only
```

Duplicates are automatically removed.

---

## Example

```cpp
set<int> s;

s.insert(10);

s.insert(20);

s.insert(10);
```

Stored:

```text
10 20
```

Duplicate removed.

---

# Ordered Set

## Syntax

```cpp
set<int> s;
```

---

## Example

```cpp
s.insert(5);

s.insert(1);

s.insert(10);
```

Output:

```text
1 5 10
```

Always sorted.

---

## Complexity

```text
O(log n)
```

---

# Unordered Set

## Syntax

```cpp
unordered_set<int> us;
```

---

## Properties

- Unique Elements
- No Sorting

---

## Complexity

Average:

```text
O(1)
```

---

# Difference Between Set and Unordered Set

| Feature | set | unordered_set |
|----------|------|---------------|
| Sorted | Yes | No |
| Search | O(log n) | O(1) Avg |
| Internal DS | BST | Hash Table |

---

# Common Hashing Applications

---

## 1. Frequency Counting

```cpp
unordered_map<int,int> freq;
```

---

## 2. Duplicate Detection

### Example

Check if duplicates exist.

```cpp
unordered_set<int> st;
```

---

## 3. Two Sum

LeetCode #1

Use HashMap.

Complexity:

```text
O(n)
```

instead of

```text
O(n²)
```

---

## 4. Longest Consecutive Sequence

LeetCode #128

Use HashSet.

Complexity:

```text
O(n)
```

---

# String Hashing

## Definition

String Hashing converts an entire string into a single numeric value.

Instead of comparing complete strings repeatedly, we compare their hashes.

This makes comparisons faster.

---

# Why String Hashing?

Suppose:

```text
String Length = 100000
```

Comparing strings directly:

```text
O(n)
```

Comparing hashes:

```text
O(1)
```

---

# Basic Idea

Convert:

```text
abc
```

into a number.

Example:

```text
a = 1

b = 2

c = 3
```

Hash:

```text
1×P² + 2×P¹ + 3×P⁰
```

where:

```text
P = Prime Number
```

Usually:

```text
31

or

37
```

---

# Polynomial Rolling Hash

Most commonly used hashing method.

---

## Formula

```text
Hash(S)

=

S[0]×P⁰
+
S[1]×P¹
+
S[2]×P²
+ ...
```

---

## Example

String:

```text
abc
```

Values:

```text
a = 1

b = 2

c = 3
```

Take:

```text
P = 31
```

Hash:

```text
1×31⁰

+
2×31¹

+
3×31²
```

---

# Prefix Hash

Similar to Prefix Sum.

---

## Definition

Store hash values from beginning to every position.

This helps find substring hashes quickly.

---

## Example

```text
abcdef
```

Store:

```text
Hash(0)

Hash(0..1)

Hash(0..2)

...
```

---

# Why Prefix Hash?

Allows:

```text
Substring Comparison
```

in

```text
O(1)
```

---

# String Hashing Applications

---

## 1. Pattern Matching

Find pattern inside text.

---

### Example

```text
Text:
abcdef

Pattern:
cde
```

---

## 2. Rabin-Karp Algorithm

Uses String Hashing.

---

### Complexity

Average:

```text
O(n)
```

---

## 3. Duplicate Substring Detection

---

## 4. Longest Common Substring

---

## 5. Competitive Programming

String Hashing is very common in:

- Codeforces
- AtCoder
- ICPC

---

# Important Interview Tips

### Use Map When

- Need sorted keys.
- Need ordered traversal.

---

### Use Unordered Map When

- Only fast lookup is needed.

---

### Use Set When

- Need unique values.
- Need sorted output.

---

### Use Unordered Set When

- Need unique values quickly.

---

### Use String Hashing When

- Comparing large strings.
- Finding substrings efficiently.
- Pattern matching problems.

---

# Important LeetCode Questions

## Easy

### 1. Two Sum
LeetCode #1

Concept:
- HashMap

⭐⭐⭐ Must Do

---

### 2. Contains Duplicate
LeetCode #217

Concept:
- HashSet

⭐⭐ Must Do

---

### 3. Valid Anagram
LeetCode #242

Concept:
- Frequency Counting

⭐⭐ Important

---

### 4. Intersection of Two Arrays
LeetCode #349

Concept:
- Set

---

# Medium

### 5. Group Anagrams
LeetCode #49

Concept:
- HashMap

⭐⭐⭐ Very Important

---

### 6. Longest Consecutive Sequence
LeetCode #128

Concept:
- HashSet

⭐⭐⭐ Interview Favorite

---

### 7. Top K Frequent Elements
LeetCode #347

Concept:
- HashMap + Heap

⭐⭐⭐ Must Do

---

### 8. Subarray Sum Equals K
LeetCode #560

Concept:
- Prefix Sum + HashMap

⭐⭐⭐ Very Important

---

### 9. Find All Anagrams in a String
LeetCode #438

Concept:
- Hashing + Sliding Window

---

### 10. Longest Substring Without Repeating Characters
LeetCode #3

Concept:
- HashMap + Sliding Window

⭐⭐⭐ Must Do

---

# Hard

### 11. Minimum Window Substring
LeetCode #76

Concept:
- HashMap + Sliding Window

⭐⭐⭐ Frequently Asked

---

### 12. Find Duplicate Subtrees
LeetCode #652

Concept:
- Tree Hashing

---

### 13. Repeated DNA Sequences
LeetCode #187

Concept:
- String Hashing

---

# Must-Do Interview Questions

1. Two Sum (#1)
2. Contains Duplicate (#217)
3. Valid Anagram (#242)
4. Group Anagrams (#49)
5. Longest Consecutive Sequence (#128)
6. Subarray Sum Equals K (#560)
7. Longest Substring Without Repeating Characters (#3)
8. Top K Frequent Elements (#347)
9. Minimum Window Substring (#76)
10. Repeated DNA Sequences (#187)

These questions cover the most important Hashing, Maps, Sets, and String Hashing patterns commonly asked in coding interviews.