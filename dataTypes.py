#int, float, str, bool, list, dict, tup, set

a = 10
b = 20
sum = a+b
print(sum)

c = 1.2
d = 20.3

name = "nitish"
designation = "tester"

is_valid_user = False  #this is snake casing, in java we use camel case
# spaces are not allowed in any programming language in names of variable
# cannot use special characters
# good to have lowercase
# case sensitive
# use snake casing in python to define variable names

def sum():
    a = 10
    b = 20
    print(a+b)
print("hello") #this does not have the same indentation so it is not part of sum method

area = 10
print(type(area))

area = "10"   #we can change the type of variable at any time in python because it is dynamically typed language
                #whereas java is statically typed langauge, we cannot change data type
print(type(area))

area = True
area = 10.2


#to calculate tax
income = 10000
tax_percentage = 0.2
tax = income * tax_percentage
print(tax)


#strings: ordered sequence of characters
name = "sam" # reverse indexing 012  0 -2 -1
first_name = "seith"   # 01234      0 -4 -3 -2 -1

#Indexing and slicing
print(name[1]) #it will print 'a'
#print(name[3]) #it will throw error index out of range

print(first_name[-3]) #it will print 'i'

#slicing
str_alphabets = "abcdefg"
print(str_alphabets[0:3]) #it will print index 0,1 and 2 not index 3 #string[startIndex:stopIndex]
print(str_alphabets[:4]) #you dont need to give first index if its 0
print(str_alphabets[2:6])
print(str_alphabets[0:7:2]) #string[start:stop:step]
print(str_alphabets[::-1])

#String is immutable
name = "tim"
#name[1] = "o" #changing tim to tom by modifying the string
name1 = name[0] + "o" + name[-1]
print(name1)


