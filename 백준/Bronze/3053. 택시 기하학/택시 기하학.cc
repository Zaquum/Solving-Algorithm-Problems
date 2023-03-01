#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>


using namespace std;

double zegop(double a)
{
	return a*a;
}

int main(void)
{
	int r;

	cin >> r;

	double Not_uc = sqrt(2 * zegop(r));

	cout << fixed;
	cout.precision(6);

	
	cout << M_PI * zegop(r) << endl;
	cout << zegop(Not_uc) << endl;


	return 0;

}