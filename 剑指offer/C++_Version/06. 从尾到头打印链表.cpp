//方法1

class Solution {
public:
    vector<int> res;
    vector<int> reversePrint(ListNode* head) {
        while(head){
            res.push_back(head->val);
            head = head->next;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};


//方法2

class Solution {
public:
    stack<int> s;
    vector<int> res;
    vector<int> reversePrint(ListNode* head) {
        while(head){
            s.push(head->val);
            head = head->next;
        }
        while(!s.empty()){
            res.push_back(s.top());
            s.pop();
        }
        return res;
    }
};


//方法3

class Solution {
public:
    vector<int> res;
    vector<int> reversePrint(ListNode* head) {
        if(head==nullptr){
            return res;
        }
        reversePrint(head->next);
        res.push_back(head->val);
        return res;
    }
};
