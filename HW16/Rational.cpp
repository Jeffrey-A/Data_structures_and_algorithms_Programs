//Jeffrey Almanzar
#include <iostream>
using namespace std;
#include "Rational.h"

bool Rational::set(const int n, const int d)
{
	if (d != 0) {
		num_ = n;
		den_ = d;
		if (num_%den_ == 0) {
			num_ = n / d;
			den_ = 1;
		}
		else if (num_ % 2 == 0 && den_ % 2 == 0) {
			while (num_ % 2 == 0 && den_ % 2 == 0) {
				num_ = num_ / 2;
				den_ = den_ / 2;
			}
		}
		else if (den_%num_ == 0) {
			den_ = den_ / num_;
			num_ = num_ / num_;
			
		}
		return true;
	}
	else
		return false;
}
//Adding
Rational operator+(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.den() + r2.num() * r1.den();
	den = r1.den() * r2.den();
	return Rational(num, den);
}
//Subtracting
Rational operator-(const Rational &r1, const Rational &r2)
{
	int num, den;

	num = r1.num() * r2.den() - r2.num() * r1.den();
	den = r1.den() * r2.den();
	return Rational(num, den);
}
//Multiplying
Rational operator*(const Rational &r1, const Rational &r2)
{
	int num, den;
	num = r1.num() * r2.num();
	den = r1.den() * r2.den();
	return  Rational(num, den);
}
//Dividing
Rational operator/(const Rational &r1, const Rational &r2)
{
	int num, den;
	num = r1.num() *  r2.den();
	den = r1.den() *  r2.num();
	return  Rational(num, den);
}
//less than
bool operator<(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 < fraction2;
}
//less or equal
bool operator<=(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 <= fraction2;
}
//greater than
bool operator>(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 > fraction2;
}
//greater or equal
bool operator>=(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 >= fraction2;
}
//equal to
bool operator==(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 == fraction2;
}
//not equal to
bool operator!=(const Rational &r1, const Rational &r2)
{
	int num1, den1, num2, den2;
	double fraction1, fraction2;

	num1 = r1.num();
	den1 = r1.den();

	num2 = r2.num();
	den2 = r2.den();

	fraction1 = num1 / double(den1);
	fraction2 = num2 / double(den2);

	return fraction1 != fraction2;
}
//input
std::istream& operator>>(std::istream &is, Rational &r)
{
	char c;

	is >> r.num_ >> c >> r.den_;
	return is;
}
//ouput
std::ostream& operator<<(std::ostream &os, const Rational &r)
{
	os << r.num() << "/" << r.den();
	return os;
}


//Testing
int main()
{
	Rational r1 = Rational(2, 4), r2 = Rational(3, 6), r3 = Rational(1, 3), r4 = Rational(3, 10), r5 = Rational(7, 2), r6 = Rational(20, 6);
	cout << "                     ************************" << endl;
	cout << "                     *       Rational       *" << endl;
	cout << "                     ************************" << endl;
	
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                             Creating" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "Created fraction 2/4, got: " << r1 << ".       Should have received 1/2." << endl;
	cout << "Created fraction 3/6, got: " << r2 << ".       Should have received 1/2." << endl;
	cout << "Created fraction 1/3, got: " << r3 << endl;
	cout << "Created fraction 3/10, got: " << r4 << endl;
	cout << "Created fraction 7/2, got: " << r5 << endl;
	cout << "Created fraction 20/6, got: " << r6 << ".     Should have received 10/3." << endl;

	// Adding
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                              Adding" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << r1 << "+" << r2 << "= " << r1 + r2 << ".        Should get 1/1 or 1." << endl;
	cout << r1 << "+" << r3 << "= " << r1 + r3 << ".        Should get 5/6." << endl;
	cout << r1 << "+" << r4 << "= " << r1 + r4 << ".        Should get 4/5." << endl << endl;

	// subtracting
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                             Subtracting" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << r1 << "-" << r2 << "= " << r1 - r2 << ".       Should get 0/1 or 0." << endl;
	cout << r1 << "-" << r3 << "= " << r1 - r3 << ".       Should get 1/6." << endl;
	cout << r1 << "-" << r4 << "= " << r1 - r4 << ".       Should get 1/5." << endl << endl;

	// multiplying
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                             Multiplying" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << r1 << "*" << r2 << "= " << r1 * r2 << ".       Should get 1/4." << endl;
	cout << r1 << "*" << r5 << "= " << r1 * r5 << ".       Should get 7/4." << endl;
	cout << r4 << "*" << r6 << "= " << r4 * r6 << ".       Should get 1/1 or 1." << endl << endl;

	// dividing
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                            Dividing" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << r1 << " / " << r2 << "= " << r1 / r2 << ".       Should get 1/1 or 1." << endl;
	cout << r1 << " / " << r5 << "= " << r1 / r5 << ".       Should get 1/7." << endl;
	cout << r2 << " / " << r6 << "= " << r2 / r6 << ".       Should get 3/20." << endl << endl;

	// comparing
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "                            Comparing" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << r1 << " < " << r2 << " is: " << (r1 < r2) << ".       Should be 0 or False." << endl;
	cout << r1 << " <= " << r2 << " is: " << (r1 <= r2) << ".     Should be 1 or True." << endl;
	cout << r1 << " < " << r3 << " is: " << (r1 < r3) << ".       Should be 0 of False." << endl;
	cout << r1 << " > " << r4 << " is: " << (r1 > r4) << ".       Should be 1 or True." << endl << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	cout << "              Input and Output were made by you in class:" << endl;
	cout << "--------------------------------------------------------------------------" << endl;
	Rational r7;
	cout << "Now, enter a fraction, for example 3/4:";
	cin >> r7;
	cout << "You entered: " << r7 << endl;
	return 0;
}

