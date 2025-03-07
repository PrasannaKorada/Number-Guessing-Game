# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:51:22 2025

@author: GOWRI
"""
# python number guessing game
import random
low_num = int(input("enter the lowest num:"))
high_num=int(input("enter the high num:"))
answer = random.randint(low_num,high_num)
guesses =0
is_running =True

print("Python Number Guessing Game")
print(f"select a number b/w {low_num} and {high_num}")

while is_running:
    guess = input("enter your guess:")
    
    if guess.isdigit():
        guess=int(guess)
        guesses +=1
        if guess< low_num or guess>high_num:
            print("this is out of bound")
            print(f"plzz select a number b/w {low_num} and {high_num}")
        elif guess <answer:
            print("too low..try again..!")
        elif guess >answer:
            print("too high..try again..!")   
        else:
            print(f"CORRECT..! The answer was {answer}")
            print(f"Number of guesses:{guesses}")
            is_running =False
                
    else:
        print("invalid guess")
        print(f" plzz select a number b/w {low_num} and {high_num}")
        
        
        