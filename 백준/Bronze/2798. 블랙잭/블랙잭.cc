#include <iostream>
#include <cstdio>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>

#define Max_N 100;

using namespace std;


int main(void)
{
	int N, M;
	cin >> N >> M;

	int a[100];
	int temp_MAX = 0;
	for (int i = 0; i < N; i++)
		cin >> a[i];
	for (int i = 0; i < N; i++)
	{
		for (int j = i+1; j < N; j++)
		{
			for (int k = j+1; k < N; k++)
			{
				if((a[i]+a[j]+a[k]<=M) && (a[i] + a[j] + a[k] >= temp_MAX))
					temp_MAX = a[i]+a[j]+a[k];			
			}
		}
	}
	cout << temp_MAX;


	return 0;

}