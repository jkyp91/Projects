import random
#ALTERNATIVE LIST COMPREHENSION (this is practice with functions):
#print[random.randint(1,50) for i in range(5)]
#the above would simply provide 5 numbers..Crazy simple compared to the following:
#generate 5 numbers between 1-50
def five_numbers():
  numbers = []
  
  while True:
    num = random.randint(1,50)
    numbers.append(num)
    if len(numbers) >= 5:
      print("Your winning numbers are: ")
      print(sorted(numbers))
      break
#generate 2 lucky stars between 1-11      
def lucky_stars():
  stars = []
  
  while True:
    two_stars = random.randint(1,11)
    stars.append(two_stars)
    if len(stars) >= 2:
      print("And your lucky stars are: ")
      print(sorted(stars))
      break
      
five_numbers()
lucky_stars()
