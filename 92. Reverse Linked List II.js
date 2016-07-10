/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    dummy = new ListNode(-1);
    dummy.next = head;
    p = dummy;
    for (var i = 1; i < m; i++)
    {
        head = head.next;
        p = p.next;
    }
    nextnode = null;
    reverse_end = null;
    for (i = m; i <= n; i++)
    {
        if (i == m)
            reverse_end = head;
        var temp = head;
        head = head.next;
        temp.next = nextnode;
        p.next = temp;
        nextnode = temp;
    }
    reverse_end.next = head;
   
