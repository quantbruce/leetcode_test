//方法1
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) 
    {
        vector<int> res;
        queue<TreeNode*> que;
        que.push(root);

        if(!root) return res;
        while(!que.empty())
        {
            TreeNode *node = que.front();
            que.pop();
            if(node->left) 
                que.push(node->left);
            if(node->right) 
                que.push(node->right);
            res.push_back(node->val);
        }
        return res;
    }
};
