#include <iostream>
#include <cstdio>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>
#include <string>

using namespace std;
#define Max 1000000

int sorted[Max];
int list[Max];

/*숫자들이 정렬되는 과정*/
void merge(int left, int mid, int right)
{
	int i, j, k, l;
	i = left;
	j = mid + 1;
	k = left;
	//int length = right - left + 1;
	//int *sorted = new int[length];

	/*분할 정렬된 list 합볍*/
	while (i <= mid && j <= right)
	{
		if (list[i] <= list[j])
			sorted[k++] = list[i++];
		//k++;
		//i++;
		else
			sorted[k++] = list[j++];
		//k++;
		//j++;
	}
	if (i > mid) {
		for (l = j; l <= right; l++)
			sorted[k++] = list[l];
	}
	else{
		for (l = i; l <= mid; l++)
			sorted[k++] = list[l];
	}

	for (l = left; l <= right; l++) {
		list[l] = sorted[l];
	}
	//delete[] sorted;	
}



//합병 정렬
void merge_sort(int left, int right) {

	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);

	}
}


int main(void)
{
	int i;
	int n;

	cin >> n;

	//int *list = new int[n];

	for (i = 0; i < n; i++)
		//cin >> list[i];
		scanf("%d", &list[i]);
	
	merge_sort(0, n - 1);

	for (i = 0; i < n; i++)
		//cout << list[i];
		printf("%d\n", list[i]);

	//delete[] list;
	return 0;
}