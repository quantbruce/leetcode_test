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
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        vector<vector<int>> res;
        if(root==nullptr) return res;
        queue<TreeNode*> que;
        que.push(root);
        while(!que.empty())
        {
            int sz = que.size();
            vector<int> tmp;
            for(int i=0; i<sz; i++)
            {
                TreeNode *node = que.front();
                que.pop();
                tmp.push_back(node->val);
                if(node->left) que.push(node->left);
                if(node->right) que.push(node->right);
            }
            if(res.size()&1)
            {
                reverse(tmp.begin(), tmp.end());
                res.push_back(tmp);
            }
            else
                res.push_back(tmp);
        }
        return res;
    }
};
