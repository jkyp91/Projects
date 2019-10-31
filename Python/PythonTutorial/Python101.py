#!/bin/python3

#Print string
print("Strings and things:")
print('Hello World!')
print("""Hello, this is
a multi-line string!""")
print("this is" + " a string")

print('\n') #new line

#Math
print("Math time:")
print(50+50)  #add
print(50-50) #subtract
print(50*50) #multiply
print(50/50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers

#Variables & Methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #turn quote uppercase
print(quote.lower()) #turn lower case
print(quote.title()) #title

name = "John"
age = 27 #int int(29) integer does not round up
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(29.9)) #will print 29 not 30
print("My name is " + name + " and I am " + str(age) + " years old.") #convert age (integer to string)

print('\n') #new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions
print("Now some functions:")
def who_am_i():
	name = "John" #declaring a variable inside a function means variable only resides in the function and cannot be called outside the function
	age = 27
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x + y)

add(5,5)
add(305,207)

#Using return
def multiply(x,y):
	return x * y #return stores the value and saves it for later

print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))

print('\n') #new line

#Boolean expressions (True or False)
print("Boolean expressions:")
bool1 = True #bool
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True" #string
print(type(bool5))

#Relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and, test_or, test_not)

print('\n') #new line
print("Conditional Statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"
print(soda(3))
print(soda(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting Tipsy!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money"
	elif (age > 21) and (money >= 5):
		return "Nice try kid!"
	else:
		return "You're too poor and too young."
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(21,5))

print('\n') #new line

#Lists
print("Lists have brackets:")
movies = ["When Harry Met Sally","The Hangover", "The perks of being a wallflower", "The Exorcist"]

print(movies[0]) #prints 1st movie in list
print(movies[0:2])#if you want 1st 2 movies, you have to call out an additional value (up to but not including)
print(movies[1:]) #slicing - print all movies from 1
print(movies[:1]) #only call up to the first movie
print(movies[-1]) #-1 pulls the last item out of the list
print(movies[-2])
print(len(movies)) #prints no. of movies in the list

movies.append("Jaws") #Add a movie to the list
print(movies)

movies.pop() #without giving it a value it will remove the last item in the list
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry Met Sally","The Hangover", "The perks of being a wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]

#combining lists
combined = zip(movies, person)
print(list(combined))

#Tuples - a list that cannot be modified (cannot append / pop)
print("Tuples have parentheses and cannot change") #Tuples have parantheses (, lists have brackets [
grades = ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
print("For Loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

print("While loops - Execute as long as True:")
i = 1
while i < 10:
	print(i) #will print i until 9
	i += 1

#!/bin/python3

#Importing
print("Importing is important:")

import sys #this is system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def new_line():
	print('\n')

new_line()

#Advanced Strings
print("Advanced Strings:")
my_name = "John"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = "This is a sentence"

print(sentence[:4]) #first word
print(sentence[-8:]) #last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\"" #escape quotes within quotes
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #case sensitive fixed by .lower() (returns True)

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) #True and not False therefore True, True

too_much_space = "         hellow       "
print(too_much_space.strip()) #strips by delimiter (space)
full_name = "ohn Kyprianou"
print(full_name.replace("ohn", "John")) #use .replace to replace aword in a string
print(full_name.find("Kyprianou"))

#Placeholders
movie = "The Hangover"
actor1 = "Alan"
actor2 = "Stew"
print("My favourite movie is {} with {} and {}.".format(movie, actor1, actor2)) #Note the {} acts as a placeholder with the .format()

def favourite_book(title, author):
	fav = "My favourite book is \"{}\", which is written by {}".format(title, author)
	return fav

print(favourite_book("Game of Thrones","George RR Martin"))

new_line()

#Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russians": 7, "Old Fashioned":10, "Lemon Drop": 8, "Buttery Nipple": 6} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Andy", "Ollie"]})
print(employees)

drinks["White Russians"] = 8
print(drinks)
print(drinks.get("White Russians")) #Returns price of white russian
print(drinks.get("Martini")) #Returns none
print(drinks["White Russians"]) #Returns price of white russian

#Lists and dictionaries
movies = ["When Harry Met Sally","The Hangover", "The perks of being a wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)
