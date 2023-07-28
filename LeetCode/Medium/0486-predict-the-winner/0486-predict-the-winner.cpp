class Solution{
    public:
        int solve(vector<vector<int>>&dp, vector<int>& nums, int i, int j, bool turn){
            if(i>j)
                return 0;
            if(dp[i][j]!=-1e5)
                return dp[i][j];
            int ans = 0;
            if(turn){
                ans = max(nums[i]+solve(dp, nums, i+1, j, false), nums[j]+solve(dp, nums, i, j-1, false));
            }
            else
                ans = min(-nums[i]+solve(dp, nums, i+1, j, true), -nums[j]+solve(dp,nums,i,j-1,true));
            return dp[i][j]=ans;
        }
        bool PredictTheWinner(vector<int>& nums){
            int n = nums.size();
            vector<vector<int>>dp(n, vector<int>(n,-1e5));
            return solve(dp,nums,0,n-1,true) >= 0;
        }
};

// O(2^n)
// class Solution {
// public:
//     int solve(vector<int>& nums, int i, int j, bool turn){
//         if(i>j)
//             return 0;

//         // turn == 1 : player 1
//         if(turn){
//             return max(nums[i] + solve(nums,i+1,j,false), nums[j]+solve(nums,i, j-1, false));
//         }
//         // else : player 2
//         else
//             return min(solve(nums,i+1,j,true) - nums[i], solve(nums,i,j-1,true)-nums[j]);
//     }
//     bool PredictTheWinner(vector<int>& nums) {
//         int ans = solve(nums, 0, nums.size()-1, true);
//         return ans >= 0;
//     }
// };