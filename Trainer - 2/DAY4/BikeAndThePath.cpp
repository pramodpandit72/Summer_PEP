#include<bits/stdc++.h>
using namespace std;

int N = 4;

bool findingPath(vector<vector<int>> &maze, int x, int y, string path) {
    // Destination reached
    if(x == N - 1 && y == N - 1) {
        cout<<path<<endl;
        return true;
    }
    //Boundary
    if(x >= N || y >= N || maze[x][y] == 0) {
        return false;
    }
    // Visited
    maze[x][y] = 0;
    // DOWN
    if(findingPath(maze, x + 1, y, path + "D")){
        return true;
    }
    // RIGHT
    if(findingPath(maze, x, y + 1, path + "R")){
        return true;
    }  
    maze[x][y] = 1;
    return false;  
}

int main() {
    vector<vector<int>> maze = {
        {1,0,0,0},
        {1,1,0,1},
        {0,1,0,0},
        {1,1,1,1}
    };

    cout<<findingPath(maze, 0, 0, "")<<endl;


    return 0;
}