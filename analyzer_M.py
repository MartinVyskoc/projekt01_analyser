"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Vyskocil

email: vyskoc68@gmail.com

discord: Petr Svetr#4490ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ
"""
import re

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

#name = input("zadej jmeno: ")
#pass_u = input("zadej heslo: ")
name = "bob"
pass_u = "123"
# # print(f"username:{name}")
# # print(f"password:{pass_u}")

if check_login(name, pass_u):
    print(line)
    print(f"Welcome to the app, {name}")
else:
    print("unregistered user, terminating the program.")

print("We have 3 texts to be analyzed.")
print(line)
#choice_text = int(input("Enter a number btw. 1 and 3 to select: "))
choice_text = 4 - 1
anal_text = (task_template.TEXTS[choice_text])
anal_text = anal_text.replace(".", "")
print(anal_text)
print(f"počet slov: {word_count(anal_text)}")
print(f"velké pismeno: {count_titlecase_words(anal_text)}")
print(f"velká pismena: {count_uppercase_words(anal_text)}")
print(f"malá pismena: {count_lowercase_words(anal_text)}")
result1, result2 = count_numbers_words(anal_text)
print(f"cisla: {result1}")
print(f"součet {result2}")
print("KONEC * KONEC")