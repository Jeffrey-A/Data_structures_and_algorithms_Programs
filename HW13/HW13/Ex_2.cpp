////Jeffrey Almanzar
////Exercise 2
//#include<iostream>
//#include<string>
//using namespace std;
//
//int main() {
//	int user_input;
//	int coins[5] = { 25,10,5,1 };//coins
//
//	cout << "Enter the number of cents(<100): ";
//	cin >> user_input;
//
//	int i,q=0, d=0, n=0, p=0,size=0;
//	int change[15];
//
//	for (i = 0; i < 4; ++i) {
//		while (user_input >= coins[i]) {
//			change[size] = coins[i]; //add one of this coin to the change
//			++size;
//			user_input = user_input - coins[i];
//		}
//	}
//	
//	for (i = 0; i < size; ++i) {
//		if (change[i] == 25) {
//			q++;
//		}
//		else if (change[i] == 10) {
//			d++;
//		}
//		else if (change[i] == 5) {
//			n++;
//		}
//		else if (change[i] == 1) {
//			p++;
//		}
//	}
//
//	cout << "===============================" << endl;
//	cout << "\t" << q << " quarters " << endl << "\t" << d << " dimes " << endl << "\t" << n << " nickels "<<endl << "\t" << p << " pennies" << endl;
//	cout << "===============================" << endl;
//
//}

