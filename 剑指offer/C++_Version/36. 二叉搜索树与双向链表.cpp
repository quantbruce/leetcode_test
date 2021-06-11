/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    
public:
    Node* treeToDoublyList(Node* root) 
    {
        if(!root) return NULL;
        dfs(root);
        pre->right = head;
        head->left = pre;
        return head;
    }

private:
    Node *pre, *head;
    void dfs(Node* cur)
    {
        if(!cur) return;
        dfs(cur->left);
        if(pre)
        {
            pre->right = cur;
            cur->left = pre;
        }
        else
        {
            head = cur;
        }
        pre = cur;
        dfs(cur->right);
    }

};
