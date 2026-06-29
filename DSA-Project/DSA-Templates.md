# DSA Templates & Patterns

## Common Problem Patterns

### 1. Sliding Window
```cpp
int slidingWindow(vector<int>& nums, int k) {
    int maxSum = 0, currentSum = 0;
    
    // Build first window
    for(int i = 0; i < k; i++) {
        currentSum += nums[i];
    }
    maxSum = currentSum;
    
    // Slide the window
    for(int i = k; i < nums.size(); i++) {
        currentSum = currentSum - nums[i - k] + nums[i];
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}
```

### 2. Two Pointers
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while(left < right) {
        int sum = nums[left] + nums[right];
        if(sum == target) return {left, right};
        else if(sum < target) left++;
        else right--;
    }
    return {};
}
```

### 3. Prefix Sum
```cpp
vector<int> getPrefixSum(vector<int>& nums) {
    vector<int> prefix(nums.size());
    prefix[0] = nums[0];
    for(int i = 1; i < nums.size(); i++) {
        prefix[i] = prefix[i-1] + nums[i];
    }
    return prefix;
}
```

### 4. Binary Search
```cpp
int binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target) return mid;
        else if(nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### 5. Hashing/HashMap
```cpp
vector<int> findPair(vector<int>& nums, int target) {
    unordered_map<int, int> mp;
    
    for(int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if(mp.find(complement) != mp.end()) {
            return {mp[complement], i};
        }
        mp[nums[i]] = i;
    }
    return {};
}
```

---

## Graph Templates

### BFS (Breadth-First Search)
```cpp
vector<int> bfs(vector<vector<int>>& adj, int start) {
    vector<int> result;
    vector<bool> visited(adj.size(), false);
    queue<int> q;
    
    q.push(start);
    visited[start] = true;
    
    while(!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);
        
        for(int neighbor : adj[node]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    return result;
}
```

### DFS (Depth-First Search)
```cpp
void dfs(vector<vector<int>>& adj, int node, vector<bool>& visited, vector<int>& result) {
    visited[node] = true;
    result.push_back(node);
    
    for(int neighbor : adj[node]) {
        if(!visited[neighbor]) {
            dfs(adj, neighbor, visited, result);
        }
    }
}

vector<int> dfsTraversal(vector<vector<int>>& adj) {
    vector<int> result;
    vector<bool> visited(adj.size(), false);
    
    for(int i = 0; i < adj.size(); i++) {
        if(!visited[i]) {
            dfs(adj, i, visited, result);
        }
    }
    return result;
}
```

### Dijkstra's Algorithm
```cpp
vector<int> dijkstra(int n, vector<vector<pair<int, int>>>& adj, int start) {
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    dist[start] = 0;
    pq.push({0, start});
    
    while(!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if(d > dist[u]) continue;
        
        for(auto [v, w] : adj[u]) {
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

---

## Dynamic Programming Templates

### 1D DP (Fibonacci)
```cpp
int fib(int n, vector<int>& dp) {
    if(n <= 1) return n;
    if(dp[n] != -1) return dp[n];
    
    dp[n] = fib(n-1, dp) + fib(n-2, dp);
    return dp[n];
}
```

### 2D DP (Knapsack)
```cpp
int knapsack(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n+1, vector<int>(capacity+1, 0));
    
    for(int i = 1; i <= n; i++) {
        for(int w = 0; w <= capacity; w++) {
            if(weights[i-1] <= w) {
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    return dp[n][capacity];
}
```

### LCS (Longest Common Subsequence)
```cpp
int lcs(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n; j++) {
            if(s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}
```

---

## Tree Templates

### Tree Traversal (DFS)
```cpp
void inorder(TreeNode* root, vector<int>& result) {
    if(!root) return;
    inorder(root->left, result);
    result.push_back(root->val);
    inorder(root->right, result);
}

void preorder(TreeNode* root, vector<int>& result) {
    if(!root) return;
    result.push_back(root->val);
    preorder(root->left, result);
    preorder(root->right, result);
}

void postorder(TreeNode* root, vector<int>& result) {
    if(!root) return;
    postorder(root->left, result);
    postorder(root->right, result);
    result.push_back(root->val);
}
```

### Level Order Traversal (BFS)
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if(!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while(!q.empty()) {
        int size = q.size();
        vector<int> level;
        
        for(int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if(node->left) q.push(node->left);
            if(node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}
```

---

## Important Algorithms

### Merge Sort
```cpp
void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    while(i <= mid && j <= right) {
        if(arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    
    while(i <= mid) temp[k++] = arr[i++];
    while(j <= right) temp[k++] = arr[j++];
    
    for(int i = 0; i < temp.size(); i++) {
        arr[left + i] = temp[i];
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if(left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

### QuickSort
```cpp
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for(int j = low; j < high; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if(low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

---

## Complexity Cheat Sheet

| Operation | Time | Space |
|-----------|------|-------|
| Array Access | O(1) | O(n) |
| Array Search | O(n) | - |
| Binary Search | O(log n) | O(1) |
| Sorting | O(n log n) | O(n) |
| HashMap Operations | O(1) avg | O(n) |
| BFS/DFS | O(V+E) | O(V) |
| Dijkstra | O((V+E)logV) | O(V) |
| DP | Varies | Varies |

