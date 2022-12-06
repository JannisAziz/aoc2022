input_raw = open("Day03/day_03_input.txt", "r")
rucksacks = input_data = input_raw.read().splitlines()

import string
letters = string.ascii_lowercase+string.ascii_uppercase

def letter_to_int(letter):
    return letters.index(letter) + 1

total = 0
for rucksack in rucksacks:
    # if len(rucksack) % 2 != 0:
    #     print("Error: Uneven distribution found!")
    #     break

    compartementOne = rucksack[slice(0, len(rucksack)//2)]
    compartementTwo = rucksack[slice(len(rucksack)//2, len(rucksack))]
    #print(compartementOne, compartementTwo)

    for letter in compartementOne:
        if compartementTwo.__contains__(letter):
            #print("Duplicate found!: " + letter)
            total += letter_to_int(letter)
            break

#print(total)

group_size = 3
rucksack_groups = [rucksacks[i:i+group_size] for i in range(0, len(rucksacks), group_size)]

total = 0
for group in rucksack_groups:
    for letter in group[0]:
        if group[1].__contains__(letter) and group[2].__contains__(letter):
            total += letter_to_int(letter)
            break

print(total)