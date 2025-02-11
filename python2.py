print ("hello world")

print(5+3)
print(23546+4)
print(0*20)

print(23*2)
type(20)
class'int'
a=23
print(type(a))
class'int'
x=23
y=12
print(x+y)
print("Sr engineering college")
print("kanna")

x=2
print(x+1)
  x="kanna"
  y="
  
  
  fruits = {"apple", "banana", "cherry"} 
numbers = {1, 2, 3, 4}                  
frozen_fruits = frozenset(["apple", "banana", "cherry"])  
print(frozen_fruits)


x="12a"
print(type(x))


y=False
print(type(y))
a="'hello'world"
print("'hello'world")
print(type(a))
print('"nandhini/b" \n 2')
x=("what\tb")
print("what\tb")
print(type(x))
list1=[1,2,5,8]
print(type(list1))

z=1,2,3
print(type(z))
print(z)
# Example 2: Accessing elements by index
fruits = ["apple", "banana", "cherry",'mango','orange']
print(fruits[-4])  # Output: apple
print(fruits[-5])  # Output: banana
print(fruits[2]) # Output: cherry (negative index accesses from the end)

print("venky" + " " +  "preethi")
kanna="preethi"*3 +" " + "kanna"*3
print(kanna) 

# Indexing a string
text = "Python"
print(text[0])   # Output: P (first character)
print(text[2])   # Output: t (third character)
print(text[-1])  # Output: n (last character)
text = "preethi"
print(text[2])
print(text[-3])

text = "Hello, World!"
print(text[0:5])  # Output: 'Hello'
print(text[7:])   # Output: 'World!'

name ="preethi"
name2="kanna"
age =26
message = f"{name + name2} are {age} years old"
print(message)
name = "kanna"
name2 = "preethi"
message =f"{name} loves {name2}"
print(message)










name = "srinivas"
name2 ="kanna"
message = f"{name} is father of {name2}"
print(message)

string ="hello, good morning all"
message = f"string\n\t good morning all"
print (string)

string = "venkateshnagunoori,?"
print(len(string))
string = "   Python Programming   "

split_string = string.split() 
print(split_string)


string ="   Venky Nagunoori   "
print(string.strip())
print(string.lower())
print(string. upper())
print(string. replace("Venky","Preethi"))
split_string=string.split()

string = "Venky Nagunoori"

joined_string = "-".join(string) 
print(joined_string)

string = "Venky Nagunoori"
split_string = string.split()  # Splitting the string into words
joined_string = "-".join(split_string)  # Joining with a hyphen
print(joined_string)
string = "Venky Nagunoori"
# Join characters of the string with a hyphen
joined_string = "-".join(string)
print(joined_string)

string = "Venky Nagunoori"
# Split the string into words and join with a hyphen
joined_string = "-".join(string.split())
print(joined_string)



string = "ven"
print(string.isalpha())
print(string.isdigit())
print(string.isalnum())

string ="   venky nagunoori   "
print(string.strip())
print(string.lower())
print(string.upper())
print(string.replace("venky", "Nagunoori"))
split_string = string.split()
print(split_string)
joined_string = "_".join(split_string)
print(joined_string)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(6))  # Output: 120


string = "venkatesh"
string2 = "preethi"
print(string+ " " + string2)

string = "preethi"
string2 = "venkatesh"
print(len(string))

string = "preethi"
string2 = "venkatesh"
print(len(string)


name = "ven"
name2 = "preethi"
print(name + " "+ name2)





my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[2:6])
print(my_list[1;3]) + (my_list[])



x = 10
y = 20

# Both conditions must be true
if x > 5 and y < 30:
    print("Both conditions are true")
else:
    print("At least one condition is false")


my_list = [1, 2, 3, 4, 5, 6]
my_slice = my_list[-3:-1]  
print(my_slice)


name = "srinivas"
name2 = "jyothi"
print(name + " " + name2)
print(len(name + name2))
print(name[1:5])


name = "hello"
print(name[::-1])



a =34
b = 43
print(a>b)
print(a<b)
c = 4
d = 4
print(a=>b)

a = 34
b = 43

print(a > b)   # Checks if a is greater than b
print(a < b)   # Checks if a is less than b

c = 4
d = 4
print(a >= b)  # Checks if a is greater than or equal to b



name = "kanna"
name1 = "preethi"
print(name + " " +name1)
a = 5
if not a < 0:
    print("a is not negative")
else:
    print("a is negative")

a = 5
if not a < 0:
    print("a is not negative")
else:
    print("a is negative")
 g = 43
 if not g>0:
 print("g is not a negative")
 else:
 print("g is negative")
 
 
 g = 43
if not g > 0:
    print("g is not a negative")
else:
    print("g is negative")


def fibonacci(n):3
    fib_series = [0, 1]  # Starting values
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])  # Sum of last two numbers
    return fib_series[:n]  # Return the series up to 'n' terms

# Example usage
n = int(input("Enter the number of Fibonacci terms: "))
print(f"Fibonacci Series: {fibonacci(n)}")

Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print(f1)
