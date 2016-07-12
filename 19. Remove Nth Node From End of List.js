/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(-1);
    dummy.next = head;
    let pl = dummy, pf = head;
    for (let i = 0; i < n; i++)
        pf = pf.next;
    while (pf !== null)
    {
        pl = pl.next;
        pf = pf.next;
    }
    pl.next = pl.next.next;
    return dummy.next;
};
