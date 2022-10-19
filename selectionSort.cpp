// Selection sort in C++

#include<iostream>
using namespace std;

// function to swap two elements
void swap(int *x, int *y) {
  int temp = *x;
  *x = *y;
  *y = temp;
}

// function to print array
void printArr(int arr[], int n) {
  for(int i=0; i<n; i++) {
    cout<<arr[i]<<" ";
  }
  cout<<endl;
}

// function for Selection Sort
int *insertionSort(int arr[], int n) {
  for(int i=0; i<n; i++) {
    for(int j=i+1; j<n-1; j++) {
      if(arr[i] > arr[j]) {
        swap(arr[i], arr[j]);
      }
    }
  }
  return arr;
}

int main() {
  int unsortedArr[7] = {3, 7, 2, 8, 1, 0, 9};
  int size = sizeof(unsortedArr)/sizeof(unsortedArr[0]);

  cout<<"Unsorted Array : ";
  printArr(unsortedArr, size);

  int *sortedArr = insertionSort(unsortedArr, size);
  cout<<"Sorted Array : ";
  printArr(sortedArr, size);

  return 0;
}