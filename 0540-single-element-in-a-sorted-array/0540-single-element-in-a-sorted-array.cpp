class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
int low = 0;
        int high = nums.size() - 1;
        
        // Binary search boundary
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            // This trick ensures mid is always even.
            // If mid is odd, (mid ^ 1) gives (mid - 1).
            // If mid is even, (mid ^ 1) gives (mid + 1).
            if (nums[mid] == nums[mid ^ 1]) {
                // Pair is valid, single element is on the right
                low = mid + 1;
            } else {
                // Pair is broken, single element is on the left or is mid
                high = mid;
            }
        }
        return nums[low];
    }
};