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

        
print(result)
RohithVS
