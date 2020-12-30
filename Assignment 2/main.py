# CS311 Assignment 2
# Python test of tool
# --

a = 10
b = 12

# 1. Interpretation
# a. Very hard to show in a program
# The most basic is that it reads the code from top to bottom
print(a)
print(b)
# b. Reads the program line be line, will print 10 first, 12 second
# In C it would compile the code into an EXE file or some other file
# c. I mean it's just a feature, it's just how it works, not much to critique

# 2. Boolean expression
# a. sample:
c = True
d = False
if a > b:
    print('10 > 12')
else:
    print('12 > 10')

if c:
    print(c)
else:
    print(d)
if d:
    print(c)
else:
    print(d)

# b. Uses boolean variables, evaluates certain "claims", expressions and defines them as True or False
# here it evaluates the expression a > b. This will result into False and the program will print 12 > 10
# it can also take into account already existing bool variables like in this c and d example
# in general, it is pretty simple and similar to other languages
# c. it's pretty simple, nothing to complain about

# 3. short circuit evaluation
# a.
if a > b or b > a:
    print('a > b')
if b > a and a > b:
    print('wrong')
else:
    print('right')
# b. short circuit evaluation is an efficiency tool
# it works with 'or' and 'and' operators
# if the first expression of 'or' is true, this will automatically pass the whole thing as true
# if the first expression of 'and' is false, it evaluates the whole thing as false
# it does exist in c++, not sure if it is different technically
# c. I mean it's just a good bonus feature that saves time

# 4. numeric types
# a.
print(int(322))
print(float(322.22))
print(complex(32.22, 15))
print(bool(1))
print(bool(0))
# b. numeric types are variables that operate on numbers
# 3 major types and 1 subtype
# int for integer, float for floating point, complex for complex numbers with imaginery part
# subtype is boolean, it can work with 1s(True) and 0s(False)
# C++ has more types, short or long ints, short or long doubles, short or long floats, unsigned types of these variables too
# not sure if C without libraries has complex numbers though
# c. I think it is kind of oversimplified

# 5. strings
# a.
e = 'This is a string'
print(e)
print(e[:4])
# b. basically an array specifically made for sentences
# does not need specifications for how much space to allocate
# python is famous for its easy use of strings in general and there are also various built-in tools to work with them
# while in C you it requires a whole library and a bunch of self-made functions to work well
# c. This is actually worth praising, not criticizing. Although memory management is obviously lacking

# 6. arrays
# a.
f = 0,1,2,3,4,5,6,7,8,9,10
print(f[2])
print(e[2])
# b. a row of numbers or ascii symbols
# again, much easier in python, does not require to specify the length of array and has same tools as string
# C needs length, C needs type, C is harder to use in general
# c. same as strings, ease of use is good, lack of memory control is kinda bad

# 7. lists
# a.
testlist = ["green","blue","red"]
print(testlist[2])
# b. list is basically an array for strings
# in python, again, much easier, you just make a usual array but use "word" instead of number or symbols
# in C, again, you need either a library, or create whole class to work with lists comfortably
# constructors, destructors, copy, functions to append list, function to delete and so on
# c. I would take easier time with lists over memory management any time, because i'm lazy, so I don't think I can criticize this

# 8. tuples
# a.
testtuple = ("green","blue","yellow")
print(testtuple[2] + ' ' + testtuple[1])
# b. an unchangable list
# before discovering python I've never even heard about tuples, so it's one of python's features
# not even sure how to implement this in C, because of how much stuff you need for just a list
# c. I can't really critique this, I never used them

# 9. slices
# a.
x = slice(0,2,1)
print(testtuple[x])
# b. slices the array,list,or tuple by skipping X amount of entries
# you just need to specify start,end and how much to skip
# once again, in C you need a whole program on its own to do this reliably
# in python it is one function
# c. same thing, it's very good to have a tool in one function
# rather than make multiple functions that would do the same thing in C
# however, I never used this, so I can't really critique

# 10. index range checking
# a.

# b. There is no such function in python really
# no such function in C either
# c. a shame you have to check this on your own

# 11. dictionaries
# a.
testdict = {
    "big": "small",
    "long": "short",
    "old": "young"
 }

print(testdict["big"])
# b. works like a phone book, you enter one word - it will give you a corresponding word from the dictionary
# I have never seen such a thing in C, so it must be another do-it-yourself thing
# c. This one is actually a lot of work to set up, although it must be much less than create dictionary in C from scratch

# 12. if statements
# a.
if (a < b):
    print("tested")
# b. This one is actually quite minimal, clean and simple.
# C is pretty similar to this one, except you use { } to mark code blocks
# also else if here is elif, saves some time and effort
# c. I actually hate the fact that indentation plays such a huge role

# 13. switch statements
# a.

# b. I am surprised that there is NO switch statement in python. One can certain make an alternative by hand, but
# matter of fact, it doesn't exist as is. I never used it in C though, so I can't say I miss it much
# in C you type switch(expression) and make case 1, case 2, etc, with code that will be executed and a break statement
# c. Can't critique something that doesn't exist and I won't critique it's absence. Never liked switch statements

# 14. for loop
# a.
for x in range(6):
    print(x)
# b. For loop is extremely weird in python to be honest, after all other languages
# In C for loop is big and bulky, but it's rather simple for(int i;x<y;i++)
# This is very straightforward, while python is oriented for strings/tuples/etc
# for each position in array/string do this
# c. I critique the weirdness of for loop in python

# 15. while loop
# a.
while a < 20:
    a += 1
    print("+1")
print("a is 20 now")
# b. while loop is pretty straightforward in python, unlike for
# just like in C, it just takes some expression that can be evaluated to True or False
# Then either does the code if it's True or skips it if it's False
# C is very similar and only format changes: while(expression) { do this }
# c. Again, indentation to define code blocks is just not good for me

# 16. indentation to denote code blocks
# a.
for x in range(6):
    print(x)
print(x)
# b.This code will print numbers from 0 to 5 and 5 will be printed twice, because one print(x) is a part of loop
# and another print(x) is not a part of for loop due to indentation
# in C {} denote code blocks and indentation is mostly for readability
# c. This I really dislike about python, i'd take {} any time, although they are very confusing at times

# 17. type binding
# a.

# b. Doesn't really exist in python, it is a Dynamic Type Binding language, meaning it assigns the type after the user
# types the value
# in C you always have to specify type and be careful with conversions (static binding)
# c. I don't really like it, I want to be able to restrict the variable to be a certain type

# 18. type checking
# a.
typetest = "hi"
typetestT = 12.5
print(type(typetest))
print(type(typetestT))
# b. There is a type() command to check the type of variable, you just insert the variable and it will return the type
# Similar thing in C is typeid operator, however, it is slightly more complicated and it is also not as important
# Since you have to keep track of them anyway
# c. I like this one, it's pretty neat, but would it be necessary if there was type binding?

# 19. functions
# a.
def testfunction():
    print("testing testing")
testfunction()
# b. keyword def to define a function name and it's arguments, : to start the function insides, indentation to control
# what's a part of it and what isn't. functionname() to call it
# again, pretty similar to C, except for format and that def bit, in C you can assign a type to function and the
# fact that C has pointers, so the function can modify multiple variables of main program
# c. it is fairly restricted compared to C

# 20. Pointers
# a.

# b. They do not exist in python
# Although I was struggling with them in C and still do sometimes, they come in very handy in some situations
# I have not been working too much with python, so I don't know what people use in cases where they would use pointers in C
# c. Absence of pointers, but are they needed here? not sure
