class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size(), l = 0, r = n - 1;
        while (l <= r)
        {
            int mid = (l + r) >> 1;
            if (mid == n)
                return n;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return l;
    }
};
