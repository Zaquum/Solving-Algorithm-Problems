int candy(int* ratings, int ratingsSize){
    int* result = (int*)malloc(ratingsSize * sizeof(int));

    result[0] = 1;

    for(int i=1; i<ratingsSize; i++){
        if(ratings[i] > ratings[i-1]){
            result[i] = result[i-1] + 1;
        }
        else
            result[i] = 1;
    }

    for(int i=ratingsSize-2; i>=0; i--){
        if(ratings[i] > ratings[i+1] && result[i] <= result[i+1])
            result[i] = result[i+1] + 1;
    }
    int ans = 0;
    for(int i=0; i<ratingsSize; i++)
        ans += result[i];

    free(result);
    return ans;
}