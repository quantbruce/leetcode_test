//方法1
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int target) 
    {
        vector<vector<int>> res;
        vector<int> path;
        recur(root, target, path, res);
        return res;
    }

private:
    void recur(TreeNode* root, int tar, vector<int> &path, vector<vector<int>> &res)
    {
        if(!root) return;
        path.push_back(root->val);
        tar -= root->val;
        if(tar==0 && !root->left && !root->right)
        {
            res.push_back(path);
        }
        recur(root->left, tar, path, res);
        recur(root->right, tar, path, res);
        path.pop_back();
    }
};
