def get_top_totals(amount = 1):
    input_raw = open("Day01/day_01_input.txt", "r")
    input_data = input_raw.read().splitlines()

    calorie_totals = []

    # Calculate totals
    curr_total = 0
    prev_total = 0
    for calories in input_data:
        if calories != "":
            curr_total += int(calories)
        else:
            calorie_totals.append(curr_total)
            curr_total = 0

    calorie_totals.sort()
    calorie_totals.reverse()

    top_three_total = 0
    for i in range(amount):
        top_three_total += calorie_totals[i]
    return top_three_total