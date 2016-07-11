/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    var dummy = new ListNode(-1);
    dummy.next = head;
    var p = dummy;
    while (head !== null)
    {
        if (head.val == val)
        {
            p.next = head.next;
            head = head.next;
        }
        else
        {
            head = head.next;
            p = p.next;
        }
    }
    return dummy.next;
};
