int peakIndexInMountainArray(int* arr, int arrSize){
    int find_max(int start, int end){
        if(start < end){
            int mid = (start + end) / 2;
            if(arr[mid] < arr[mid+1])
                return find_max(mid + 1, end);
            else
                return find_max(start, mid);
        }
        return start;
    }
    return find_max(0, arrSize-1);
}