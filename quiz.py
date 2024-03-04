"""
File: quiz.py
Author: Lorenzo Rivera
Date: 2024-03-04
Description: Legend of Zelda-themed quiz game with score tracker.
"""

print("------------------------------")
print("Multiple-Choice Quiz Game\n")
point_tracker = 0

#First question
print("\nWhich is NOT one of the names of the Master Sword?\n")
print("(a) The Blade of Evil's Bane")
print("(b) The Sword that Seals the Darkness")
print("(c) Excalibur")

#Determines correct answer of first question
question_one = input("> ")
if question_one == "a":
    print("Correct!")
    point_tracker = point_tracker + 1
else:
    print("Incorrect.")

#Second question
print("\nWho is Zelda's chosen hero?\n")
print("(a) Link")
print("(b) Ganon")
print("(c) Tingle")

#Determines correct answer of second question
question_two = input("> ")
if question_two == "a":
    print("Correct!")
    point_tracker = point_tracker + 1
else:
    print("Incorrect.")

#Third question
print("\nWhat is the latest installment in the series?")
print("(a) Skyward Sword")
print("(b) Tears of the Kingdom")
print("(c) Breath of the Wild")

#Determines correct answer of third question
question_three = input("> ")
if question_three == "a":
    print("Correct!")
    point_tracker = point_tracker + 1
else:
    print("Incorrect.")

#Results of quiz
final_percent = round(point_tracker / 3, 1)
print("\nQuiz complete!")
print("You answered " + str(point_tracker) + " out of 3 correctly. Your score is " + str(final_percent))