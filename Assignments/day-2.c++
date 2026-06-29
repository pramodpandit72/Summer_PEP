#include<bits/stdc++.h>
using namespace std;

int MaxSubarraySum(vector<int> arr) {
    int currSum = 0;
    int maxSum = INT_MIN;

    for(int x : arr) {
        currSum += x;

        maxSum = max(maxSum, currSum);

        if(currSum < 0){
            currSum = 0;
        }
    }
    return maxSum;
}

int MaxSum(vector<int> arr, int k) {
    int wSum = 0;

    for(int i = 0; i < k; i++) {
        wSum += arr[i]; 
    }

    int maxSum = wSum;

    for(int i = k; i < arr.size(); i++) {
        wSum += arr[i];
        wSum -= arr[i - k];

        maxSum = max(maxSum, wSum);
    }
    return maxSum;
}