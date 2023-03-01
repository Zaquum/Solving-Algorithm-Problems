#include <iostream>
#include <cstdio>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>
#include <string>

const int Max = 51;

using namespace std;


int N, M;
string a[Max];
string whitechess[8] = { {"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"}
};
string blackchess[8] = { {"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
{"BWBWBWBW"},
{"WBWBWBWB"},
};


int com_white(int x, int y)
{
	int cnt = 0;

	for (int i = x; i < x + 8; i++)
	{
		for (int j = y; j < y + 8; j++)
		{
			if (whitechess[i - x][j - y] != a[i][j])
				cnt++;
		}
	}
	return cnt;
}

int com_black(int x, int y)
{
	int cnt = 0;

	for (int i = x; i < x + 8; i++)
	{
		for (int j = y; j < y + 8; j++)
		{
			if (blackchess[i - x][j - y] != a[i][j])
				cnt++;
		}
	}
	return cnt;
}


int min(int a, int b)
{
	return a > b ? b : a;
}


int calcolor()
{
	int mincounts = 987654321;
	for (int x = 0; x <= N - 8; x++) {
		for (int y = 0; y <= M - 8; y++) {
			mincounts = min(mincounts, min(com_white(x, y), com_black(x, y)));

		}
	}

	return mincounts;

}

int main(void)
{
	
	string str;
	cin >> N >> M;


	for (int i = 0; i < N ; i++)
		cin>>a[i];
		
	cout << calcolor();

	return 0;

}