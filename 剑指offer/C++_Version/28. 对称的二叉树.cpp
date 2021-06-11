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
    bool isSymmetric(TreeNode* root)
    {
        return mirror(root, root);
    }

private:
    bool mirror(TreeNode *node1, TreeNode *node2)
    {
        if(!node1 && !node2) return true;
        if(!node1 || !node2) return false;
        return (node1->val==node2->val) && mirror(node1->left, node2->right) && \
        mirror(node1->right, node2->left);
    }
};



//方法2
class Solution {
public:
    bool isSymmetric(TreeNode* root) 
    {
        if(!root) return true;
        stack<TreeNode*> stack;
        stack.push(root->left);
        stack.push(root->right);
        while(!stack.empty())
        {
            TreeNode *node1 = stack.top();
            stack.pop();
            TreeNode *node2 = stack.top();
            stack.pop();
            if(!node1 && !node2) continue;
            if(!node1 || !node2 || node1->val!=node2->val) return false;
            stack.push(node1->left);
            stack.push(node2->right);
            stack.push(node1->right);
            stack.push(node2->left);
        }
        return true;
    }
};

