#include<bits/stdc++.h>
using namespace std;

int climb(int n, vector<int>& dp) {

    // base case
    if(n == 0 || n == 1)
        return 1;

    // already calculated
    if(dp[n] != -1)
        return dp[n];

    // store answer
    dp[n] = climb(n-1, dp) + climb(n-2, dp);

    return dp[n];
}

int main() {

    int n = 5;

    vector<int> dp(n + 1, -1);

    cout << climb(n, dp);

    return 0;
}