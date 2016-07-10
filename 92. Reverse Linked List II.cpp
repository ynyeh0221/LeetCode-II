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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* p = dummy;
        for (int i = 1; i < m; i++)
        {
            head = head->next;
            p = p->next;
        }
        ListNode* nextnode = NULL;
        ListNode* reverse_end = NULL;
        for (int i = m; i <= n; i++)
        {
            if (i == m)
                reverse_end = head;
            ListNode* temp = head;
            head = head->next;
            temp->next = nextnode;
            p->next = temp;
            nextnode = temp;
        }
        reverse_end->next = head;
        return dummy->next;
    }
};
