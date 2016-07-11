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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* p = dummy;
        while (head != NULL)
        {
            if (head->val == val)
            {
                p->next = head->next;
                head = head->next;
            }
            else
            {
                head = head->next;
                p = p->next;
            }
        }
        return dummy->next;
    }
};
