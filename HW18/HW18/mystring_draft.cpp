//Jeffrey Almanzar
// mystring.cpp
#include <iostream>
#include <cassert>
#include "mystring.h"

mystring::mystring(unsigned int capacity){
	size_ = 0; // empty string
	capacity_ = capacity;
	string_ = new char[capacity];
}

mystring::~mystring(){
	
	// put the code here
	delete[] string_;
}

mystring&  mystring::operator+=(char c){
	// put the code here for adding one character to the string
	if (size_ == capacity_) {
		resize(2 * capacity_);
	}
	string_[size_++] = c;
	return *this;
}

void mystring::resize(unsigned int newcapacity){
	
	char *tmp;
	
	// tmp will be used for the "new" placeholder of array
	// put the code here for resizing the string to be of new capacity 'newcapacity'
	// don't forget to copy over elements from the "old" place to the "new" one
	capacity_ = newcapacity;
	tmp = new char[capacity_];
	size_t i;
	for (i = 0; i < size_; ++i) {
		tmp[i] = string_[i];
	}
	delete [] string_; // deallocate the space by "old" array
	string_ = tmp; // re-direct the pointer to the "new" array
}

std::ostream& operator<<(std::ostream &os, const mystring &st){
	
	// put the code here for outputting characters, one by one, from the string_ array to the 'os'

	size_t i;
	for (i = 0; i < st.size_; ++i) {
		os<< st.string_[i];
	}
	os << std::endl;
	
	return os;
}

 
char& mystring::operator[](unsigned int position) {

	assert(position < size_);
	
	// put the rest of the code here
	return string_[position];
}

int mystring::find(char c) {
	// finds the first occurence of c in the string, returns its position, 
	// returns -1 if not found
	
	// put the code here
	size_t i;
	for (i = 0; i < size_; ++i) {
		if (string_[i] == c) {
			return i;
		}
	}return -1;
	
}

void mystring::reverse() {
	
	// put the code for string reversal here
	char *temp;
	temp = new char[capacity_];
	size_t pos, i;
	pos = size_ - 1;
	for (i = 0; i < size_; ++i) {
		temp[i] = string_[i];
	}

	for (i = 0; i < size_; ++i) {
		string_[i] = temp[pos];
		--pos;
	}
	delete[] temp; //deallocating memory
}



mystring::mystring(const mystring &str) {
	copy(str);
}

void mystring::copy(const mystring &str){

	// this procedure copies everything from string 'str' to "this" string
	// size_ has to be updated, capacity_ has to be updated
	// new space should be allocated for the array (use tmp)
	// at the end don't forget to do string_ = tmp;
	size_ = str.size_;
	capacity_ = str.capacity_;
	char *temp;
	temp = new char[capacity_];
	size_t i;
	for (i = 0; i < str.capacity_; ++i) {
		temp[i] = str.string_[i];
	}
	string_ = temp;
}

mystring& mystring::operator=(const mystring &str) {
	if (this != &str) {
		delete[] string_;
		copy(str);

		return *this;
	}
	
}

/* operator overloading */
/* comment : actually it is advised not to do operator overloading on the same number of parameters (1 parameter in our case),
especially when their types are "close". 
For example in this case, we defined operator+= on character and on mystring types, which are pretty close.
So in real world, we won't do it. Instead we will most likely define two operators:
addchar
addstring 
*/


mystring &mystring::operator+=(const mystring &str) {
   // this is concatentation of two strings operator for two strings, i.e. s1 += s2
   

   // put your code here
	
	if (size_ + str.size_ > capacity_) {
		resize(size_ + str.size_);
	}

	size_t j, pos=size_;
	for (j =0; j < str.size_; ++j) {
		string_[pos++] = str.string_[j];
	}
	size_ = size_ + str.size_;
	return *this;

}

std::istream& operator>> (std::istream &is, mystring &st) {
	unsigned int length;
	std::cout << "Please enter the size of the string: ";
	std::cin >> length;

	st.capacity_ = length;
	st.resize(length);
	
	int i = 0;
	char inputItem;

	std::cout << "Now enter characters one by one, pressing Enter after each:\n";

	inputItem=' ';

	while (i < length && inputItem != '\n') {
		is >> inputItem;
		st.string_[i] = inputItem;
		i++;
	}

	st.size_ = length;

	return is;

}




