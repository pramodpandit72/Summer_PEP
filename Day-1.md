# Complexity Analysis

## Definition
Complexity Analysis is the process of measuring how much **time** and **memory (space)** an algorithm uses as the input size increases.

It helps us compare different solutions and choose the most efficient one.

---

## Why is Complexity Analysis Important?

Suppose you have two solutions for the same problem:

- Solution A takes 1 second for 1000 inputs.
- Solution B takes 10 seconds for 1000 inputs.

Obviously, Solution A is better.

Complexity Analysis helps us predict performance before running the program on large inputs.

---

## Types of Complexity

### 1. Time Complexity

Time Complexity tells us how much time an algorithm takes to execute.

It does **not** measure actual seconds.

Instead, it counts how the number of operations grows with input size.

### Example

```cpp
for(int i = 0; i < n; i++) {
    cout << i;
}
```

The loop runs `n` times.

Time Complexity = **O(n)**

---

### 2. Space Complexity

Space Complexity tells us how much extra memory an algorithm uses.

### Example

```cpp
vector<int> arr(n);
```

The vector stores `n` elements.

Space Complexity = **O(n)**

---

## Big O Notation

Big O Notation is used to represent the worst-case complexity of an algorithm.

### Common Complexities

| Complexity | Name | Performance |
|------------|------|-------------|
| O(1) | Constant | Best |
| O(log n) | Logarithmic | Very Fast |
| O(n) | Linear | Good |
| O(n log n) | Linearithmic | Efficient |
| O(n²) | Quadratic | Slow |
| O(n³) | Cubic | Very Slow |
| O(2ⁿ) | Exponential | Extremely Slow |
| O(n!) | Factorial | Worst |

---

## Examples

### O(1) - Constant Time

```cpp
int x = arr[0];
```

Only one operation.

---

### O(log n) - Logarithmic Time

Binary Search

```cpp
while(low <= high) {
    int mid = (low + high) / 2;
}
```

Search space becomes half every step.

---

### O(n) - Linear Time

```cpp
for(int i = 0; i < n; i++) {
    cout << arr[i];
}
```

Runs `n` times.

---

### O(n²) - Quadratic Time

```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        cout << i << j;
    }
}
```

Nested loops.

Total operations = n × n

---

## Best, Average and Worst Case

### Best Case

Minimum operations needed.

### Average Case

Expected operations for normal inputs.

### Worst Case

Maximum operations needed.

In DSA, we usually focus on the **Worst Case**.

---

# Competitive Programming Environment

## Definition

Competitive Programming (CP) is a sport where programmers solve coding problems within a limited time.

Problems test:

- Logic Building
- Data Structures
- Algorithms
- Problem Solving Skills
- Optimization Skills

---

## Popular Competitive Programming Platforms

- Codeforces
- LeetCode
- CodeChef
- AtCoder
- HackerRank
- HackerEarth

---

## Typical Competitive Programming Workflow

### Step 1

Read the problem carefully.

### Step 2

Understand:

- Input
- Output
- Constraints

### Step 3

Think of an algorithm.

### Step 4

Analyze complexity.

### Step 5

Write code.

### Step 6

Test with sample inputs.

### Step 7

Submit solution.

---

## Importance of Constraints

Constraints tell us which complexity is acceptable.

### Example

```text
n ≤ 100
```

O(n²) is usually acceptable.

---

```text
n ≤ 100000
```

O(n²) will be too slow.

Use O(n log n) or O(n).

---

## Fast Input/Output in C++

In competitive programming, fast I/O is commonly used.

```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
```

Place these lines at the start of `main()`.

---

## Common CP Template

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    return 0;
}
```

---

## Skills Needed for Competitive Programming

- Strong DSA
- Mathematics
- Problem Solving
- Pattern Recognition
- Optimization Techniques

---

# STL Deep Dive

## Definition

STL stands for **Standard Template Library**.

It is a collection of ready-made data structures and algorithms provided by C++.

Using STL saves time and reduces coding effort.

---

## Main Components of STL

### 1. Containers

Containers store data.

### 2. Iterators

Iterators are used to traverse containers.

### 3. Algorithms

Algorithms perform operations like sorting and searching.

### 4. Functors

Special objects that behave like functions.

---

# Containers in STL

## Vector

Dynamic array.

```cpp
vector<int> v;
```

### Important Functions

```cpp
v.push_back(10);
v.pop_back();

v.size();

v.front();
v.back();

v.clear();
```

---

## Pair

Stores two values together.

```cpp
pair<int,int> p;

p.first = 10;
p.second = 20;
```

---

## Array

Fixed-size array.

```cpp
array<int,5> arr;
```

---

## Stack

Follows LIFO (Last In First Out).

```cpp
stack<int> st;

st.push(10);
st.pop();

st.top();
```

---

## Queue

Follows FIFO (First In First Out).

```cpp
queue<int> q;

q.push(10);
q.pop();

q.front();
q.back();
```

---

## Priority Queue

Stores elements in sorted priority order.

By default, largest element stays at top.

```cpp
priority_queue<int> pq;
```

### Min Heap

```cpp
priority_queue<int,
               vector<int>,
               greater<int>> pq;
```

---

## Set

Stores unique elements in sorted order.

```cpp
set<int> s;
```

### Operations

```cpp
s.insert(10);
s.erase(10);
s.find(10);
```

Complexity: O(log n)

---

## Unordered Set

Stores unique elements.

Not sorted.

```cpp
unordered_set<int> us;
```

Average Complexity: O(1)

---

## Map

Stores key-value pairs in sorted order.

```cpp
map<int,string> mp;

mp[1] = "Ram";
```

Complexity: O(log n)

---

## Unordered Map

Hash-based key-value storage.

```cpp
unordered_map<int,string> mp;
```

Average Complexity: O(1)

---

# Iterators

## Definition

Iterators are objects that point to elements inside containers.

### Example

```cpp
vector<int> v = {1,2,3};

for(auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}
```

---

## Common Iterators

```cpp
begin()
end()

rbegin()
rend()
```

---

# STL Algorithms

Include:

```cpp
#include <algorithm>
```

---

## Sort

```cpp
sort(v.begin(), v.end());
```

Time Complexity: O(n log n)

---

## Reverse

```cpp
reverse(v.begin(), v.end());
```

---

## Max Element

```cpp
int mx = *max_element(v.begin(), v.end());
```

---

## Min Element

```cpp
int mn = *min_element(v.begin(), v.end());
```

---

## Binary Search

```cpp
binary_search(v.begin(), v.end(), x);
```

Array must be sorted.

---

## Count

```cpp
count(v.begin(), v.end(), x);
```

Counts occurrences of x.

---

# Why STL is Important in DSA and CP

- Reduces coding time
- Provides optimized implementations
- Makes code shorter and cleaner
- Widely used in coding interviews
- Essential for Competitive Programming

---

# Quick Revision

- Complexity Analysis measures time and memory usage.
- Time Complexity and Space Complexity are the two main types.
- Big O Notation represents algorithm efficiency.
- Competitive Programming focuses on solving problems quickly and efficiently.
- STL is a library containing ready-made data structures and algorithms.
- Important STL containers: Vector, Pair, Stack, Queue, Set, Map.
- Iterators help traverse containers.
- STL algorithms like sort(), reverse(), and binary_search() are heavily used in DSA and CP.