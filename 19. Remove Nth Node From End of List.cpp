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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pl = dummy, *pf = head;
        for (int i = 0; i < n; i++)
            pf = pf->next;
        while (pf != NULL)
        {
            pl = pl->next;
            pf = pf->next;
        }
        pl->next = pl->next->next;
        return dummy->next;
    }
};
