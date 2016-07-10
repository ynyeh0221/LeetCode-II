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
    ListNode* reverseList(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        ListNode* nextnode = NULL;
        while (head)
        {
            ListNode* temp = head;
            head = head->next;
            temp->next = nextnode;
            dummy->next = temp;
            nextnode = temp;
        }
        return dummy->next;
    }
};
