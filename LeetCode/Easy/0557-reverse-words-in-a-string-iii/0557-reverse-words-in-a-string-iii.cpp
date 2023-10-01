#include <sstream>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        istringstream iss(s);
        string word, result;

        while (iss >> word) {
            reverse(word.begin(), word.end());
            if (!result.empty())
                result += " ";
            result += word;
        }

        return result;
    }
};