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
    TreeNode* mirrorTree(TreeNode* root)
    {
        if(!root) return nullptr;
        TreeNode* tmp = root->left;
        root->left = mirrorTree(root->right);
        root->right = mirrorTree(tmp);
        return root;
    }
    
};


//方法2
class Solution {
public:
    TreeNode* mirrorTree(TreeNode* root)
    {
        if(root==nullptr) return nullptr;
        stack<TreeNode*> stack;
        stack.push(root);
        while(!stack.empty())
        {
            TreeNode *node = stack.top();
            stack.pop();
            if(node->right) stack.push(node->right);
            if(node->left) stack.push(node->left);
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
        }
        return root;
    }
};


//方法3
class Solution {
public:
    TreeNode* mirrorTree(TreeNode* root)
    {
        if(root==nullptr) return nullptr;
        stack<TreeNode*> stack;
        stack.push(root);
        while(!stack.empty())
        {
            TreeNode *node = stack.top();
            stack.pop();
            if(node->right) stack.push(node->right);
            if(node->left) stack.push(node->left);
            swap(node->left, node->right);
        }
        return root;
    }
};
