#include <iostream>
#include "LList.h"

using namespace std;

int main()
{
	LList a; // linked list
	int s; // size of the linked list
	int i; 
	
	cout << "Checking the append operation: " << endl;
	a.append(5);
	
	cout << a[0] << endl;
	
	a.append(7);
	a.append(12);
	a.append(6);
		
	cout << a[1] << endl;
	cout << a[2] << endl;
	cout << a[3] << endl; 
	
	cout << "Done with append check." << endl;
	
	cout << "Checking he insertion operation: " << endl;
	
	a.insert(2,6);
	a.insert(4,18);
	
	s = a.size();
	
	cout << "Right now there are " << s << " elements in the array:" << endl;
	
	for(i=0; i<s ; i++)
	{
		cout << a[i] << "   ";
	}
	
	cout << endl;
	cout << "Insertion operation check is over." << endl;
	
	cout << "Checking the deletion operation: " << endl;
	cout << "Popping " << a.pop(2) << endl;
	cout << "Popping " << a.pop(0) << endl;
	
	s = a.size();
	cout << "We are left with " << s << " elements: " << endl;
	
		for(i=0; i<s ; i++)
	{
		cout << a[i] << "   ";
	}
	cout << endl;
	
	cout << "Deletion operation check is over." << endl;
}
