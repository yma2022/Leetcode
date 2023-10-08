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
    int ans = INT_MAX;
    TreeNode *prev = NULL;
    void inorder(TreeNode *root) 
    {
        if(root==NULL)
        {
            return;
        }
        inorder(root->left);
        // if we find at least a node before, we update diff
        if (prev!=NULL)
        {
            int diff = root->val - prev->val;
            ans = min(diff,ans);
        }
        prev = root;
        inorder(root->right);
    }
    int getMinimumDifference(TreeNode *root) 
    {
        inorder(root);
        return ans;
    }
};