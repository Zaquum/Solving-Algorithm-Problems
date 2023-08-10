class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int start = 0, end = nums.size()-1;

        while(start <= end){
            int mid = (start+end)/2;
            
            if(nums[mid]==target)
                return true;
            if(nums[mid]==nums[end]){
                end--;
                continue;
            }
            // left sorted
            if(nums[start] <= nums[mid]){
                if(nums[start]<=target && target<nums[mid])
                    end = mid - 1;
                else
                    start = mid + 1;
            }
            else{
                if(nums[mid]<target && target<=nums[end])
                    start = mid + 1;
                else
                    end = mid - 1;
            }
        }
        return false;
    }
};