//Jeffrey Almanzar  HW15
#include <iostream>
#include <fstream>
#include <string>
#include<vector> //like a dynamic array. It's part of the C++ Standard Template Library 
using namespace std;
//----------------------------------------------------------------------------------------------------
double find_min(vector <double> &a) {   // passing a vector by reference 
	//pre: a is a vector of size>0.
	//post: Finds the minimum element and returns it.
	double min = a[0];
	int i;
	for (i = 0; i < int(a.size()); i++) { //without converting a.size() to an int I get a warning from the compiler: warning C4018: '<': signed/unsigned mismatch
		if (a[i] < min) {
			min = a[i];
		}
	}
	return min;
}
//----------------------------------------------------------------------------------------------------
double find_max(vector<double> &a) {
	//pre: a is a vector of size>0.
	//post: Finds the maxmimum element and returns it.
	double max= a[0];
	int i;
	for (i = 0; i < int(a.size()); i++) {
		if (a[i] > max) {
			max = a[i];
		}
	}
	return max;
}
//----------------------------------------------------------------------------------------------------
double average(vector<double> &a) {
	//pre: a is a vector of size>0.
	//post: Finds the average of all values and returns it.
	int count = 0;
	double sum = 0.0;
	int i;
	for (i = 0; i < int(a.size()); i++) {
		count++;
		sum += a[i];
	}
	return sum / double(count);
}
//----------------------------------------------------------------------------------------------------
int num_of_zeros(vector<double> &a) {
	//pre: a is a vector of size>0.
	//post: Finds the numbers of zeros in a and returns it.
	int num = 0, i;
	for (i = 0; i<int(a.size()); i++) {
		if (a[i] == 0.0) {
			num++;
		}
	}
	return num;
}
//----------------------------------------------------------------------------------------------------
void get_pos(vector<double> &a, vector<double> &p) {
	//pre: a and p are vectors.Size of a is > 0.
	//post: Finds all the positives values in a and place them in p.
	int i;
	for (i = 0; i<int(a.size()); i++) {
		if (a[i] > 0) {
			p.push_back(a[i]);//similar to the python append method
		}
	}
}
//----------------------------------------------------------------------------------------------------
void get_neg(vector<double> &a, vector<double> &n) {
	//pre: a and n are vectors.Size of a is > 0.
	//post: Finds all the negatives values in a and place them in n. 
	int i;
	for (i = 0; i<int(a.size()); i++) {
		if (a[i] < 0) {
			n.push_back(a[i]);//similar to the python append method
		}
	}
}
//----------------------------------------------------------------------------------------------------
double pos_neg_ave(int num, vector<double> items) {
	//pre: num is the size of the vector items.
	//post: returns the average value of items. 
	double sum = 0;
	if (num>0) { //if it's not empty
		int i;
		for (i = 0; i<num; i++) {
			sum += items[i];
		}
		return sum / double(num);
	}
	else {
		return sum;
	}
}
//----------------------------------------------------------------------------------------------------
void display_array(vector<double> &a, string name) {
	//pre: a is a vector with size>0 and name is a string.
	//post: display to the console the vector a.
	cout << "               ******" << name << "******" << endl;
	cout << "----------------------------------------------------------------------------" << endl;
	for (int i = 0; i<int(a.size()); i++) {
		cout << a[i] << " | ";
	}
	cout << endl;
	cout << "----------------------------------------------------------------------------"<<endl;
}
//----------------------------------------------------------------------------------------------------
int find_minimum_index(vector<double>&a) {
	//pre: a is a vector of size>0.
	//post: finds and returns the index of the minimum element in a.
	double min = a[0];
	int min_pos=0;
	int i;
	for (i = 0; i < int(a.size()); i++) { 
		if (a[i] < min) {
			min = a[i];
			min_pos = i;
		}
	}
	return min_pos;
}
//----------------------------------------------------------------------------------------------------
void sort(vector<double> unsorted, vector<double>&sorted) {
	//pre: sorted and unsorted are vectors of size >0.
	//post: place the elements of unsorted in increasing order in sorted.
	double min;
	int mini_pos=0;
	while (int(unsorted.size())>0) {
		min = find_min(unsorted); //find the minimun element
		mini_pos = find_minimum_index(unsorted);//find the position of the minimun element
		sorted.push_back(min); //place the minimun value in sorted
		unsorted.erase(unsorted.begin() + mini_pos); //erase the minimum value from the unsorted vector
	}
}
//----------------------------------------------------------------------------------------------------
int main() {
	string filename;
	ifstream info_file; //input file
	ofstream sorted_file; // output file
	vector<double> numbers; // saves the numbers found in the file
	vector<double> numbers_sorted; //will contain the values of the vector numbers  in increasing order.

	// Getting the file name from the user
	//----------------------------------------------------------------------------------------------------
	cout << "Enter file name (sample.txt): ";
	cin >> filename;
	info_file.open(filename);
	//----------------------------------------------------------------------------------------------------
	if (info_file.is_open()) {   // file open succesfully
		cout << "File succesfuly opened!!" << endl;

		double temp;
		while(!info_file.eof()){// while not at the end of the file
			info_file >> temp;
			numbers.push_back(temp);   //place the item in my vector data structure 
		}
		cout << endl;
		info_file.close();

        //----------------------------------------------------------------------------------------------------
		vector<double>positives; //will keep all the postive values
		vector<double>negatives; //will keep all the negative values
		double mini = find_min(numbers);  //minimum
		double maxi = find_max(numbers);  //maximum 
		double ave = average(numbers);    //average of all the values
		int zeros = num_of_zeros(numbers); // number of zeros
		get_pos(numbers, positives);  // gets all positives values
		get_neg(numbers, negatives);  // gets all negatives values
		int pos = int(positives.size()); //number of positives values
		int neg = int(negatives.size()); //number of negatives values
		double average_pos = pos_neg_ave(pos, positives); //average of all positives values
		double average_neg = pos_neg_ave(neg, negatives); //average of all negatives values
		cout << "----------------------------------------------------------------------------" << endl;
		display_array(numbers, "Values in file"); //display all the values found in the fille
		cout << "               Min: " << mini<<"  "<<"Max: "<<maxi<<"  "<<"Average: "<<ave<< endl;
		cout << endl;
		cout << endl;
		cout << "----------------------------------------------------------------------------" << endl;
		display_array(positives, "Positives Values"); //display all the positive values found in the file
		cout << "               Quantity: " << positives.size() << "  Average: " << average_pos << endl;
		cout << endl;
		cout << endl;
		cout << "----------------------------------------------------------------------------" << endl;
		display_array(negatives, "Negatives Values"); //display all the negative values found in the file
		cout << "               Quantity: " << negatives.size() << "  Average: " << average_neg << endl;
		cout << endl;
		cout << endl;
		cout << "----------------------------------------------------------------------------" << endl;
		cout << "               ******" <<"Number of Zeros"<< "******" << endl;
		cout << "----------------------------------------------------------------------------" << endl;
		cout << "Quatity: " << zeros << endl;
		cout << "----------------------------------------------------------------------------" << endl;

		//----------------------------------------------------------------------------------------------------
		sort(numbers, numbers_sorted); //sorting the values.
		sorted_file.open("outsample.txt"); //output file.
		//writing in outsample.txt
		sorted_file << "               ******" << "Sorted Array"<< "******" << endl;
		sorted_file << "----------------------------------------------------------------------------" << endl;
		for (int i = 0; i<int(numbers_sorted.size()); i++) {
			sorted_file << numbers_sorted[i] << " | ";
		}
		sorted_file << endl;
		sorted_file << "----------------------------------------------------------------------------" << endl;
		sorted_file << "              by Jeffrey Almanzar                  " << endl;
		sorted_file.close();
		//----------------------------------------------------------------------------------------------------
		
		cout << endl;
		cout << endl;
		cout << "----------------------------------------------------------------------------" << endl;
		cout << "The collection of numbers was sorted and storaged in the file: outsample.txt " << endl;;
		cout << "----------------------------------------------------------------------------" << endl;
		cout << endl;
	}
	else {
		cout << "Could not open the file."<<endl <<"Please check file directory." << endl;
	}
	return 0;
}