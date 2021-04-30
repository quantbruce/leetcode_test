//方法1

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size()==0) 
            return NULL;

        TreeNode *node = new TreeNode(preorder[0]);
        int idx;
        while(inorder[idx]!=node->val)
            idx++;

        vector<int> left_pre(preorder.begin()+1, preorder.begin()+idx+1);
        vector<int> left_in(inorder.begin(), inorder.begin()+idx);

        vector<int> right_pre(preorder.begin()+idx+1, preorder.end());
        vector<int> right_in(inorder.begin()+idx+1, inorder.end());

        node->left = buildTree(left_pre, left_in);
        node->right = buildTree(right_pre, right_in);

        return node;
    }
};
