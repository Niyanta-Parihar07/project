# Number guessing game 

import random

def guess_the_number() : 
    
    secret_number = random.randint(1,100) # The number is randomly chosen by the computer.

    attempts=0            
    maximum_attempt=5
    
    print("You have a maximum of 5 attempts ")
    print("Wish you all the best 🤞")                                       
    print("Reminder 🔔: Enter numbers only (alphabets are not allowed).")
    print("Your game starts now 🥳🎉")
    
    while attempts < maximum_attempt:   
        try:
            guess = int(input("Enter the number between 1 and 100 : ")) # Here you will guess number between 1 to 100 . 
        except ValueError:
            print("Invalid input! Please enter a number only .")
            continue    
        
        
        # You have to guess right number then you will win the game.
        
        attempts +=1  
        
        if(guess==secret_number):
            print("Hurray!! You won the game 🎉")
            break 
        elif(guess > secret_number):
            print("Your entered value is greater than the right answer")
        elif(guess < secret_number):
            print("Your entered value is lesser than the right answer")
            
#This runs only if loop ended without break (i.e user failed)

        if attempts == maximum_attempt and guess != secret_number:
            print("Game over ❌ . Better luck next time!") 
            print("The correct number was:", secret_number)     
            
guess_the_number()            
