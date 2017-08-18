##actions = {
##    ["Do Good": "Hold the door open for someone today."],
##    ["Say Good": "Give someone a compliment."],
##    ["Eat Good": "Eat serving of at least two veggies today"],
##    ["Hear Good": "Listen or read a positive message today."],
##    }


##exercise_good = {
##    ["


import random


response_1 = {"Do Good": "Hold the door open for someone today."}
response_2 = {"Say Good": "Give someone a compliment."}
response_3 = {"Eat Good": "Eat a serving of at least two veggies today"}
response_4 = {"Hear Good": "Listen or read a positive message today."}
response_5 = {"Exercise_0": "Get your body moving. Whatever you are able to do just get moving! From jumping jacks to yard work. Whatever you decide, Exercising can help offset depression, anxiety, and stress."}


exercise = [response_5]
social = [response_1, response_2]
nutrition = [response_3]


def speak_exercise():
    for value, value in response_5.items():
        print(value)

def speak_social():
    for response in social:
        print(response)

def speak_nutrition():
    for value, value in response_3.items():
        print(value)


# Local test at calling the response
speak_exercise()

print("\n")

speak_nutrition()




