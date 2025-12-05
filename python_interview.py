# Fibonacci series 

a =0
b =1
n =10
for i in range(n):
    print(a)
    c =a+b
    a =b
    b =c

# Write a program in Python to check whether a number is palindrome or not using recursive method

num =int(input("Enter the value"))

i =2

while num>1:
    if num %i ==0:
        print(i)
        num =num//i
    else: 
        i+=1        

# Write a program in Python to find given number is perfect or not

num =int(input("neter the number"))

sum_of_numbers =0
i =1

while i<num:
     if num % i ==0:
         sum_of_numbers +=i
     i =i+1
if sum_of_numbers ==num:
    print("thi is perfect square number")
else:
    print("this is not a perfect square number")    


# Python Program to calculate factorial using iterative method

num =int(input("enter the number"))

factorial =num
i = 1

while num>i:
    factorial *=i
    i+=1

print(factorial)    


# Python program to calculate the power of any number

base =int(input("Enter the number"))
exponent =int(input("Enter the number"))

i =1
result =1

while i <=exponent:
    result =result*base
    i+=1

print(result)    

# merged two dictionaries 

dict1 ={"a":1,"b":2,"c":3}
dict2 ={"d":4,"e":5}

merged =dict1 | dict2
print(merged)

# using second method

merge ={**dict1,**dict2}
print(merge)


# find the longest word in the string

str ="This fox is jump over the wall"

str1=str.split()

longest =" "

for i in str1:
    if len(i) >len(longest):
        longest =i

print(longest)        


# Write a Python code to find the first non-repeating character in a string

str1 ='swiss'

frequency ={}

for ch in str1:
    if ch not in frequency:
        frequency[ch]=1
    else:
        frequency[ch]+=1

for ch in str1:
    if frequency[ch]==1:
        print(ch)
        break
        

# Create a Python program to determine how many capital letters are in a string.
        
str2 ='hellO WORLd'

count =0

for ch in str2:
    if ch >='A' and ch<='Z':
        count+=1
print(count)        


# How do you count digits, letters, and spaces in a string?

str3 ='Hello 098'

letters = 0
digits = 0
spaces = 0

for ch in str3:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letters += 1

    elif '0' <= ch <= '9':
        digits += 1    

    elif ch == ' ':
        spaces += 1

print(letters,digits,spaces)        
    