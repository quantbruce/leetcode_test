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
    bool isSubStructure(TreeNode* A, TreeNode* B)
    {
        return bool(A && B) && \
        (recur(A, B) || isSubStructure(A->left, B) || (isSubStructure(A->right, B)));
    }

private:
    bool recur(TreeNode* A, TreeNode* B)
    {
        if(B==NULL) return true;
        if(A==NULL || A->val!=B->val) return false;
        return recur(A->left, B->left) && recur(A->right, B->right);
    }
};
