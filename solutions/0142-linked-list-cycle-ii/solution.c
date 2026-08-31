/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    int pos=-1;
    struct ListNode* slow=head;
    struct ListNode* fast=head;
    struct ListNode* slow2=head;
    while(fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
        if(slow==fast){
            break;
        }
    }
    if(fast==NULL || fast->next==NULL){
        return NULL;
    }
    pos=0;
    while(slow2!=fast){
        pos++;
        slow2=slow2->next;
        fast=fast->next;
    }
    return slow2;
}
