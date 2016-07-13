// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        long long int l = 1, r = n;
        while (l <= r)
        {
            long long int mid = (l+r) >> 1;
            if (guess(mid) == 0)
                return mid;
            else if (guess(mid) == 1)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return l;
    }
};
