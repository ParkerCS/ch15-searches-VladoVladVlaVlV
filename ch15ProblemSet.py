'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
file = open("dictionary.txt", "r")
word_list = []
second_list = []
for line in file:
    word_list.append(line.strip())  # use line.strip to take off empty spaces
print(word_list)
a = 0
e = 0
for i in range(len(word_list)):
    if len(word_list[i]) > len(word_list[i - 1]):
        if len(word_list[i]) > len(word_list[a]):
            a = i
        elif len(word_list[i]) == len(word_list[a]):
            e = i
            second_list.append(word_list[e])

print(word_list[a])
for i in range(len(second_list)):
    if len(second_list[i]) == len(word_list[a]):
        print(word_list[i])
file.close()

# 2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
file = open("AliceInWonderland.txt", "r")
average_length_list = []
brojka = 0
for line in file:
    words = split_line(line)
    for word in words:
        average_length_list.append(word.strip())
print(average_length_list)
for i in range(len(average_length_list)):
    brojka += len(average_length_list[i])
print(round(brojka / len(average_length_list), 4))
file.close()

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

# 3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

# 3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"
file = open("AliceInWonderland.txt", "r")
list_x = []
brojka = 0
for line in file:
    words = split_line(line)
    for word in words:
        list_x.append(word.strip())

list_y = []
for i in range(len(list_x)):
    if len(list_x[i]) == 7:
        list_y.append(list_x[i])

for i in range(len(list_y)):
    for j in range(i + 1, len(list_y)):

        if str(list_y[i]).upper() == str(list_y[j]).upper():
            list_y[i] = 0

list_z = []
for i in range(len(list_y)):
    if list_y[i] != 0:
        list_z.append(list_y[i])

list_g = []
for i in range(len(list_z)):
    list_g.append(0)

''''''
for i in range(len(list_x)):
    for j in range(len(list_z)):
        if str(list_x[i]).upper() == str(list_z[j]).upper():
            list_g[j] += 1

print(list_z)

var = max(list_g)
print(var)
for i in range(len(list_g)):
    if list_g[i] == var:
        var = i
print("The most occuring 7 letter word is:", list_z[var])

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.
