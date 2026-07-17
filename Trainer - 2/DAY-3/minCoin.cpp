// Problem: minimun number of coin
#include<bits/stdc++.h>
using namespace std;

int minCoin(int n) {
    vector<int> coin{100, 50, 20, 10, 5, 2, 1};
    int total = 0;

    for(int i = 0; i < coin.size(); i++) {
        total = total + (n / coin[i]);
        n = n % coin[i];

        
        if(n == 0) {
            break;
        }
    }
    return total;

}

int main() {
    
    // int n;  // 242  o/p: 5
    // cout<<"Enter the number: ";
    // cin>>n;
    
    cout<<minCoin(1000);
}