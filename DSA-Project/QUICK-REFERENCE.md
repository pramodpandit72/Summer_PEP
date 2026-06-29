# Quick Reference Guide

## Array Operations
- Access: `arr[i]` - O(1)
- Insert: `arr.insert(pos, val)` - O(n)
- Delete: `arr.erase(pos)` - O(n)
- Push back: `arr.push_back(val)` - O(1) amortized
- Sort: `sort(arr.begin(), arr.end())` - O(n log n)

## String Operations
- Length: `str.length()` - O(1)
- Substring: `str.substr(start, len)` - O(len)
- Find: `str.find(substr)` - O(n*m)
- Compare: `str.compare(other)` - O(n)

## HashMap
- Insert: `mp[key] = val` - O(1) avg
- Find: `mp.find(key)` - O(1) avg
- Erase: `mp.erase(key)` - O(1) avg
- Iterate: `for(auto [k,v] : mp)` - O(n)

## Vector Methods
- `push_back()` - Add to end
- `pop_back()` - Remove from end
- `insert(it, val)` - Insert at iterator
- `erase(it)` - Remove at iterator
- `clear()` - Remove all
- `size()` - Get size
- `empty()` - Check if empty

## Set Operations
- Insert: `s.insert(val)` - O(log n)
- Find: `s.find(val)` - O(log n)
- Erase: `s.erase(val)` - O(log n)
- Iterate: `for(int x : s)` - O(n)

## Queue Operations
- Enqueue: `q.push(val)` - O(1)
- Dequeue: `q.pop()` - O(1)
- Front: `q.front()` - O(1)
- Empty: `q.empty()` - O(1)

## Stack Operations
- Push: `st.push(val)` - O(1)
- Pop: `st.pop()` - O(1)
- Top: `st.top()` - O(1)
- Empty: `st.empty()` - O(1)

## Priority Queue
- Push: `pq.push(val)` - O(log n)
- Pop: `pq.pop()` - O(log n)
- Top: `pq.top()` - O(1)
- Min heap: `priority_queue<int, vector<int>, greater<int>> pq`

## Tree Node
```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
```

## Linked List Node
```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

## Common Algorithms

### Binary Search
```cpp
int left = 0, right = n - 1;
while(left <= right) {
    int mid = left + (right - left) / 2;
    if(arr[mid] == target) return mid;
    else if(arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
return -1;
```

### Merge Sort
Time: O(n log n), Space: O(n)

### Quick Sort
Time: O(n log n) avg, O(n²) worst, Space: O(log n)

### Bubble Sort
Time: O(n²), Space: O(1)

## Complexity Cheat Sheet

| Complexity | Range for n |
|-----------|------------|
| O(1) | Any |
| O(log n) | n < 10^9 |
| O(n) | n < 10^8 |
| O(n log n) | n < 10^6 |
| O(n²) | n < 5000 |
| O(n³) | n < 500 |
| O(2^n) | n < 25 |
| O(n!) | n < 12 |

## STL Frequently Used

```cpp
#include <bits/stdc++.h>
using namespace std;

// Sorting
sort(arr.begin(), arr.end());
sort(arr.begin(), arr.end(), greater<int>());

// Min/Max
int minVal = *min_element(arr.begin(), arr.end());
int maxVal = *max_element(arr.begin(), arr.end());

// Sum
int sum = accumulate(arr.begin(), arr.end(), 0);

// Reverse
reverse(arr.begin(), arr.end());

// Find
auto it = find(arr.begin(), arr.end(), value);

// Count
int cnt = count(arr.begin(), arr.end(), value);

// Unique (remove duplicates)
arr.erase(unique(arr.begin(), arr.end()), arr.end());
```

## Two-Dimensional Arrays
```cpp
// Declaration
vector<vector<int>> matrix(rows, vector<int>(cols, 0));

// Accessing
matrix[i][j]

// Iteration
for(int i = 0; i < rows; i++) {
    for(int j = 0; j < cols; j++) {
        // Process
    }
}
```

## Tips & Tricks

1. **Initialize properly** - `vector<int> dp(n, -1)` for memoization
2. **Use 0-indexing** - Most algorithms use 0-based indexing
3. **Check boundaries** - Always check `i >= 0 && i < n`
4. **Use long long** - For large numbers or products
5. **Prefix sums** - Fast range queries
6. **Modulo arithmetic** - `(a + b) % MOD` for large answers
7. **2D prefix sum** - `prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]`
8. **Early termination** - Exit loop early when possible

## Common Pitfalls

- ❌ Integer overflow - Use `long long`
- ❌ Off-by-one errors - Careful with loop bounds
- ❌ Not checking edge cases - Empty arrays, single elements
- ❌ Wrong comparison in sorting - Check if ascending/descending
- ❌ Modifying during iteration - Create copy if needed
- ❌ NULL pointer access - Check `ptr != NULL`
- ❌ Forgetting base case in recursion - Always add base case

