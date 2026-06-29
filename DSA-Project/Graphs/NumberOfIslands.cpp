// Problem: Number of Islands
// LeetCode #200
// Topic: Graph - DFS/BFS
// Difficulty: Medium

#include <bits/stdc++.h>
using namespace std;

// Approach: DFS to explore connected components
// Time: O(m*n), Space: O(m*n) [recursion stack]

int numIslandsDFS(vector<vector<char>>& grid) {
    if(grid.empty()) return 0;
    
    int rows = grid.size();
    int cols = grid[0].size();
    int count = 0;
    
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            if(grid[i][j] == '1') {
                dfs(grid, i, j, rows, cols);
                count++;
            }
        }
    }
    
    return count;
}

void dfs(vector<vector<char>>& grid, int i, int j, int rows, int cols) {
    // Boundary check and water check
    if(i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '0') {
        return;
    }
    
    // Mark as visited
    grid[i][j] = '0';
    
    // Explore all 4 directions
    dfs(grid, i+1, j, rows, cols);  // Down
    dfs(grid, i-1, j, rows, cols);  // Up
    dfs(grid, i, j+1, rows, cols);  // Right
    dfs(grid, i, j-1, rows, cols);  // Left
}

// Alternative: BFS Approach
// Time: O(m*n), Space: O(min(m,n)) [queue]
int numIslandsBFS(vector<vector<char>>& grid) {
    if(grid.empty()) return 0;
    
    int rows = grid.size();
    int cols = grid[0].size();
    int count = 0;
    
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            if(grid[i][j] == '1') {
                bfs(grid, i, j, rows, cols);
                count++;
            }
        }
    }
    
    return count;
}

void bfs(vector<vector<char>>& grid, int startI, int startJ, int rows, int cols) {
    queue<pair<int, int>> q;
    q.push({startI, startJ});
    grid[startI][startJ] = '0';
    
    int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    while(!q.empty()) {
        auto [i, j] = q.front();
        q.pop();
        
        for(auto& dir : directions) {
            int ni = i + dir[0];
            int nj = j + dir[1];
            
            if(ni >= 0 && ni < rows && nj >= 0 && nj < cols && grid[ni][nj] == '1') {
                grid[ni][nj] = '0';
                q.push({ni, nj});
            }
        }
    }
}

// Example Usage
int main() {
    vector<vector<char>> grid = {
        {'1', '1', '1', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '0', '0', '0'}
    };
    
    cout << "Number of Islands: " << numIslandsDFS(grid) << endl;  // Output: 1
    
    return 0;
}
