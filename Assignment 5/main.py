class Time:

    def __init__(self):
        self.hours = 12
        self.minutes = 0
        self.AM_PM = 'A'

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getAM_PM(self):
        return self.AM_PM

    def setTime(self, hours, minutes, AM_PM):
        if (hours >= 1 and hours <= 12):
            self.hours = hours
        else:
            self.hours = 12
        if (minutes >= 0 and minutes <= 59):
            self.minutes = minutes
        else:
            self.minutes = 0
        if (AM_PM == 'A' or AM_PM == 'P'):
            self.AM_PM = AM_PM
        else:
            self.AM_PM = 'A'


Test1 = Time()

print("testing default")
print(Test1.getHours())
print(Test1.getMinutes())
print(Test1.getAM_PM())

print("testing setTime")
Test1.setTime(2, 40, 'P')
print(Test1.getHours())
print(Test1.getMinutes())
print(Test1.getAM_PM())

print("testing invalid inputs")
Test1.setTime(25, 102, 'Z')
print(Test1.getHours())
print(Test1.getMinutes())
print(Test1.getAM_PM())

print("testing user input")
Test1.setTime(int(input("H\n")), int(input("M\n")), input("AP\n"))
print(Test1.getHours())
print(Test1.getMinutes())
print(Test1.getAM_PM())
