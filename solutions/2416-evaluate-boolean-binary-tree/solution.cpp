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
          bool bood(TreeNode *de) {
        if (de==NULL)
            return false;
        if (de->val==0 || de->val==1)
            return de->val;
        if(de->val==2)
            return bood(de->left) || bood(de->right);
        if(de->val==3)
            return bood(de->left)*bood(de->right);
        return false;
    };
    bool evaluateTree(TreeNode* root) {
        return bood(root);
    }
};
