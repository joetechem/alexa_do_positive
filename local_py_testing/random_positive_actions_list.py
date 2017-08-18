"""A list of positive actions."""

# importing the random module
import random

ANODE_ACTIONS = [
    "Hold the door open for someone today.",
    "Give someone a compliment.",
    "Get your body moving. Whatever you are able to do just get moving! From jumping jacks to yard work. Whatever you decide, Exercising can help offset depression, anxiety, and stress.",
    "Listen or read a positive message, or has uplifting content. The variety of subject matter, the better.",
    "Eat a serving of at least two veggies today",
    "Think about how a person has helped you in some way. This could either be a friend, family member, colleague, teacher, or even a pet. And go ahead and thank them. This can go a long way in making another feel good.",
    "Take a cold shower. Yes. Cold. Studies show, taking a cold shower can increase oxygen intake, alertness, and overall physical and mental wellness. One study showed, routine showers can help treat symptoms of depression. Go ahead. Jump in!",
    "Think about your life goals. Do this not only after listening to my speech output, but everyday. Just like practice, if you follow a simple pattern, you can achieve what you want.",
    "Complete the most important thing on your to do list.",
    "Stretch. Take a moment to stretch. Hold that stretch for at least thirty seconds. This will increase blood flow and oxygen intake. Which are good things. I would stretch myself, but alas. I am only hardware and software.",
    "Take a deep breath. Hold it for ten seconds. Then exhale for twice the amount you inhaled."
    ]

# testing pulling a random item from list.
#print(random.choice(ANODE_ACTIONS))

# dictionary
ANODE_ACTIONS2 = {
    "Hold the door open for someone today.": "Hold the door open for someone today.",
    "Give someone a compliment.": "Give someone a compliment.",
    "Get your body moving. Do some form of exercise!": "Get your body moving. Whatever you are able to do just get moving! From jumping jacks to yard work. Whatever you decide, Exercising can help offset depression, anxiety, and stress.",
    "Listen to or read a positive or uplifting message": "Listen or read a positive message, or has uplifting content. The variety of subject matter, the better.",
    "Eat some veggies today!": "Eat a serving of at least two veggies today",
    "Thank a person that has helped you.": "Think about how a person has helped you in some way. This could either be a friend, family member, colleague, teacher, or even a pet. And go ahead and thank them. This can go a long way in making another feel good.",
    "Take a cold shower!": "Take a cold shower. Yes. Cold. Studies show, taking a cold shower can increase oxygen intake, alertness, and overall physical and mental wellness. One study showed, routine showers can help treat symptoms of depression. Go ahead. Jump in!",
    "Think about your life goals today, and everyday. Practice in thought, makes perfect.":"Think about your life goals. Do this not only after listening to my speech output, but everyday. Just like practice, if you follow a simple pattern, you can achieve what you want.",
    "Complete the most important thing on your to-do list.": "Complete the most important thing on your to do list.",
    "Stretch! Hold your stretch for 30 seconds!": "Stretch. Take a moment to stretch. Hold that stretch for at least thirty seconds. This will increase blood flow and oxygen intake. Which are good things. I would stretch myself, but alas. I am only hardware and software.",
    "Take a deep breath. Exhale for twice as long as it took you to inhale your breath.": "Take a deep breath. Hold it for ten seconds. Then exhale for twice the amount you inhaled."
    }

speech_key = random.choice(ANODE_ACTIONS2.values())

speech_to_card = [speech_key]
card_key = speech_to_card[0]


print("\nSPEECH_OUTPUT: " + speech_key)

print("\nCARD OUTPUT: " + card_key)
##print(random.choice(ANODE_ACTIONS2.keys()))
##for key, value in ANODE_ACTIONS2.items():
##    print(key)
##    print(value)
