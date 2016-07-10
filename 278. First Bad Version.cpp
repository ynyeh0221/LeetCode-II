// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long int l = 1;
        long long int r = n;
        while (l < r)
        {
            int mid = (l + r) >> 1;
            if (isBadVersion(mid))
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
};
