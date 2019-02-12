////Jeffrey Almanzar
////Exercise 3
//#include<iostream>
//using namespace std;
//
//int main() {
//	int user_input=0,save_input[50],size=0;
//	
//	do {
//		cout << "Enter non-negative integers (-1) to quit: ";
//		cin >> user_input;
//		save_input[size] = user_input;
//		size++;
//	} while (user_input >= 0);
//	size--;
//	cout << endl;
//	
//	int i;
//	double total = 0.0,avr=0.0;
//	for (i = 0; i < size; i++) { //add all the values entered
//		total= total+ save_input[i];
//	}
//	avr = total / size;
//
//	cout << "========================================" << endl;
//	cout << "You entered " << size << " numbers:"<<endl;
//	cout << "  Their sum is " << total << endl << "  The average is " << avr << endl;
//	cout << "========================================" << endl;
//	
//}