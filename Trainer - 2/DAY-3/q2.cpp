// Problem: SubscriptionRenewalWindow

#include<bits/stdc++.h>
using namespace std;

int SubscriptionRenewalWindow(vector<int>& nums,int k) {
    int n = nums.size();
    int maxSize = 0;
    int left = 0, right = 0;

    while(left < n && right < n) {
        if(nums[right] - nums[left] <= k) {
            maxSize = max(maxSize, right - left + 1);
            right++;
        }else{
            left++;
        }
    }
    return maxSize;

    // int left = 0;
    // int maxSize = 0;
    // for(int right = 0; right < nums.size(); right++) {
    //     if(nums[right] - nums[left] > k) {
    //         left++;
    //     }
    //     maxSize = max(maxSize, right - left + 1);
    // }
    // return maxSize;
}

int main() {  
    // int n;  // 242  o/p: 5
    // cout<<"Enter the number: ";
    // cin>>n;
    vector<int> nums{1, 3, 5, 7, 9};
    int k = 4;
    
    cout<<SubscriptionRenewalWindow(nums, k);
}