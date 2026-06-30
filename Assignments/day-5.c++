#include <bits/stdc++.h>
using namespace std;

1. Valid Parentheses (Basic) 
Problem:
Given a string containing (), {}, and [], check whether the parentheses are balanced.
Example:
Input: "()[]{}"
Output: True

Input: "(]"
Output: False
Concepts Used:
•	Push opening brackets. 
•	Pop and match when a closing bracket appears. 
________________________________________
2. Next Greater Element (Easy-Medium) 
Problem:
For every element in an array, find the first greater element on its right. If none exists, print -1.
Example:
Input:
[4, 5, 2, 10]

Output:
5 10 10 -1
Concepts Used:
•	Monotonic Stack 
•	Traverse from right to left. 
________________________________________
3. Largest Rectangle in Histogram (Medium) 
Problem:
Given heights of histogram bars, find the area of the largest rectangle.
Example:
Input:
[2, 1, 5, 6, 2, 3]

Output:
10
Explanation:
The largest rectangle is formed by bars of height 5 and 6.


    bool isValid(string s) {
        stack<char> st;

        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (st.empty())
                    return false;

                if ((ch == ')' && st.top() != '(') ||
                    (ch == '}' && st.top() != '{') ||
                    (ch == ']' && st.top() != '['))
                    return false;

                st.pop();
            }
        }

        return st.empty();
    }


        vector<int> nextGreaterElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        stack<int> st;

        for (int i = n - 1; i >= 0; i--) {

            while (!st.empty() && st.top() <= nums[i]) {
                st.pop();
            }

            if (!st.empty())
                ans[i] = st.top();

            st.push(nums[i]);
        }

        return ans;
    }


        int largestRectangleArea(vector<int>& heights) {

        stack<int> st;
        int n = heights.size();
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {

            while (!st.empty() && (i == n || heights[st.top()] >= heights[i])) {

                int height = heights[st.top()];
                st.pop();

                int width;

                if (st.empty())
                    width = i;
                else
                    width = i - st.top() - 1;

                maxArea = max(maxArea, height * width);
            }

            st.push(i);
        }

        return maxArea;
    }