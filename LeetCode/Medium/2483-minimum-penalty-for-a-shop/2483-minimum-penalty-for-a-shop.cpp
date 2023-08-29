class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size(), max_score = 0, score = 0, idx = -1;
        for(int i=0; i<n; i++){
            if(customers[i]=='Y')
                score += 1;
            else
                score -= 1;
            if(score > max_score){
                idx = i;
                max_score = score;
            }
        }
        return idx + 1;
    }
};