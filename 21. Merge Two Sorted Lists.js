/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    dummy = new ListNode(-1);
    p = dummy;
    while (l1 !== null && l2 !== null)
    {
        var temp = null;
        if (l1.val < l2.val)
        {
            temp = l1;
            l1 = l1.next;
        }
        else
        {
            temp = l2;
            l2 = l2.next;
        }
        p.next = temp;
        p = temp;
    }
    if (l1 !== null)
        p.next = l1;
    if (l2 !== null)
        p.next = l2;
    return dummy.next;
};
