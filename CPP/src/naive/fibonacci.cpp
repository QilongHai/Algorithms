#include <iostream>
using namespace std;


int fib_1(int n)
{
    if (n <= 2)
        return 1;
    return fib_1(n-1) + fib_1(n-2);
}


int fib_2(int n)
{
    int f[1000];
    int i = 0;
    f[0] = 0;
    f[1] = 1;

    for (i=2; i<=n; i++)
    {
        f[i] = f[i-1] + f[i-2];
        // cout << f[i];
    }

    return f[n];    
}


int fib_3(int n)
{
    int a = 0;
    int b = 1;
    int tmp;
    int i;

    if (n == 0)
        return 0;
    for (i=2; i<=n; i++)
    {
        tmp = a + b;
        a = b;
        b = tmp;
    }

    return b;

}


int main()
{
    int n = 30;
    cout << "fib_1: " << n << " is " << fib_1(n) << endl;

    int m = 30;
    cout << "fib_2: " << m << " is " << fib_2(m) << endl;

    int p = 30;
    cout << "fib_3: " << p << " is " << fib_3(p) << endl;

    return 0;
}
