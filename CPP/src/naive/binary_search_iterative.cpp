#include <iostream>
using namespace std;

int binarySearch(int A[], int low, int high, int key){
    while (low <= high){
        int mid = low + (high - low) / 2;

        if (A[mid] == key){
            return mid;
        }

        if (A[mid] < key){
            low = mid + 1;
        }else{
            high = mid - 1;
        }
    }
    return -1;
}

int main(){
    int A[] = {2, 3, 4, 10, 11, 15, 19, 22, 27, 30};
    int key = 10;
    int low = 0;
    int high = sizeof(A) / sizeof(A[0]) - 1;

    int result = binarySearch(A, low, high, key);
    (result == -1) ? cout << "Element is not present in array" 
                   : cout << "Element is present at index " << result; 
    return 0;

}