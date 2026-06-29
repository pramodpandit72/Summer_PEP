// Problem: Climbing Stairs
// LeetCode #70
// Topic: Dynamic Programming
// Difficulty: Easy

#include <bits/stdc++.h>
using namespace std;

// Approach 1: Top-Down DP (Memoization)
// Time: O(n), Space: O(n)
int climbStairsMemo(int n, vector<int>& memo) {
    // Base cases
    if(n == 1) return 1;
    if(n == 2) return 2;
    
    // Check memo
    if(memo[n] != -1) return memo[n];
    
    // Recurrence: ways to reach n = ways to reach (n-1) + ways to reach (n-2)
    memo[n] = climbStairsMemo(n-1, memo) + climbStairsMemo(n-2, memo);
    return memo[n];
}

// Approach 2: Bottom-Up DP (Tabulation)
// Time: O(n), Space: O(n)
int climbStairsTabulation(int n) {
    if(n == 1) return 1;
    if(n == 2) return 2;
    
    vector<int> dp(n+1);
    dp[1] = 1;
    dp[2] = 2;
    
    for(int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}

// Approach 3: Space-Optimized DP
// Time: O(n), Space: O(1)
int climbStairsOptimized(int n) {
    if(n == 1) return 1;
    if(n == 2) return 2;
    
    int prev2 = 1;  // ways to reach step 1
    int prev1 = 2;  // ways to reach step 2
    
    for(int i = 3; i <= n; i++) {
        int current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}

// Example Usage
int main() {
    int n = 5;
    
    // Using memoization
    vector<int> memo(n+1, -1);
    cout << "Memoization: " << climbStairsMemo(n, memo) << endl;
    
    // Using tabulation
    cout << "Tabulation: " << climbStairsTabulation(n) << endl;
    
    // Using space-optimized
    cout << "Space-Optimized: " << climbStairsOptimized(n) << endl;
    
    // For n=5, output should be 8
    // Paths: (1+1+1+1+1), (1+1+1+2), (1+1+2+1), (1+2+1+1), (2+1+1+1)
    //        (1+2+2), (2+1+2), (2+2+1)
    
    return 0;
}
