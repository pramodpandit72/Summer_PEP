#include<bits/stdc++.h>
using namespace std;

string compressString(string s) {
    string ans = "";
    int count = 1;

    for (int i = 0; i < s.size(); i++) {

        if (i + 1 < s.size() && s[i] == s[i + 1]) {
            count++;
        } else {
            ans += s[i];

            if (count > 1){
                ans += to_string(count);
            } 
            count = 1;
        
        }
    }

    return ans;
}

int main() {
    string s;
    cin >> s;

    cout << compressString(s);

    return 0;
}




#include<bits/stdc++.h>
using namespace std;

bool isValid(string s) {
    stack<char> st;

    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
            if (st.empty())
                return false;

            if ((c == ')' && st.top() != '(') ||
                (c == '}' && st.top() != '{') ||
                (c == ']' && st.top() != '[')) {
                    return false;
                } else{
                    st.pop();
                }
        }
    }

    return st.empty();
}

int main() {
    string s;

    cout << "Enter brackets: ";
    cin >> s;

    if (isValid(s))
        cout << "Valid Parentheses" << endl;
    else
        cout << "Invalid Parentheses" << endl;

    return 0;
}





#include<bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) {
        val = x;
        left = nullptr;
        right = nullptr;
    }
};

TreeNode* build(vector<int>& nums, int left, int right) {

    if (left > right) return nullptr;

    int mid = left + (right - left) / 2;

    TreeNode* root = new TreeNode(nums[mid]);

    root->left = build(nums, left, mid - 1);
    root->right = build(nums, mid + 1, right);

    return root;
}

TreeNode* sortedArrayToBST(vector<int>& nums) {
    return build(nums, 0, nums.size() - 1);
}

void inorder(TreeNode* root) {
    if (root == nullptr)
        return;

    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main() {

    vector<int> nums = {-10, -3, 0, 5, 9};

    TreeNode* root = sortedArrayToBST(nums);

    cout << "Inorder Traversal: ";
    inorder(root);

    return 0;
}












// #include <iostream>
// using namespace std;

// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(NULL) {}
// };

// class Solution {
// public:
//     ListNode *detectCycle(ListNode *head) {
//         if (head == NULL || head->next == NULL)
//             return NULL;

//         ListNode *slow = head;
//         ListNode *fast = head;

//         while (fast != NULL && fast->next != NULL) {
//             slow = slow->next;
//             fast = fast->next->next;

//             if (slow == fast) {
//                 slow = head;
//                 while (slow != fast) {
//                     slow = slow->next;
//                     fast = fast->next;
//                 }
//                 return slow;
//             }
//         }
//         return NULL;
//     }
// };

// int main() {
//     // Example: [3,2,0,-4], pos = 1
//     ListNode *head = new ListNode(3);
//     ListNode *second = new ListNode(2);
//     ListNode *third = new ListNode(0);
//     ListNode *fourth = new ListNode(-4);

//     head->next = second;
//     second->next = third;
//     third->next = fourth;
//     fourth->next = second; // Creates cycle

//     Solution obj;
//     ListNode *ans = obj.detectCycle(head);

//     if (ans)
//         cout << "Cycle starts at node with value: " << ans->val << endl;
//     else
//         cout << "No cycle" << endl;

//     return 0;
// }

