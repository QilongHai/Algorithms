#include <iostream>
using namespace std;

void bubble_sort(int A[], int n)
{
    for (bool sorted = false; sorted = !sorted; n--)
        for (int i = 1; i < n; i++)
            if (A[i-1] > A[i])
            {
                int tmp = A[i-1];
                A[i-1] = A[i];
                A[i] = tmp;
                sorted = false;
            }
}