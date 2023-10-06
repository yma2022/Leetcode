class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        int l = 1;
        int r = x / 2;

        while (l <= r) {
            int m = r - (r - l) / 2;
            if (m > x / m) r = m - 1;
            else if (m < x / m) l = m + 1;
            else return m;
        }
        return r;      
    }
};