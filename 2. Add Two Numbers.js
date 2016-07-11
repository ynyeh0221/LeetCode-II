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
var addTwoNumbers = function(l1, l2) {
    var dummy = new ListNode(-1);
    var p = dummy;
    var en = 0;
    while (l1 !== null && l2 !== null)
    {
        let temp = l1.val + l2.val + en;
        if (temp <= 9)
        {
            p.next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p.next = new ListNode(temp-10);
            en = 1;
        }
        l1 = l1.next;
        l2 = l2.next;
        p = p.next;
    }
    while (l1 !== null)
    {
        let temp = l1.val + en;
        if (temp <= 9)
        {
            p.next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p.next = new ListNode(temp-10);
            en = 1;
        }
        l1 = l1.next;
        p = p.next;
    }
    while (l2 !== null)
    {
        let temp = l2.val + en;
        if (temp <= 9)
        {
            p.next = new ListNode(temp);
            en = 0;
        }
        else
        {
            p.next = new ListNode(temp-10);
            en = 1;
        }
        l2 = l2.next;
        p = p.next;
    }
    if (en == 1)
        p.next = new ListNode(1);
    return dummy.next;
};
