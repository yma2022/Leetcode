class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result(nums.size());
        int left = 0;
        int right = nums.size() - 1;
        int k = nums.size() - 1;
        for (; k>= 0; k--){
            if (nums[right] * nums[right] >= nums[left] * nums[left]){
                result[k] = nums[right] * nums[right];
                right--;
            }
            else{
                result[k] = nums[left] * nums[left];
                left++;
            }
        }
        return result;
        
    }
};