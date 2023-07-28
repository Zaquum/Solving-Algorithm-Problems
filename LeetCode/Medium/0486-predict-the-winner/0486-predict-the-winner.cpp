class Solution {
public:
    int solve(vector<int>& nums, int i, int j, bool turn){
        if(i>j)
            return 0;

        // turn == 1 : player 1
        if(turn){
            return max(nums[i] + solve(nums,i+1,j,false), nums[j]+solve(nums,i, j-1, false));
        }
        // else : player 2
        else
            return min(solve(nums,i+1,j,true) - nums[i], solve(nums,i,j-1,true)-nums[j]);
    }
    bool PredictTheWinner(vector<int>& nums) {
        int ans = solve(nums, 0, nums.size()-1, true);
        return ans >= 0;
    }
};