#include <iostream>
using namespace std;

int fib_1(int n)
{
    if (n < 2)
    {
        return 1;
    }else{
        return fib_1(n-1) + fib_1(n-2);
    }
}

int main()
{
    int n = 20;
    cout << "fibonacci " << n << " is " << fib_1(n) << endl;
    return 0;
}
