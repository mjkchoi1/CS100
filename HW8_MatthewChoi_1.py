#Problem 1

def twoWords(length, firstLetter):
    lst = []
    while True:
        x=input("Enter a "+ str(length) + "-letter word please: ")
        if length == len(x):
            lst.append(x)
            break
    while True:
        y=input("Enter a word beginning with " + firstLetter + ' please: ')
        if y[0] == firstLetter.upper() or y[0] == firstLetter.lower():
            lst.append(y)
            break
    print(lst)

#Problem 2
def twoWordsV2(length, firstLetter):
    lst = []
    x=input("Enter a "+ str(length) + "-letter word please: ")
    while length != len(x):
        x=input("Enter a "+ str(length) + "-letter word please: ")
    lst.append(x)
    y=input("Enter a word beginning with " + firstLetter + ' please: ')
    while y[0] != firstLetter.upper() and y[0] != firstLetter.lower():
        y=input("Enter a word beginning with " + firstLetter + ' please: ')
    lst.append(y)
    print(lst)

#Problem 3
def enterNewPassword():
    password = input("Enter password: ")
    length = False
    integer = False
    if len(password)>=8 and len(password)<=15:
        length = True
    for x in password:
        if x.isdigit():
            integer = True
    if length==False and integer==False:
        print("Password needs to be 8 ~ 15 characters with integers")
        
    elif length==False and integer==True:
        print("Password too short")
        
    elif length==True and integer==False:
        print("Please put in an integer")

    else:
        print("Password is valid")

#Problem 4
import random

import random

def GuessNumber():
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    num = random.randint(1,50)
    count = 1
    print("Guess ", count)
    userGuesses = int(input("? "))
    
    while num != userGuesses:
        if (count == 5 or userGuesses == num):
            print("You used all of your chances. The number is ", num)
            break
        if userGuesses < num:
            print('Higher than ', userGuesses)
            count += 1
            print("Guess ",count)
            userGuesses = int(input("? "))
        elif userGuesses > num:
            print('Lower than ', userGuesses)
            count += 1
            print("Guess ", count)
            userGuesses = int(input("? "))
        else:
            print("You are right! I was thinking of ", num, ' !')
            break


          

        
