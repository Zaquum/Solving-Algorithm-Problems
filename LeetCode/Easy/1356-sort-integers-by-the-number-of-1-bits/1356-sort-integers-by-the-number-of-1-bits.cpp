class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), customComparator);
        return arr;
    }

    static int countBits(int n) {
        int count = 0;
        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }

    static bool customComparator(int &a, int &b) {
        int countA = countBits(a);
        int countB = countBits(b);

        if (countA == countB)
            return a < b;

        return countA < countB;
    }
};