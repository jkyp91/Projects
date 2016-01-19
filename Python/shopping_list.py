#requesting user input and storing the data
# make a list to hold our items
shopping_list = []
#print instructions on how to use

def print_help():
  print("Type the items you plan to buy")
  print("Type 'DONE' when your finished")
  print("Type 'SHOW' to show your list")
  print("Type 'HELP' for the help list")

print_help()
#ask for new items
def add_to_list(new_item):  
  shopping_list.append(new_item)
  
#print list
def print_list():
  print("Here's your list:")
  count = 0
  for item in shopping_list:
    count += 1
    print ("{}. ".format(count), item)
    
#be able to quit app
while True:
  new_item = input("> ")
  
  if new_item == 'DONE':
    break
  elif new_item == 'SHOW':
    print_list()
    continue
  elif new_item == 'HELP':
    print_help()
    continue
  add_to_list(new_item)  

print_list()    
