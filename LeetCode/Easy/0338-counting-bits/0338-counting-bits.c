/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize){
    *returnSize = n+1;
    int* ans = (int*)malloc(sizeof(int) * (*returnSize));

    for(int i=0; i<=n; i++){
        ans[i] = binary(i);
    }
    return ans;
}

int binary(int n){
    int remain;
    int result = 0;
    while(n>0){
        remain = n%2;
        n = n/2;
        result += remain;
    }
    return result;
}