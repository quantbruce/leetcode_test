//方法1

class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val)
    {
        if(head->val == val)
            return head->next;
            
        ListNode* cur = head;
        ListNode* pre = head->next;

        while(cur!=NULL && cur->val!=val)
        {
            pre = cur;
            cur = cur->next;
        }
        pre->next = cur->next;
        return head;
    }
};
