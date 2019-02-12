// test_searches.cpp
//Jeffrey Almanzar
//Exercises 8,9
#include "searches.h"
#include <iostream>
using namespace std;

// 8
int linear_search(const int *a, int size, int m) {
	int i;
	int pos = -1;
	for (i = 0; i < size; i++) {
		if (a[i] == m) {
			pos = i;
			break;  //item already found!!
		}
	}
	return pos;
}

// 9
int binary_search(const int *a, int size, int m) {
	int low = 0, high = size - 1;

	while (low <= high) {
		int mid = (low + high) / 2;
		int item = a[mid];

		if (m == item) {
			return mid;
		}
		else if (m < item) {
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}
	return -1;
}

int main(){
	int a[7]={1,5,8,12,17,23,39};
	
	int k,n;
	
	cout << "We are given the array of: ";
	for (int i=0; i< 7 ; i++){
		cout << a[i] << "  ";}
	cout << endl;
	
	k = linear_search(a,7,12);
	n = binary_search(a,7,12);
	
	cout << "The index of 12 in the array is :" <<"\n\t" << k << " according to the linear search.";
	cout << "\n\t" << n << " according to the binary search." << endl;
}
