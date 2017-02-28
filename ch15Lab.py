'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


file = open("dictionary.txt", "r")
dictionary_list = []
for line in file:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word.strip())
print(dictionary_list)
file.close()

file = open("AliceInWonderland200.txt", "r")
line_numb = 0

for line in file:
    line_numb += 1
    words = split_line(line)
    for word in words:
        for i in range(len(dictionary_list)):
            if word.upper() == dictionary_list[i].upper():
                break;
        else:
            print(word, "on line", line_numb, "is a possible misspelling")

file.close()

file2 = open("AliceInWonderLand200.txt")
line_numb2 = 0
upper_bound = len(dictionary_list) - 1
lower_bound = 0
found = False
for line in file2:
    line_numb2 += 1
    words = split_line(line)
    for word in words:
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2

            if dictionary_list[middle_position].upper() < word.upper():
                lower_bound = middle_position + 1
            elif dictionary_list[middle_position].upper() > word.upper():
                upper_bound = middle_position - 1
            else:
                found = True

        if not found:
            print(word, "on line", line_numb2, "is a possible misspelling")
        found = False
        upper_bound = len(dictionary_list) - 1
        lower_bound = 0
file2.close()
