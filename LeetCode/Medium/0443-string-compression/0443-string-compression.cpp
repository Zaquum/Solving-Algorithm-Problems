class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int idx = 0;
        int i = 0;
        while (i < n){
            char cur = chars[i];
            int cnt = 1;
            while (i+1 < n && chars[i] == chars[i+1]){
                cnt++;
                i++;
            }
            chars[idx] = cur;
            idx++;
            if (cnt > 1) {
                int len = 0;
                for (int tmp = cnt; tmp > 0; tmp /= 10) {
                    len++;
                }
                
                int new_idx = idx + len - 1;
                for (int tmp = cnt; tmp > 0; tmp /= 10) {
                    chars[new_idx] = '0' + tmp % 10;
                    new_idx--;
                }
                
                idx += len;
            }
            // if string method is available
            // if (cnt > 1) {
            //     string cntStr = to_string(cnt);
            //     for (char c : cntStr) {
            //         chars[idx] = c;
            //         idx++;
            //     }
            // }

            i++;
        }
        return idx;
    }
};