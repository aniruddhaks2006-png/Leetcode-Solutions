struct ListNode* partition(struct ListNode* head,int x){
struct ListNode lowerDummy;
struct ListNode higherDummy;
struct ListNode* lower=&lowerDummy;
struct ListNode* higher=&higherDummy;
lower->next=NULL;
higher->next=NULL;
while(head!=NULL){
if(head->val<x){
lower->next=head;
lower=lower->next;
}
else{
higher->next=head;
higher=higher->next;
}
head=head->next;
}
higher->next=NULL;
lower->next=higherDummy.next;
return lowerDummy.next;
}
