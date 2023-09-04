/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        vector<ListNode*> set; // Use vector of ListNode pointers
        while (head) {
            for (int i = 0; i < set.size(); i++) {
                if (set[i] == head) // Compare pointers, not values
                    return true;
            }
            set.push_back(head);
            head = head->next; // Use -> to access member variables/methods of pointers
        }
        return false; // Return false if no cycle is found
    }
};