#the floor division // rounds the result down to the nearest whole number
x = 15
y = 2

print(x // y)
# (**) - is called exponential 
a = 7
b = 4
print (7**4)


#if statement : used when if statement is true
a = 33
b = 200
if b > a:
    print("b is greater than a")


#else if statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  #using and logical operator 
  #used when both conditions are true
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#using or logical operator
#used when one condition is true
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#using not operator
#used to reverse the condition 
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#nested if
#You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# pass statement
#if statements cannot be empty,put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

#The while loop
# used to execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1
# the break statement
# used to stop the loop even if the while condition is true
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement
#we can stop the current iteration, and continue with the next

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#else statement: used once the condition is no longer true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  #loops: used for iterating over a sequence
#the break statement
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# continue statement: stop the current iteration loop and continue with the rest
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#range() function
for x in range(6):
  print(x)
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
  


