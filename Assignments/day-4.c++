
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }
};



class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast)
                return true;
        }

        return false;
    }
};



class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        // Step 1: detect cycle
        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast) {
                // Step 2: find start
                ListNode* temp = head;

                while(temp != slow) {
                    temp = temp->next;
                    slow = slow->next;
                }

                return temp;
            }
        }

        return NULL;
    }
};