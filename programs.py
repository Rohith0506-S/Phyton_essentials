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


