Project: 0x09. Python - Everything is object

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a newline character
The first line of all your script files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc


.txt Answer Files
Only one line
No Shebang
All your files should end with a new line

Task 0
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

Task 1
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

Task 2
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

Task 3
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

Task 4
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

Task 5
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

Task 6
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

Task 7
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

Task 8
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

Task 9
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

Task 10
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

Task 11
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

Task 12
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

Task 13
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

Task 14
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

Task 15
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

Task 16
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

Task 17
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

Task 18
What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

Task 19
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

Task 20
a = ()
Is a a tuple? Answer with Yes or No.

Task 21
a = (1, 2)
Is a a tuple? Answer with Yes or No.

Task 22
a = (1)
Is a a tuple? Answer with Yes or No.

Task 23
a = (1, )
Is a a tuple? Answer with Yes or No.

Task 24
What does this script print?

a = (1)
b = (1)
a is b

Task 25
What does this script print?

a = (1, 2)
b = (1, 2)
a is b

Task 26
What does this script print?

a = ()
b = ()
a is b

Task 27
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

Task 28
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
