"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Vyskocil

email: vyskoc68@gmail.com

discord: Petr Svetr#4490ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ
"""
import sys

from data import task_template

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

line = 20 * "--"

def check_login(name, password):
    if name in users:
        if password == users[name]:
            return True
        else:
            return False
    else:
        return False

def word_count(text):
    words = text.split()
    return len(words)

def count_titlecase_words(text):
    capitalized_words = 0
    for word in text.split():
        if word[0].isupper() and word[1:].islower():
            capitalized_words += 1
    return capitalized_words

def count_uppercase_words(text):
    uppercase_words = 0
    for word in text.split():
        if word.isupper():
            uppercase_words += 1
    return uppercase_words

def count_lowercase_words(text):
    lowercase_words = 0
    for word in text.split():
        if word.islower():
            lowercase_words += 1
    return lowercase_words

def count_numbers_words(text):
    numbers_words = 0
    numbers_sum = 0
    for word in text.split():
        if word.isdigit():
            numbers_words += 1
            numbers_sum = numbers_sum + int(word)
    return numbers_words, numbers_sum

name = input("zadej jmeno: ")
pass_u = input("zadej heslo: ")

if check_login(name, pass_u):
    print(line)
    print(f"Welcome to the app, {name}")
else:
    print("unregistered user, terminating the program.")
    sys.exit()

print("We have 3 texts to be analyzed.")
print(line)
choice_text = input("Enter a number btw. 1 and 3 to select: ")
if choice_text.isdigit():
    choice_text = int(choice_text) - 1
    if choice_text < 0 or choice_text > 2:
        print("Your choice is out of range")
        print(line)
        sys.exit()
else:
    print("Your choice is not number")
    print(line)
    sys.exit()
#choice_text = int(choice_text)
print(line)

anal_text = (task_template.TEXTS[choice_text])
anal_text = anal_text.replace(".", "").replace(",", "")
print(anal_text)
print(f"počet slov: {word_count(anal_text)}")
print(f"velké pismeno: {count_titlecase_words(anal_text)}")
print(f"velká pismena: {count_uppercase_words(anal_text)}")
print(f"malá pismena: {count_lowercase_words(anal_text)}")
result1, result2 = count_numbers_words(anal_text)
print(f"cisla: {result1}")
print(f"součet {result2}")

longest_word_length = 0

for word in anal_text.split():
    if len(word) > longest_word_length:
        longest_word_length = len(word)

dictionary = {}

for i in range(1, longest_word_length + 1):
    dictionary[i] = 0

max_star = 0
for word in anal_text.split():
    dictionary[len(word)] += 1
    if dictionary[len(word)] > max_star:
        max_star = dictionary[len(word)]

print("-" * 22)
print(" LEN|", "OCCURENCES".center(max_star), "|NR.")
print("-" * 22)

for key, value_p in dictionary.items():
    key2 = str(key)
    len_p = key2.rjust(3)
    star1 = str("*" * value_p)
    star2 = star1.ljust(max_star)
    print(len_p, "|", star2, "|", value_p)

print("KONEC * KONEC")