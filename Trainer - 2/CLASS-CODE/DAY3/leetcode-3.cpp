// Problem: LEETCODE 3

#include<bits/stdc++.h>
using namespace std;

int longestUniqueSubstring(string s) {
    unordered_set<char> set;
    int left = 0;
    int maxLen = 0;

    for(int right = 0; right < s.size(); right++) {
        char current = s[right];
        
        while(set.count(current)) {
            set.erase(s[left]);
            left++;
        }
        set.insert(current);
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}

int main() {  
    string s = "abcabc";
    
    cout<<longestUniqueSubstring(s);
}