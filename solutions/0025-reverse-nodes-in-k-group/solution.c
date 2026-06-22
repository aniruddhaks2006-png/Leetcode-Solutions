/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (head == NULL || k == 1)
        return head;

    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *prevGroup = &dummy;
    while (1) {
        struct ListNode *kth = prevGroup;
        for (int i = 0; i < k && kth != NULL; i++)
            kth = kth->next;
        if (kth == NULL)
            break;  
        struct ListNode *groupNext = kth->next;
        struct ListNode *prev = groupNext;
        struct ListNode *curr = prevGroup->next;
        while (curr != groupNext) {
            struct ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        struct ListNode *temp = prevGroup->next;
        prevGroup->next = kth;
        prevGroup = temp;
    }
    return dummy.next;
}
