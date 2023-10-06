class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 2) return true;
        long left = 1;
        long right = num / 2;
        
        while (left <= right){
            long mid = right - (right - left) / 2;
            long guess = mid * mid;
            if (guess > num) right = mid - 1;
            else if (guess < num) left = mid + 1;
            else return true;
        }
        return false;
        
    }
};