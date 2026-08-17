# 1.remove lowercase substring
# ----------------------------

s = input("enter a string:")
enter a string:RohithSubramanian
result =""
for i in s:
    if not i.islower():
        result += i

        
print(result)
RS

# 2.Evaluate an expression
# ------------------------

x = input("enter an expression:")
enter an expression:24+27
print(eval(x))
51

# 3.Insert spacing between uppercase
# ----------------------------------

s = input("enter a string:")
enter a string:RohithSubramanian
result =""
for i in range(len(s)):
    if s[i].isupper() and i != 0:
        result += " "
    result += s[i]

    
print(result)
Rohith Subramanian

# 4.remove the parenthesis area in a string
# -----------------------------------------

s = input("Enter a string:")
Enter a string:Rohith (hi guys) Subramanian
result =""
inside = False
for i in s:
    if i =="(":
        inside = True
    elif i ==")":
        inside = False
    elif not inside:
        result += i

        
print(result)
Rohith  Subramanian

# 5.Split a string with multiple delimiters
# -----------------------------------------

s = input("Enter a string:")
Enter a string:apple,banna:orange;grape|strawberry
result = ""
s = s.replace(":",",")
s = s.replace(";",",")
s = s.replace("|",",")
result = s.split(",")
print("Result:",result)
Result: ['apple', 'banna', 'orange', 'grape', 'strawberry']

# 6.Find all adverbs and their positions
# --------------------------------------

s = input("Enter a string:")
Enter a string:Rohith  quickly completed the work and carefully checked it
words = s.split()

position = 0

for word in words:
    if word.endswith("ly"):
        print("Adverb:",word, "Position:", position)
    position = position+1

    
Adverb: quickly Position: 1
Adverb: carefully Position: 6


# 7.Case-insensitive string replacement
# -------------------------------------

s = input("Enter a string:")
Enter a string:hello guys
x = input("Enter a key:")
Enter a key: Hi
s = s.split()
result = ""

for i in s:
    if i.lower() == "hello":
        result = result + x
    else:
        result = result + i + " "

        
print("Result:", result)
Result:  Higuys 

# 8.Split a string at uppercase letters
# -------------------------------------

s = input("Enter a string:")
Enter a string:RohithIsLookingGood
result = ""
for i in range(len(s)):
    if s[i].isupper() and i !=0:
        result += " "
    result += s[i]

    
print(result)
Rohith Is Looking Good


# 9.Remove everything except alphanumeric characters
# --------------------------------------------------

s = input("Enter a string:")
Enter a string:Rohith@123#Python!
result =""
for char in s:
    if char.isalnum(): # isalnum is used to check the leter  is alphanumeric or not
        result = result+char

        
print("After removing:", result)
After removing: Rohith123Python

# 10.Remove all white spaces
# --------------------------

s = input("Enter a string:")
Enter a string:Rohith VS
result = ""
for i in s:
    if i != " ":
        result = result + i

# 11.Extract values between quotation marks
# -----------------------------------------

s = input("enter a string:")
enter a string:He said "hello" and "welcome"
result = ""
inside = False

for ch in s:
    if ch == '"':
        inside = not inside
    elif inside:
        result = result + ch

        
print(result)
hellowelcome


# 12.convert snake case to camel case
# -----------------------------------

s=input("Enter a snake case string: ")
Enter a snake case string: my_dream_car
words = s.split("_")
result = words[0]

for word in words[1:]:
    result = result + word.capitalize()

    
print("Camel case string:",result)
Camel case string: myDreamCar

# 13.Check whether a year is a leap year
# --------------------------------------

year = int(input("Enter a year:"))
Enter a year:2004
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")

    
leap year


# 14.Convert a string to datetime
# -------------------------------
                     

from datetime import datetime
                     
s = input("Enter date (YYYY-MM-DD): ")
                     
Enter date (YYYY-MM-DD): 2004-05-24
date = datetime.strptime(s, "%Y-%m-%d")
                     
print("Converted datetime:", date)
                     
Converted datetime: 2004-05-24 00:00:00

# 15.Count uppercase and lowercase letters
#-----------------------------------------

def count_letters(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper = upper+1
        elif ch.islower():
            lower = lower+1
    return upper ,lower

s = input("Enter a string: ")
Enter a string: RohithSubramanian
upper, lower = count_letters(s)

print("Uppercase letter:", upper)
Uppercase letter: 2
print("Lowercase letter:", lower)
Lowercase letter: 15

# 16.Remove duplicate elements from a list
# ----------------------------------------

def unique_list(x):
    result = []

    for num in x:
        if num not in result:
            result.append(num)

    return result

x = input("Enter numbers: ").split()
Enter numbers: 1 2 2 2 3 3 4 5 5
new_list=[]

\
for num in x:
    new_list.append(int(num))

    
answer = unique_list(new_list)
print("Unique elements:", answer)
Unique elements: [1, 2, 3, 4, 5]

# 17.Check whether a number is prime
# ----------------------------------

def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

    
num = int(input("Enter a number: "))
Enter a number: 27
answer = prime(num)

if answer:
    print("prime number")
else:
    print("not a prime number")

    
not a prime number


# 18.Print even numbers from a given list
# ---------------------------------------

x = input("Enter numbers: ").split()
Enter numbers: 1 2 3 4 5 6 7 8
new_list=[]

for i in x:
    new_list.append(int(i))

    
print(new_list)
[1, 2, 3, 4, 5, 6, 7, 8]

for num in new_list:
    if num % 2 == 0:
        print(num)

        
2
4
6
8


# 19.Check whether a number is perfect
# ------------------------------------

def perfect_num(x):
    total = 0
    for i in range(1, x):
        if x % i == 0:
            total = total+i
    if total == num:
        return True
    else:
        return False

    
num = int(input("enter a number: "))
enter a number: 24
answer = perfect_num(num)

if answer:
    print("Perfect number")
else:
    print("Not a perfect number")

    
Not a perfect number

# 20.Reverse a string word by word
# --------------------------------

s = input("Enter a string: ")
Enter a string: I am coding 
words = s.split()

result = ""

for i in range(len(words) -1, -1, -1):
    result = result + words[i] + " "

    
print("reversed string:", result)
reversed string: coding am I 


        
print(result)
RohithVS
