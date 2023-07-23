from data import task_template

choice_text = 2
anal_text = (task_template.TEXTS[choice_text])
anal_text = anal_text.replace(".", " ").replace(",", " ")
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
    