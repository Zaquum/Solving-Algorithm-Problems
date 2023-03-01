#include <iostream>

int main()
{
    using namespace std;
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int Num, NewNum;
    int Num_10, Num_1, Num_Right;
    int Count = 0;
    
    cin >> Num;
    NewNum = Num;
    do{
        Num_10 = NewNum/10;
        Num_1 = NewNum%10;
        Num_Right = Num_10+Num_1;
        NewNum = Num_1*10 + Num_Right%10;
        Count++;
    }while(!(Num==NewNum));
    
    cout << Count << endl;
    
    return 0;
}