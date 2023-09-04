/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(!head || !head->next)
        return false;
    struct ListNode *slow;
    struct ListNode *fast;
    slow = head;
    fast = head->next;
    while(slow != fast){
        if(!fast || !fast->next)
            return false;
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}