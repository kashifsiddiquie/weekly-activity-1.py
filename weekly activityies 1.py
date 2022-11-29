# chapter 3.py 
# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
## Ask user to guess a number .
# if user guessed correctly then print "You WIN !!!!"
# if user didn't guessed correctly then :
# if user guessed lower than actual number then print “too low"
# if user guessed higher than actual number then print “too high’

# google “how to generate random number in python " to generate rand
# winning number



# EXERCISE SOLUTION
winning_number = 27
user_input = input(“guess a number b/w 1 and 100 : ")
usér_input = int(user_input)
if user_input == winning_number:
print("YOU WIN !!!")
else: # nested if else
if user_input < winning_number:
print(“too low")
else:
print(“too high")


# check two conditions at same time
# and , or
name = ‘abc’
age = 19
if name=='abcd' or age==23:
print("condition True")
else:
print("condition False")







# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with ('a' or ‘A') and age is above 10 then
# Print ‘you can watch coco movie’
# Else print ‘sorry, you cannot watch coco’ |


user_name = input("“enter your name plea
user_age = input(“enter your age please
user_age = int(user_age)
if user_age >= 1p and (user_name[@]=='a
print(“you can watch coco ")
else:
print("you cannot watch coco")



# if elif else statement

# show ticket pricing

#1to3 (free)

# 4 to 10 (150)

#11 to 6@ (250)

# above 60 (200)
age = input("please input your age : ")
age = int(age)

if age==0 or age < @:
    print("you can't watch")
elif @<age<=3:
    prirt. < ‘Ticket price : Free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("ticket price : 250")
else:
    print("Ticket price : 200")




# exercise one of three
# sum of n natural numbers
# ask a user for natural number(n)


n = input(“enter a number : ")
n = int(n)
tétal = 9
i=
while i <= n:
total += i
i¢=1
print(total)



 

# algorithm - (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# exampJe - "1256"
# pick string character one by one and change to int
# int(example[@]) + int(example[1]) .... go upto len(example) - 1

number = input("enter a number ")
# "1256" # length = 4 , last index = 3
# int(number[i])

total = 0
i=@
while i < len(number):
vutal += int(number,1])
i + =1
print(total)



# ask a user for name

# Example - Harshit Vashisth
# print count of each words
# output :
       # H = : 1
       # a = : 2
       # r = : 3 
       # s = : 4
       # h = : 5
       # i = : 6
       #   = : 7
       # v = : 9



    


    name = input("please enter your name ")
    # harsit vashisth

    # harshit
    # name.count("h") , name.count(name[0]) = 2
    # name.count("a") , name.count(name[1]) = 1
    # name.count("r") , name.count(name[2]) = 1
    # name.count("s") , name.count(name[3]) = 1
    # name.count("h") , name.count(name[4]) = 2
    # name.count("i") , name.count(name[5]) = 1
    # name.count("t") , name.count(name[6]) = 1
    
    # output 
    # h : 2
    # a : 1
    # r : 1
    # s : 1
    # h : 2 
    # i : 1 
    # t : 1
    temp_var =
i=@
while i < len(name):
if name[i] not in temp_var:

temp_var += name[i]

print(#"{name[i]} : {name.count(name[i])}")
i += 1
    
    
    





