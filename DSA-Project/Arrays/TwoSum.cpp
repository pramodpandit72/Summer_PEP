// Problem: Two Sum
// LeetCode #1
// Topic: Array - Hashing
// Difficulty: Easy

#include <bits/stdc++.h>
using namespace std;

// Approach: Use HashMap to store complement values
// Time: O(n), Space: O(n)
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp;
    
    for(int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // If complement exists, return indices
        if(mp.find(complement) != mp.end()) {
            return {mp[complement], i};
        }
        
        // Store current number and its index
        mp[nums[i]] = i;
    }
    
    return {};
}

// Example Usage
int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = twoSum(nums, target);
    cout << result[0] << " " << result[1] << endl;  // Output: 0 1
    
    return 0;
}
