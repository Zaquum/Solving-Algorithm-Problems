class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int gcd_len = gcd(str1.size(), str2.size());
        if (gcd_len == 0)
            return "";

        string gcd_str = str2.substr(0, gcd_len);
        int i=0, j=0;
        while (i<str1.size()){
            if(str1[i] != gcd_str[j])
                return "";
            i++;
            j++;
            j%=gcd_len;
        }

        gcd_str = str1.substr(0, gcd_len);
        i=0, j=0;
        while (i<str2.size()){
            if(str2[i] != gcd_str[j])
                return "";
            i++;
            j++;
            j%=gcd_len;
        }
        return gcd_str;
    }
    int gcd(int a, int b){
        while(b){
            int tmp = b;
            b = a%b;
            a = tmp;
        }
        return a;
    }
};