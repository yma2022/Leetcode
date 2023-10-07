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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> st;
        for(int num:nums)
        {
            TreeNode* cur = new TreeNode(num);
            while(!st.empty() && st.back()->val < num)
            {
                cur->left = st.back();
                st.pop_back();
            }
            if(!st.empty()) st.back()->right = cur;
            st.push_back(cur);
        }
        return st.front();
//         if (!nums.size()) return NULL;
//         int idx = 0;
//         int rootVal = 0;
//         for (int i = 0; i < nums.size(); i++){
//             if (nums[i] > rootVal){
//                 rootVal = nums[i];
//                 idx = i;
//             }
//         }
        
//         TreeNode* root = new TreeNode(rootVal);
//         vector<int> leftNums(nums.begin(), nums.begin() + idx);
//         vector<int> rightNums(nums.begin() + idx + 1, nums.end());
        
//         root->left = constructMaximumBinaryTree(leftNums);
//         root->right = constructMaximumBinaryTree(rightNums);
//         return root;
        
    }
};