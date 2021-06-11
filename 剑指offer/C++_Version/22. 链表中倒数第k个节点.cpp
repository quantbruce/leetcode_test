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
    ListNode* getKthFromEnd(ListNode* head, int k)
    {
        ListNode *former = head;
        ListNode *latter = head;
        for(int i=0; i<k; i++)
        {
            former = former->next;
        }
        while(former!=nullptr)
        {
            former = former->next;
            latter = latter->next;
        }
        return latter;
    }
};
