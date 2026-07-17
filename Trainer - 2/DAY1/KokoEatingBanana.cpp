#include<bits/stdc++.h>
using namespace std;

int minEatingSpeed(vector<int> &piles, int h) {
    int left = 1;
    int right = *max_element(piles.begin(), piles.end());

    int answer = right;

    while(left <= right) {
        int mid = left + (right - left) / 2;

        long long totalHours = 0;

        for(int i = 0; i < piles.size(); i++) {
            totalHours = totalHours + (piles[i] + mid - 1) / mid;
        }
        // Check The values
        if(totalHours <= h) {
            answer = mid;
            right = mid - 1; // Try Small Speed;
        }else{
            left = mid + 1; // Increase Speed
        }
    }
    return answer;
}


int main() {
    vector<int> piles{3, 6, 7, 11};
    int h = 8;
    
    cout<<minEatingSpeed(piles, h);
}