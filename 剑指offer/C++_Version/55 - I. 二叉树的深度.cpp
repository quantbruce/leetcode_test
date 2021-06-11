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
    int maxDepth(TreeNode* root) 
    {
        if(!root) return 0;
        queue<TreeNode*> que;
        que.push(root);
        int res = 0;
        while(!que.empty())
        {
            queue<TreeNode*> tmp;
            int sz = que.size();
            for(int i=0; i < sz; i++)
            {   
                TreeNode* node = que.front();
                que.pop();
                if(node->left) tmp.push(node->left);
                if(node->right) tmp.push(node->right);
            }
            que = tmp;
            res++;
        }
        return res;
    }
};
