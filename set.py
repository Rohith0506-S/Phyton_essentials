Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python Collections / Non-primitive Datatypes
>>> #--------------------------------------------
>>> 
>>> # set
... 
... # set is an unordered collection of data items
... # set values are unindexed
... # set never supports duplicates
... # popping allowed from beginning to end
... 
>>> 
>>> basket = {'apple','orange','pear','banana'}
>>> basket
{'banana', 'apple', 'pear', 'orange'}
>>> type(basket)
<class 'set'>
>>> basket.add('watermelon')
>>> 
>>> basket
{'banana', 'watermelon', 'apple', 'pear', 'orange'}
>>> basket.add('orange')
>>> basket
{'banana', 'watermelon', 'apple', 'pear', 'orange'}
basket.pop()
'banana'
basket
{'watermelon', 'apple', 'pear', 'orange'}
basket.remove('apple')
basket
{'watermelon', 'pear', 'orange'}
basket.update(['banana','apple'])
basket
{'banana', 'watermelon', 'apple', 'pear', 'orange'}

#Set Operations
#--------------
squares = {1,4,9,16,25,49,64,81,100}
cubes = {1,8,,27,64,125,216,343,512,729,10000}
SyntaxError: invalid syntax
cubes = {1,8,27,64,125,216,343,512,729,10000}

squares
{64, 1, 4, 100, 9, 16, 49, 81, 25}
cubes
{512, 1, 64, 8, 10000, 343, 216, 729, 27, 125}
squares.defference(cubes)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    squares.defference(cubes)
AttributeError: 'set' object has no attribute 'defference'. Did you mean: 'difference'?
squares.difference(cubes)
{100, 4, 9, 16, 49, 81, 25}
squares.intersection(cubes)
{64, 1}
cubes.difference(squares)
{512, 8, 10000, 343, 216, 729, 27, 125}
cubes.difference(squares)
{512, 8, 10000, 343, 216, 729, 27, 125}
squares
{64, 1, 4, 100, 9, 16, 49, 81, 25}
cubes
{512, 1, 64, 8, 10000, 343, 216, 729, 27, 125}

#creates an empty set
set1
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    set1
NameError: name 'set1' is not defined. Did you mean: 'set'?
set1
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    set1
NameError: name 'set1' is not defined. Did you mean: 'set'?
set()
set()
set1 = set()
set1
set()





#creates an empty set
set1 = set()
\
set1
set()
type(set1)
<class 'set'>
set1.add(1)
set1.update([4,9,16,20])
squares
{64, 1, 4, 100, 9, 16, 49, 81, 25}
set1
{1, 4, 9, 16, 20}
set1.difference_update(aquares)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    set1.difference_update(aquares)
NameError: name 'aquares' is not defined. Did you mean: 'squares'?
set1.difference_update(squares)

set1.difference_update(squares)
set1
{20}
set1.intersection_update(squares)
set1
set()
squares.intersection_update(set1)
squares
set()
set1.update([4,9,16,25])
set1
{16, 9, 4, 25}
set1.add(45)
set1
{4, 9, 45, 16, 25}
squares
set()
squares.update([1,4,9,16,25,36,49,64,81,100])
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
set1
{4, 9, 45, 16, 25}
set1.intersection_update(squares)
set1
{16, 9, 4, 25}
set1.issubset(squares)
True
squares.issuperset(set1)
True
set1.isdisjoint(squares)
False
set1.symmetrice_difference_update(squares)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    set1.symmetrice_difference_update(squares)
AttributeError: 'set' object has no attribute 'symmetrice_difference_update'. Did you mean: 'symmetric_difference_update'?
set1.symmetric_difference_update(squares)
set
<class 'set'>
set1
{64, 1, 36, 100, 49, 81}
