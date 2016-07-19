/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (head === null)
        return [];
    let p = head;
    let length = 1;
    while (p.next !== null)
    {
        length += 1;
        p = p.next;
    }
    p.next = head;
    k %= length;
    for (let i = 0; i < length - k; i ++)
        p = p.next;
    dummy = p.next;
    p.next = null;
    return dummy;
};
