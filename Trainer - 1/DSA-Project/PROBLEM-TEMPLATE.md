# Problem-Solving Template

Use this template when solving any DSA problem:

```cpp
// Problem: [Problem Name]
// Platform: [LeetCode/Codeforces/GeeksForGeeks]
// Problem ID: [#123]
// Topic: [Topic Name]
// Difficulty: [Easy/Medium/Hard]
// Date Solved: [Date]

/**
 * Approach: [Brief description of the approach]
 * 
 * Algorithm:
 * 1. [Step 1]
 * 2. [Step 2]
 * 3. [Step 3]
 * 
 * Time Complexity: O(...)
 * Space Complexity: O(...)
 * 
 * Key Insights:
 * - Insight 1
 * - Insight 2
 * 
 * Similar Problems:
 * - Problem X (LC #123)
 * - Problem Y (CF #456)
 */

#include <bits/stdc++.h>
using namespace std;

// Solution code here
int solve() {
    // Implementation
}

// Test cases
int main() {
    // Test case 1
    // Expected output:
    
    // Test case 2
    // Expected output:
    
    return 0;
}
```

---

## Problem Analysis Checklist

### 1. Understanding
- [ ] What is the input? Format and constraints?
- [ ] What is the output? Exact requirements?
- [ ] What are edge cases? Empty, single element, duplicates?
- [ ] What are constraints? Time/space limits? Data ranges?

### 2. Approach Selection
- [ ] What pattern does this match? (Sliding window, DP, BFS, etc.)
- [ ] What data structures fit best? (Array, HashMap, Tree, Graph, etc.)
- [ ] What's the brute force approach? (Even if not optimal)
- [ ] How can we optimize from brute force?

### 3. Complexity Analysis
- [ ] What's the time complexity of my approach?
- [ ] What's the space complexity?
- [ ] Are these within constraints?
- [ ] Can I optimize further?

### 4. Implementation
- [ ] Code cleanly with good variable names
- [ ] Add comments for complex logic
- [ ] Test with provided examples first
- [ ] Test edge cases: empty, single, duplicates, boundaries
- [ ] Check for integer overflow, off-by-one errors

### 5. Optimization (if needed)
- [ ] Reduce constant factors
- [ ] Use better data structures
- [ ] Apply advanced algorithms
- [ ] Trade time for space or vice versa

### 6. Finalization
- [ ] Code is readable and maintainable
- [ ] Comments explain non-obvious logic
- [ ] Solution handles all edge cases
- [ ] Complexity is optimal or near-optimal

---

## Common Patterns Quick Reference

| Pattern | Use Case | Complexity |
|---------|----------|-----------|
| Sliding Window | Fixed/Variable window sub-problems | O(n) |
| Two Pointers | Sorted array, meeting points | O(n) |
| Binary Search | Sorted data, search space | O(log n) |
| HashMap/HashSet | Counting, lookups, grouping | O(n) |
| DFS | Connected components, paths | O(V+E) |
| BFS | Shortest path, level-wise | O(V+E) |
| DP | Overlapping subproblems | Varies |
| Greedy | Optimal local choice | Varies |
| Backtracking | All permutations/combinations | Varies |
| Union-Find | Connected components | O(α(n)) |

---

## Template Code Snippets

### Sliding Window
```cpp
int slidingWindow(vector<int>& arr, int k) {
    int n = arr.size();
    int result = 0;
    int current = 0;
    
    // Build first window
    for(int i = 0; i < k; i++) {
        current += arr[i];
    }
    result = current;
    
    // Slide the window
    for(int i = k; i < n; i++) {
        current = current - arr[i-k] + arr[i];
        result = max(result, current);
    }
    return result;
}
```

### Two Pointers
```cpp
void twoPointers(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    
    while(left < right) {
        int sum = arr[left] + arr[right];
        if(sum == target) {
            // Found
            return;
        } else if(sum < target) {
            left++;
        } else {
            right--;
        }
    }
}
```

### DFS Recursion
```cpp
void dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    
    for(int neighbor : adj[node]) {
        if(!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}
```

### BFS Queue
```cpp
void bfs(int start, vector<vector<int>>& adj) {
    queue<int> q;
    vector<bool> visited(adj.size(), false);
    
    q.push(start);
    visited[start] = true;
    
    while(!q.empty()) {
        int node = q.front();
        q.pop();
        
        for(int neighbor : adj[node]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
```

---

## Debugging Tips

1. **Print statements** - Add debug output for intermediate values
2. **Edge cases** - Test with empty, single element, max/min values
3. **Off-by-one** - Check loop bounds carefully
4. **Initialization** - Ensure variables are properly initialized
5. **Data types** - Watch for integer overflow
6. **Comparison** - Careful with floating-point comparisons

