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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(-1);
    ListNode* p = dummy;
    int en = 0;
    while (l1 != NULL && l2 != NULL)
    {
        int temp = l1->val + l2->val + en;
        if (temp <= 9)
        {
            p->next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p->next = new ListNode(temp-10);
            en = 1;
        }
        l1 = l1->next;
        l2 = l2->next;
        p = p->next;
    }
    while (l1 != NULL)
    {
        int temp = l1->val + en;
        if (temp <= 9)
        {
            p->next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p->next = new ListNode(temp-10);
            en = 1;
        }
        l1 = l1->next;
        p = p->next;
    }
    while (l2 != NULL)
    {
        int temp = l2->val + en;
        if (temp <= 9)
        {
            p->next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p->next = new ListNode(temp-10);
            en = 1;
        }
        l2 = l2->next;
        p = p->next;
    }
    if (en == 1)
        p->next = new ListNode(1);
    return dummy->next;
    }
};
