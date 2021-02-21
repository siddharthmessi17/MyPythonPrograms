a = 'hello world'
print(a.upper())
print(a.lower())
print(a.replace('h', 'j'))
print('e' in a)
print(a[:8])
print(a[2:])
print(a[-5:-2])
if 'eelo' in a:
    print('present')
else:
    print('absent')
print(type(a))

b = 10
print(type(b))
b = float(b)
print(type(b))

# below code explains the concept of formatting using method format()
quantity = 3
item_no = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, item_no, price))

# back slash is the escape character
# txt = "We are the so-called "Vikings" from the north.".....this will give error
txt = "We are the so-called \"Vikings\" from the north."  # this wont because of the escape character

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# lists
thislist = list(("apple", "banana", "cherry"))  # list created with list() constructor...note the double rounded ()ets.
print(thislist)
# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# syntax is: newlist = [expression for item in iterable if condition == True]
# The condition is like a filter that only accepts the items that valuate to True.
# The condition is optional and can be omitted
# The iterable can be any iterable object, like a list, tuple, set etc
# The expression is the current item in the iteration,
# but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
# You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]  # return orange for banana
# The expression in the example above says:
# "Return the item if is not banana, if it is banana return orange".

sid = {'age': 23, 'place': 'pune', 'sex': 'male'}
key_list = list(sid.keys())
val_list = list(sid.values())
pos = key_list.index('sex')
# print(val_list[pos])

value = sid['place']
# print(value)

# for ke in sid:
    #print(ke, sid[ke])
# print(dir(()))

 #   x = 89.75839
  #  text = 'I will buy ONGC at a price of {:.1f}'
  #  print(text.format(x))



