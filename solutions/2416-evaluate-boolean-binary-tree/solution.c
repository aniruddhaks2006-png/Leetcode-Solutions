/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool evaluateTree(struct TreeNode* root) {
    bool bood(struct TreeNode *de){
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
    return bood(root);
}
