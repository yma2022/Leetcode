class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0;
        int right = 0;
        int total = 0;
        int ans = INT32_MAX;
        for(; right < nums.size(); right++){
            total += nums[right];
            while (total >= target){
                int length = right - left + 1;
                ans = ans < length ? ans : length;
                total -= nums[left++];
            }
        }
        return ans == INT32_MAX ? 0 : ans;        
    }
};