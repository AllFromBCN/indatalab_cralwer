#This program shows the most frequently mentioned words
#Designed by Soo Min, JEONG

from collections import Counter

temp_str = []
filename = input("Enter the file name including .txt: ")

try:
    with open(filename, "r", -1, "UTF-8") as input:
        for line in input:
            line = line.rstrip()
            line.replace('- dc App', '').replace('- dc official App','')
            line = line.split('\t')[1]
            temp_str = temp_str + line.split(' ')
        c = Counter(temp_str)

        print()


finally:
    input.close()

