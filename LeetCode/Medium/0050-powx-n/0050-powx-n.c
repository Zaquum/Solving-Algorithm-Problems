double solve(double x, long long n){
    if(n==0)
        return 1;
    else if(n%2==0)
        return solve(x * x, n/2);
    else
        return x * solve(x * x, (n-1)/2);
}

double myPow(double x, long long n){
    if(n>=0)
        return solve(x,n);
    else
        return 1/solve(x,-n);
}
