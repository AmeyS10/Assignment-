Class1 (06/09/2022)

[ ]
print("Hello World!!")
Hello World!!
[ ]
# -> comments starts with # python will ignore
# Creating a variable
a = "hello everyone" # -> anything inside "__" string
print(a)
print(type(a))
hello everyone
<class 'str'>
[ ]
n1=1234
n2=5678
sum1 = n1+n2
sum2 = n2-n1
sum3 = n1*n2
sum4 = n2/n1
print(sum1,sum2,sum3,sum4)
print(type(sum1),type(sum2),type(sum3),type(sum4))
6912 4444 7006652 4.60129659643436
<class 'int'> <class 'int'> <class 'int'> <class 'float'>
[ ]
# Creating a String
name = 'Tom'
print(type(name))
# concatenating => + ,
print("My Favourite Cartoon is "+name)
print("My Favourite Cartoon is",name)
<class 'str'>
My Favourite Cartoon is Tom
My Favourite Cartoon is Tom
[ ]
# Creating a Boolean
#Boolean
print(10>8)
print(10=="10")
print(10<9)
True
False
False
Class2 (06/09/2022)

[ ]
#collection data types in python
[ ]
a = 'Hello Everyone'
b = 25
print("Hey! "+ a + "H" , b)
Hey! Hello EveryoneH 25
[ ]
# collection datatype in python
# list, tuple, set, dictionary
# list => ordered collection of data types, [], mutable (changeable)

mylist = ["Data", "Details", "Access"]
a = [55,4.5,'sa', True]
print(a + mylist)
[55, 4.5, 'sa', True, 'Data', 'Details', 'Access']
[ ]
#Indexing (Printing of Individual data)
a = [55,4.5,'sa', True]
print(a[3])

# Update
a [3] = False
print(a)

# Append => Adding more data
a.append(23)
print(a)

# Insert => Adding specific data
a.insert(0,33)
print(a)

# delete or remove
del a[2]
a.remove(False)
print(a)
print(type(a))
True
[55, 4.5, 'sa', False]
[55, 4.5, 'sa', False, 23]
[33, 55, 4.5, 'sa', False, 23]
[33, 55, 'sa', 23]
<class 'list'>
# This is formatted as code
Class 3 (12/09/2022)

[ ]
# Tuple => ordered collection of datatypes, (), immutable
_tuple_=("Dell", "Asus", "Hp", 27, 37.8)
print(_tuple_)
del _tuple_
print(_tuple_)

[ ]
# Dictionary => It consists of key and the values i.e (KEy: Value) Username : Admin
#; we us flower bracket {}
Dict={
    "Username":["Admin","Admin1"],
    "Password":"Pass",
    "OS":"Windows",
    "Ram":"128GB"
}
print(Dict["Username"])

#update
Dict['Password']=32667
print(Dict)

#Delete / Remove
del Dict["OS"]
print(Dict)
['Admin', 'Admin1']
{'Username': ['Admin', 'Admin1'], 'Password': 32667, 'OS': 'Windows', 'Ram': '128GB'}
{'Username': ['Admin', 'Admin1'], 'Password': 32667, 'Ram': '128GB'}
[ ]
# Index Number => Print individual elements
# Slicing => printing the sequence of elements

a="randomness"
print(a[0:6])
print(a[3:])
print(a[:3])
print(a[-5:])
print(a[:])
print(a[-10:-1])
random
domness
ran
mness
randomness
randomnes
[ ]
# Step Index

b="Python"
print(b[0:6:3])

#Assignment Work on negative slicing

c="Assignment"
print(c[::-3])
Ph
tmiA
