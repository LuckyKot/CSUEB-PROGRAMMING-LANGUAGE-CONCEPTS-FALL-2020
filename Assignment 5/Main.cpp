#include <new>
#include <string>
#include <iostream>

using namespace std;


class Time
{
public:
	// Constructors
	Time();
	Time(int hours, int minutes, char AM_PM);
	Time(const Time &org); // copy constructor
	// Destructor
	~Time();

	// accessors
	int getHours() const;
	int getMinutes() const;
	char getAMPM() const;

	// mutators
	void setTime(int hours, int minutes, char AM_PM);
	// overloaded operators member functions go here


private:
	// member variables
	int *hours;
	int minutes;
	char AM_PM;
};

int main() {

	Time testTime;
	Time copyTime;

	cout << "testing default" << endl;
	cout << testTime.getHours() << endl;
	cout << testTime.getMinutes() << endl;
	cout << testTime.getAMPM() << endl;
	cout << endl;

	cout << "testing setTime" << endl;
	testTime.setTime(3, 55, 'P');
	cout << testTime.getHours() << endl;
	cout << testTime.getMinutes() << endl;
	cout << testTime.getAMPM() << endl;
	cout << endl;

	cout << "testing copy" << endl;
	copyTime = testTime;
	cout << copyTime.getHours() << endl;
	cout << copyTime.getMinutes() << endl;
	cout << copyTime.getAMPM() << endl;
	cout << endl;

	cout << "testing invalid inputs" << endl;
	testTime.setTime(45, 129, 'Z');
	cout << testTime.getHours() << endl;
	cout << testTime.getMinutes() << endl;
	cout << testTime.getAMPM() << endl;
	cout << endl;

	cout << "testing user inputs" << endl;
	int x = 0;
	int y = 0;
	char z = 0;
	cin >> x;
	cin >> y;
	cin >> z;
	testTime.setTime(x, y, z);
	cout << testTime.getHours() << endl;
	cout << testTime.getMinutes() << endl;
	cout << testTime.getAMPM() << endl;
	cout << endl;

	return 0;
}

Time::Time() : minutes(0), AM_PM('A')
{
	hours = new int;
	*hours = 12;
}

Time::Time(int h, int m, char AP)
{
	hours = new int;
	setTime(h, m, AP);
}

Time::Time(const Time &org) : minutes(org.minutes), AM_PM(org.AM_PM)
{
	hours = new int;
	*hours = *org.hours;
}

Time::~Time()
{
	delete hours;
}

int Time::getHours() const
{
	return *hours;
}

int Time::getMinutes() const
{
	return minutes;
}

char Time::getAMPM() const
{
	return AM_PM;
}

void Time::setTime(int h, int m, char AP)
{
	if (h >= 1 && h <= 12)
	{
		*hours = h;
	}
	else
	{
		*hours = 12;
	}
	if (m >= 0 && m <= 59)
	{
		minutes = m;
	}
	else
	{
		minutes = 0;
	}
	if (AP == 'A' || AP == 'P')
	{
		AM_PM = AP;
	}
	else
	{
		AM_PM = 'A';
	}
}