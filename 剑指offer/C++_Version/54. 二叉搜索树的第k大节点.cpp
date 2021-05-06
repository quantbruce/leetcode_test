//方法1

class Solution {
public:
    int kthLargest(TreeNode* root, int k) 
    {
        if(root==nullptr)
            return NULL;
        vector<int> res;
        vector<TreeNode*> stack;
        while(root!=nullptr || !stack.empty())
        {
            while(root!=nullptr)
                {
                    stack.push_back(root);
                    root = root->right;
                }
            root = stack.back();
            stack.pop_back();
            res.push_back(root->val);
            if(k==res.size())
                return res[k-1];
            root = root->left;
        }
        return 0;
    }
};
