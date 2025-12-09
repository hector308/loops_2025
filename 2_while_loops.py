#notes
#while loop= execute some code while some condition remains true
# name=input("Enter your name:")
# while name=="":
#     print("You did not enter your name")
#     name=input ("Enter your name:")
# else:
#     print(f"Hello {name}.")
# age= int(input("Enter your age:"))
# while age<0:
#     print("Age can't be negative.")
#     age=int(input("Enter your name:"))
# else print (f"You are {age} years old.")
# foodlist=[1]
# food=input("Enter a food you like (q to quit):")
# while not food=="q":
#     print(f"You like {food}")
#     foodlist.append(food)
#     food=input("Enter another food you like: (q to quit)")
# print("Bye")
# print(foodlist)
# num=int(input("Enter a number between 1 and 10:"))
# while num<1 or num>10:
#     print("Number not valid.")
#     num=int(input("Enter a number between 1 and 10:"))
# print(f"Your number is {num}.")
# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".

i = 0
while i < len(colors):
    if colors[i] == "yellow":
        break
    print(colors[i])
    i += 1
# Do NOT print "yellow" — stop before it.
