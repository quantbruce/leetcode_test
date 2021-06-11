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
        queue<TreeNode*> que;
        vector<vector<int>> res; 
        if(root==nullptr) return res;
        que.push(root);

        while(!que.empty())
        {   
            int sz = que.size(); // sz是个常数定量，如果不构造这个sz，que.size()后面是动态变化的
            vector<int> ret;
            for(int i=0; i < sz; i++)
            {
                TreeNode *node = que.front();
                que.pop();
                ret.push_back(node->val);
                if(node->left) que.push(node->left);
                if(node->right) que.push(node->right);
            }
            res.push_back(ret);
        }
        return res;
    }
};
