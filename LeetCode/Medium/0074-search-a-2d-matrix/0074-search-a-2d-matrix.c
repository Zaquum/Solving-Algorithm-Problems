bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int start = 0;
    int col = *matrixColSize;
    int end = matrixSize * col - 1;

    while(start <= end){
        int mid = (start + end) / 2;
        int value = matrix[mid/col][mid%col];
        if(value == target)
            return true;
        else if(value < target)
            start = mid + 1;
        else
            end = mid - 1;
    }
    return false;
}