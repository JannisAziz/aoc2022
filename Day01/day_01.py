input_raw = open("day_01_input.txt", "r")
input_data = input_raw.read().splitlines()

calorie_totals = []

# Calculate totals
curr_total = 0
prev_total = 0
for calories in input_data:
    if calories != "":
        curr_total += int(calories)
    else:
        calorie_totals.insert(len(calorie_totals), curr_total) #.append(curr_total)
        curr_total = 0




# simple sort & reverse
calorie_totals.sort()
calorie_totals.reverse()

top_one_total = calorie_totals[0]
print(top_one_total)

top_three_total = 0
for i in range(3):
    top_three_total += calorie_totals[i]

print(top_three_total)