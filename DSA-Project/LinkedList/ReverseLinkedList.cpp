// Problem: Reverse Linked List
// LeetCode #206
// Topic: Linked List
// Difficulty: Easy

#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Approach 1: Iterative Reversal
// Time: O(n), Space: O(1)
ListNode* reverseListIterative(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* current = head;
    
    while(current) {
        ListNode* nextTemp = current->next;  // Save next node
        current->next = prev;                 // Reverse the link
        prev = current;                       // Move prev forward
        current = nextTemp;                   // Move current forward
    }
    
    return prev;
}

// Approach 2: Recursive Reversal
// Time: O(n), Space: O(n) [recursion stack]
ListNode* reverseListRecursive(ListNode* head) {
    // Base case: empty or single node
    if(!head || !head->next) return head;
    
    // Reverse the rest of the list
    ListNode* newHead = reverseListRecursive(head->next);
    
    // Put first element at the end
    head->next->next = head;
    head->next = NULL;
    
    return newHead;
}

// Helper function to print list
void printList(ListNode* head) {
    while(head) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// Example Usage
int main() {
    // Create list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    
    cout << "Original: ";
    printList(head);
    
    head = reverseListIterative(head);
    cout << "Reversed: ";
    printList(head);
    
    return 0;
}
