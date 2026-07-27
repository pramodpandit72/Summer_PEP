// #include<bits/stdc++.h>
// using namespace std;

// int minRoom(vector<vector<int>>& arr) {
//     int n = arr.size();
//     int ans = 0;

//     for (int i = 0; i < n; i++) {
//         int rooms = 1;

//         for (int j = 0; j < n; j++) {
//             if (i != j) {
//                 if (arr[i][0] < arr[j][1] &&
//                     arr[j][0] < arr[i][1]) {
//                     rooms++;
//                 }
//             }
//         }

//         ans = max(ans, rooms);
//     }

//     return ans;
// }

// int main() {
//     vector<vector<int>> arr = {
//         {0, 30},
//         {5, 10},
//         {15, 20}
//     }; 
//     cout<<minRoom(arr);

//     return 0;
// }


// Question 1:

#include <bits/stdc++.h>
using namespace std;

int minRoom(vector<vector<int>>& intervals) {
    if (intervals.empty()) {
        return 0;
    }

    sort(intervals.begin(), intervals.end());
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(intervals[0][1]);

    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i][0] >= pq.top()) {
            pq.pop();
        }

        pq.push(intervals[i][1]);
    }

    return pq.size();
}

int main() {
    vector<vector<int>> arr = {
        {0, 30},
        {5, 10},
        {15, 20}
    };
    cout << minRoom(arr);

    return 0;
}


// #include<bits/stdc++.h>
// using namespace std;

// int solve(vector<vector<int>> &arr, int i, int j) {
//    int m = arr.size();
//    int n = arr[0].size();

//    if(i == m - 1 && j == n - 1) {
//     return arr[i][j];
//    }
//    if(i >= m || j >= n) {
//     return INT_MAX;
//    }

//    int right = solve(arr, i, j + 1);
//    int down = solve(arr, i + 1, j);

//    return arr[i][j] + min(right, down);
 
// }

// int minSum(vector<vector<int>> grid) {
//     return solve(grid, 0, 0);
// }

// int main() {

//     vector<vector<int>> arr = {
//         {1,3,1},
//         {1,5,1},
//         {4,2,1}
//     };

//     cout<<minSum(arr);

//     return 0;
// }


// Question 2:

#include<bits/stdc++.h>
using namespace std;

int minSum(vector<vector<int>> &arr) {
    int m = arr.size();
    int n = arr[0].size();
    vector<vector<int>> dp(m, vector<int> (n, 0));

    dp[0][0] = arr[0][0];

    for(int i = 1; i < m; i++) {
        dp[i][0] = arr[i][0] + dp[i - 1][0];
    }

    for(int i = 1; i < n; i++) {
        dp[0][i] = arr[0][i] + dp[0][i - 1];
    }

    for(int i = 1; i < m; i++) {
        for(int j = 1; j < n; j++) {
            dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m - 1][n - 1];
    
}

int main() {
    vector<vector<int>> arr = {
        {1,3,1},
        {1,5,1},
        {4,2,1}
    };

    cout<<minSum(arr);

    return 0;
}






// Question 3:

#include<bits/stdc++.h>
using namespace std;

bool dfs(vector<vector<char>>& board, string &word, int i, int j, int index){
    int m = board.size();
    int n = board[0].size();

    if(index == word.size()){
        return true;
    }

    if(i < 0 || j < 0 || i >= m || j >= n || board[i][j] != word[index]){
        return false;
    }

    char temp = board[i][j];
    board[i][j] = '#';

    bool found =
        dfs(board, word, i+1, j, index+1) ||
        dfs(board, word, i-1, j, index+1) ||
        dfs(board, word, i, j+1, index+1) ||
        dfs(board, word, i, j-1, index+1);

    board[i][j] = temp;

    return found;
}

bool exist(vector<vector<char>>& board, string word) {
    int m = board.size();
    int n = board[0].size();

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(dfs(board, word, i, j, 0))
                return true;
        }
    }
    return false;
}

int main() {
    vector<vector<char>> arrboard = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word = "ABCCED";

    cout<<exist(arrboard, word);

    return 0;
}