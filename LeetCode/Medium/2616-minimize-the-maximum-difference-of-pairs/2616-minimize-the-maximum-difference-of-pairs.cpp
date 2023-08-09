class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int start = 0;
        int end = nums[n-1] - nums[0];
        
        while(start < end){
            int mid = (start+end)/2;
            if(possible(mid, p, n, nums))
                end = mid;
            else
                start = mid + 1;
        }
        return start;
    }
private:
    bool possible(int a, int p, int n, vector<int>& nums){
        int cnt = 0;
        int idx = 0;
        while(idx < n-1 && cnt < p){
            if(nums[idx+1] - nums[idx] <= a){
                cnt += 1;
                idx += 2;
            }
            else
                idx += 1;
        }
        return cnt >= p;
    }
};