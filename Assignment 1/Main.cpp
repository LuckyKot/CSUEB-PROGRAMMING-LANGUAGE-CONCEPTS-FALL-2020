/*  
CS 311
--
Simple Lexical Scanner
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>

using namespace std;

int main() {
	ifstream inFile;
	ofstream outFile;
	string entry;
	string line;
	string word;
	int keyword = 0;
	int number = 0;
	int sign = 0;
	int character = 0;
	int space = 0;
	int funct = 0;
	char chars[] = ".,:'\"";

	const char *keywords[15] = { "#include", "using", "namespace","int","char","cout","return","std","double","if","else","while","for","break", "<<" };
	const char *numbers[7] = { "1", "2", "3", "4", "5", "24","32"};
	//only seven just for example
	const char *signs[3] = { "+","-","=" };
	const char *characters[3] = {"a","b","c"};
	//again, small list just for tests
	

	while (entry != "exit") {
		cout << "Please, enter the name of the text file:\n";
		cin >> entry;
		if (entry == "exit") {
			break;
		}
		entry += ".txt";
		cout << "Opening " + entry + "\n";
		inFile.open(entry);
		if (!inFile) {
			cout << "The specified file does not exist or bugged out\n";
			cout << "Please, try again\n";
			cout << "Or type exit to exit\n";
			cout << "\n";
			//error in case of wrong file name
		} else {
		while (!inFile.eof()) {
			getline(inFile, line);
			word = "";
			for (auto x : line) {
				if (x == ' ' || x == ';' || x == '\'' || x == '\n') {
					if (x == ' ') {
						space++;
					}
					for (unsigned int i = 0; i < strlen(chars); ++i) {
						word.erase(remove(word.begin(), word.end(), chars[i]), word.end());
					}
					cout << word << endl;
					for (int i = 0; i < 15; i++)
					{
						if (word.compare(keywords[i]) == 0) {
							keyword++;
						}
					}
					for (int i = 0; i < 7; i++)
					{
						if (word.compare(numbers[i]) == 0) {
							number++;
						}
					}
					for (int i = 0; i < 3; i++)
					{
						if (word.compare(signs[i]) == 0) {
							sign++;
						}
					}
					for (int i = 0; i < 3; i++)
					{
						if (word.compare(characters[i]) == 0) {
							character++;
						}
					}

					word = "";
				}
				else if (x == '(') {
					word = word + x;
					x++;
					if (x == ')') {
						funct++;
					}
				}
				else
				{
					word = word + x;

				}

			}
		}
		break;
		}
	}
	cout << "There are " << keyword << " keywords\n";
	cout << "There are " << number << " numbers\n";
	cout << "There are " << sign << " signs\n";
	cout << "There are " << character << " characters\n";
	cout << "There are " << space << " spaces\n";
	cout << "There are " << funct << " functions\n";
	inFile.close();

	return 0;
}