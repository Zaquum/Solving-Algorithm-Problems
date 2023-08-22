#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

std::unordered_map<int, int> memo;

int dp(int n) {
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }
    if (n < 0) {
        return 2000;
    }

    memo[n] = std::min(dp(n - 3), dp(n - 5)) + 1;
    return memo[n];
}

int main() {
    int n;
    cin >> n;
    memo[0] = 0;
    int result = dp(n);
    if(result < 2000)
        std::cout << result << std::endl;
    else
        cout << "-1" << endl;
    return 0;
}
