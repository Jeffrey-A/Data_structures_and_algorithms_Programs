////Jeffrey Almanzar
////Exercise 4. I am using the quadratic formula.
//#include <iostream>
//#include <math.h>
//using namespace std;
//
//int main() {
//	int a=1, b=1, c=1;
//
//	cout << "Please enter the coefficients a, b, and c of a quadratic equation ";
//	cout << "separated be spaces in between: ";
//	cin >> a>> b>> c;
//	cout << endl;
//
//	double x1=0, x2=0;
//	int inside_sqrt = b*b - (4 * a*c);
//
//	b = -b;
//	int bottom = 2 * a;
//	double topSum=0,topSus=0;
//	
//	if (inside_sqrt < 0) {//negative number inside a radical
//		cout << "Sorry, no real solution!" << endl;
//	}
//	else if(inside_sqrt==0){// only one real solution
//		topSum = b + sqrt(inside_sqrt);
//		x1 = topSum / double(bottom);
//		cout << "Only one real solution: " << "X =" << x1 << endl;
//	}
//	else {//Two real solutions
//		topSum = b + sqrt(inside_sqrt);
//		topSus = b - sqrt(inside_sqrt);
//		x1 = topSum / double(bottom);
//		x2 = topSus / double(bottom);
//		cout << "Two real solutions: " << endl << "\tX1 =" << x1 << endl << "\tX2 =" << x2 << endl;
//	}
//
//}