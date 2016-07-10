/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var dummy = new ListNode(-1);
    var nextnode = null;
    while (head)
    {
        var temp = head;
        head = head.next;
        temp.next = nextnode;
        dummy.next = temp;
        nextnode = temp;
    }
    return dummy.next;
};
