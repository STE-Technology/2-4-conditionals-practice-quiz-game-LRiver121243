"""
File: quiz.py
Author: Lorenzo Rivera
Date: 2024-03-04
Description: Legend of Zelda-themed quiz game with score tracker.
"""

print("-------------------------------------------------------")
print("Multiple-Choice Quiz Game\n")
point_tracker = 0

#First question
print("\nWhich is NOT one of the names of the Master Sword? \
    \n(a) The Blade of Evil's Bane \
    \n(b) The Sword that Seals the Darkness \
    \n(c) Excalibur\n")

#Determines correct answer of first question
user_answer = input("> ")
if user_answer == "c" or user_answer == "C":
    print("Correct!")
    point_tracker += 1
else:
    print("Incorrect.")

#Second question
print("\nWho is Princess Zelda's chosen hero? \
    \n(a) Link \
    \n(b) Ganon \
    \n(c) Tingle\n")

#Determines correct answer of second question
user_answer = input("> ")
if user_answer == "a" or user_answer == "A":
    print("Correct!")
    point_tracker += 1
else:
    print("Incorrect.")

#Third question
print("\nWhat is the latest installment in the Legend of Zelda series? \
    \n(a) Skyward Sword \
    \n(b) Tears of the Kingdom \
    \n(c) Breath of the Wild\n")

#Determines correct answer of third question
user_answer = input("> ")
if user_answer == "b" or user_answer == "B":
    print("Correct!")
    point_tracker += 1
else:
    print("Incorrect.")

#Fourth question
print("\nWho is the spirit that resides within the Master Sword? \
    \n(a) Fi \
    \n(b) Impa \
    \n(c) King Rhoam Bosphoromous Hyrule\n")

#Determines correct answer of forth question
user_answer = input("> ")
if user_answer == "a" or user_answer == "A":
    print("Correct!")
    point_tracker += 1
else:
    print("Incorrect.")

#Results of quiz
final_percent = point_tracker / 4 * 100
print("\nQuiz complete!")
print("You answered " \
    + str(point_tracker) \
    + " out of 4 correctly. Your score is " \
    + str(final_percent) + "%")
print("-------------------------------------------------------")