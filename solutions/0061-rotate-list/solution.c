struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL || k == 0)
        return head;
    int len = 1;
    struct ListNode *tail = head;
    while (tail->next) {
        tail = tail->next;
        len++;
    }
    k %= len;
    if (k == 0)
        return head;
    struct ListNode *p = head;
    for (int i = 0; i < len - k - 1; i++) {
        p = p->next;
    }
    struct ListNode *q = p->next;
    p->next = NULL;
    tail->next = head;
    return q;
}
