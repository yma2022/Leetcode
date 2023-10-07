class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right){
            while (left <= right && nums[right] == val) --right;
            while (left <= right && nums[left] != val) left++;
            if (left < right){
                nums[left] = nums[right];
                left++;
                right--;
            }            
        }
        return left;
    }
};