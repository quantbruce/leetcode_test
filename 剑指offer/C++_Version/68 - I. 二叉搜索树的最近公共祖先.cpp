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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
    {
        if(root->val<p->val && root->val<q->val)
            return lowestCommonAncestor(root->right, p, q);
        else if(root->val > p->val && root->val > q->val)
            return lowestCommonAncestor(root->left, p, q);
        return root;    
    }
};



//方法2
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
    {
        TreeNode* res;
        if(p->val < q->val)
        {
            TreeNode* tmp = p;
            p = q;
            q = tmp;
        }
        while(root!=nullptr)
        {
            if(root->val > p->val)
                root = root->left;
            else if(root->val < q->val)
                root = root->right;
            else
                return root;
        }
        return root;
    }
};
