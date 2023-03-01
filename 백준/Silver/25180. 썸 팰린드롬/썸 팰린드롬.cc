#include <iostream>

using namespace std;

int N;

int main() {
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	cin >> N;

    // 989 -> N = 26
    // 999 -> N = 27
    // 9559 -> N = 28
    // 95159 -> N = 29
    // 9669 -> N = 30

	int ans = (N - 1) / 9 + 1;
	if (ans % 2 == 0 && N % 2 == 1) { // ans이 짝수인데 N이 홀수이면 자리수 하나 추가
		ans += 1;
	}
	cout << ans;

	return 0;
}