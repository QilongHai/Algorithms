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

int main()
{
    int A[] = {2, 1, 13, 4, 22, 15, 9};
    int n = sizeof(A) / sizeof(A[0]);
    bubble_sort(A, n);
    for (int i=0; i<n; i++)
        cout << A[i] << endl;
}