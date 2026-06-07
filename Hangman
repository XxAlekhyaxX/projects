import random 
import time 
import os 
hangman_stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

hangman_data = [
    {"category": "Animal", "number_of_letters": 4, "answer": "lion"},
    {"category": "Fruit", "number_of_letters": 5, "answer": "apple"},
    {"category": "Country", "number_of_letters": 5, "answer": "india"},
    {"category": "Bird", "number_of_letters": 6, "answer": "parrot"},
    {"category": "Vehicle", "number_of_letters": 3, "answer": "bus"},
    {"category": "Color", "number_of_letters": 4, "answer": "blue"},
    {"category": "Flower", "number_of_letters": 4, "answer": "rose"},
    {"category": "Animal", "number_of_letters": 7, "answer": "giraffe"},
    {"category": "Fruit", "number_of_letters": 6, "answer": "banana"},
    {"category": "Country", "number_of_letters": 6, "answer": "brazil"},
    {"category": "Bird", "number_of_letters": 5, "answer": "eagle"},
    {"category": "Vehicle", "number_of_letters": 3, "answer": "car"},
    {"category": "Color", "number_of_letters": 6, "answer": "yellow"},
    {"category": "Flower", "number_of_letters": 5, "answer": "lotus"},
    {"category": "Animal", "number_of_letters": 5, "answer": "tiger"},
    {"category": "Fruit", "number_of_letters": 5, "answer": "mango"},
    {"category": "Country", "number_of_letters": 4, "answer": "peru"},
    {"category": "Bird", "number_of_letters": 4, "answer": "crow"},
    {"category": "Vehicle", "number_of_letters": 5, "answer": "truck"},
    {"category": "Color", "number_of_letters": 5, "answer": "green"}
]

word = random.choice(hangman_data)

number = word["number_of_letters"]
blank = [] 
hangman = ["head","body","left hand","right hand","left leg","right leg"]

for i in range(number):
    blank.append("_")
letter_count = 1
miss_count = 0 
while True: 
    print("Hangman:")
    print("Word:"," ".join(blank)) # join is used to join all the items in a list using a string 
    print(f"Hint: {word["category"]}")
    
    letter = input(f"Enter letter- {letter_count}:")
    time.sleep(3)
    
    if letter == word["answer"][letter_count-1]:
        print("You're correct.")
        blank[letter_count-1] = letter 
        letter_count += 1 
        if letter_count > number:
            print("hangman is alive:")
            print(hangman_stages[0])
            print("game end")
            break 
    else:
        print("You're wrong, Try again")
        miss_count += 1 
        part = hangman[miss_count-1]
        print(f"{part} is drawn:")
        print(hangman_stages[miss_count])
        
        if miss_count == 6:
            print("hangman is dead")
            print(f"Answer: {word["answer"]}")
            break 
    # after the decision has made for a single character 
    time.sleep(3)
    os.system("clear")








