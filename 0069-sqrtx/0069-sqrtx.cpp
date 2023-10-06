class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        int left = 1;
        int right = x / 2;
        while (left <= right){
            int mid = right - (right - left) / 2;
            if ((long) mid * mid > x) right = mid - 1;
            else if ((long) mid * mid < x) left = mid + 1;
            else return mid;
        }
        return right;        
    }
};