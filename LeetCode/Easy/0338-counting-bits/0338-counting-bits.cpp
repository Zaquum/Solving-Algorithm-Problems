class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        for(int i=0; i<=n; i++){
            ans.push_back(binary(i));
        }
        return ans;
    }

    int binary(int n){
        int result = 0;
        int remain;
        while(n>0){
            remain = n % 2;
            n = int(n/2); // quotient
            result += remain;
        }
        return result;
    }
};