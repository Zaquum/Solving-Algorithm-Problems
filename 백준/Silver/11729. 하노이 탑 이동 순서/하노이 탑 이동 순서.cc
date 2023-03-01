#include <iostream>
#include <cstdio>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>


using namespace std;

int hanoi_cnt(int a)
{
	if (a == 1)
		return 1;
	else
		return 2*hanoi_cnt(a - 1)+1;
}

void move_hanoi(int n, int from, int by, int to)
{
	if (n == 1)
		printf("%d %d\n", from, to);
	else
	{
		move_hanoi(n - 1, from, to, by);
		printf("%d %d\n", from, to);
		move_hanoi(n - 1, by, from, to);	
	}

}


int main(void)
{
	int line;
	scanf("%d", &line);

	hanoi_cnt(line);
	printf("%d\n", hanoi_cnt(line));
	move_hanoi(line, 1, 2, 3);


	return 0;

}