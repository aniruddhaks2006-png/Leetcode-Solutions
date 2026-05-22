/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
       struct ListNode *p=head;
        struct ListNode *q=head;
        int size=0,quiz=0;
        while(p!=NULL)
        {
            size++;
            p=p->next;

        
        }
        int nin=size-n;
        if(nin==0){
            return head->next;
        }
        while(q!=NULL)
        { quiz++;
          if(quiz==nin)
            {
                q->next=q->next->next;
                return head;
            }
        q=q->next;    
        }
    return NULL;
}
