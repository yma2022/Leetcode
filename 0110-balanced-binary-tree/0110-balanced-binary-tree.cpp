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
    int getHeight(TreeNode* node){
        if (!node) return 0;
        if (getHeight(node->left) == -1 || getHeight(node->right) == -1 || abs(getHeight(node->left) - getHeight(node->right)) > 1) return -1;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
    bool isBalanced(TreeNode* root) {
        return getHeight(root) != -1;
    }
};