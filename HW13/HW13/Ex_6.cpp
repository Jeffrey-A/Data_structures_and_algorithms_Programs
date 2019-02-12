////Jeffrey Almanzar
////Exercise 6 updated
//#include<iostream>
//using namespace std;
//int main() {
//	int anual_investment = 0, num_of_years = 0;
//	double interest_rate = 0.0;
//
//	cout << "Enter the anual investment amout: ";
//	cin >> anual_investment;
//	cout << endl;
//	cout << "\tEnter the interest rate earned every year (5%) --> 5: ";
//	cin >> interest_rate;
//	cout << "\tPlease enter the number of years: ";
//	cin >> num_of_years;
//	cout << endl;
//	int i;
//	double final_amount = anual_investment + ((interest_rate*anual_investment) / 100); // calculates the first year
//	for (i = 1; i < num_of_years; i++) {// calculates the rest of the  years starting from the second one
//		final_amount = (final_amount + anual_investment) *(1 + (interest_rate / 100));
//	}
//	cout << "The final value of the investment in " << num_of_years << " years is: $" << final_amount << endl;
//}
