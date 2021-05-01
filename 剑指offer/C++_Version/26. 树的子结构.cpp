//

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
        if(!B) return true;
        if(!A || A->val!=B->val) return false;
        return recur(A->left, B->left) && recur(A->right, B->right);
    }
};
