class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> freq;
        for(auto c:s){
            freq[c]++;
        }
        priority_queue<pair<int, char>> max_heap;
        for(auto elem: freq){
            max_heap.push({elem.second, elem.first});
        }

        if(max_heap.top().first > (s.size()+1)/2)
            return "";
        
        string result;
        int prev_cnt=0;
        char prev_char=' ';
        while(!max_heap.empty()){
            auto cnt_char = max_heap.top();
            max_heap.pop();
            result.push_back(cnt_char.second);
            
            if(prev_cnt > 0)
                max_heap.push({prev_cnt, prev_char});
            prev_cnt = cnt_char.first - 1;
            prev_char = cnt_char.second;
        }
        return result;
    }
};