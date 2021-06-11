//方法1
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        ListNode* node1 = headA;
        ListNode* node2 = headB;
        while(node1!=node2)
        {
            if(node1!=nullptr)
                node1 = node1->next;
            else
                node1 = headB;
            if(node2!=nullptr)
                node2 = node2->next;
            else
                node2 = headA;
        }    
        return node1;
    }
};
