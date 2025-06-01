# # Lesson 1: print
# name = input("What is your name")
# print("Nice to meet you, "+ name+"!")

# age= input("How old are you")
# print("You are "+age+" years old")

# city = input("Where are you from?")
# print("You are from "+city+"!")

# Mini excercise
#1
# color = input("What is your favority color?")
# print("Your favority color is "+color+"!")

# #2
# name = input("What is your name")
# print("Your name is "+ name+".")

# #3
# job = input("what is your job")
# print("Your job is "+job)

# #4
# question = input("A que le tienes miedo")
# print("Le tienes miedo a "+question)

# English Vocabulary Quiz Game

# A dictionary of English words and their meanings
# vocab = {
#     "apple": "a fruit that is red or green and round",
#     "run": "to move fast with your feet",
#     "book": "a set of written pages",
#     "happy": "feeling good or joyful",
#     "water": "a clear liquid that we drink"
# }

# print("Welcome to the English Vocabulary Quiz!")
# print("Type the correct word for each meaning.\n")

# score = 0

# # Ask each meaning
# for word, meaning in vocab.items():
#     answer = input(f"What word means: '{meaning}'? ").strip().lower()
#     if answer == word:
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Wrong! The correct word was '{word}'.\n")

# print(f"You got {score} out of {len(vocab)} correct.")


# English-Spanish Flashcard Game 🎓🇬🇧🇪🇸

import random

# English-Spanish word pairs
word_list = [
    ("apple", "manzana"),
    ("house", "casa"),
    ("cat", "gato"),
    ("water", "agua"),
    ("friend", "amigo"),
    ("school", "escuela"),
    ("car", "coche"),
    ("book", "libro"),
    ("love", "amor"),
    ("hello", "hola")
]

# Shuffle the word list
random.shuffle(word_list)

score = 0
total = len(word_list)

print("🎉 Welcome to the English from Spanish Flashcard Game! 🎉")
print("Translate the Spanish word into English.\n")

# Game loop
for eng, spa in word_list:
    answer = input(f"What is the English word for '{spa}'? ").strip().lower()
    if answer == eng:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is '{eng}'.\n")

# Final score
print(f"🏁 You got {score}/{total} correct! 🏆")
if score == total:
    print("🎊 Perfect score! You’re a language master!")
elif score > total / 2:
    print("💪 Great job! Keep practicing!")
else:
    print("📘 Keep learning! You’ll get better every day!")
