from enum import Enum

input_raw = open("Day02/day_02_input.txt", "r")
input_data = input_raw.read().splitlines()

Hand = Enum("Hand", ['ROCK', 'PAPER', 'SCISSORS'])
class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def letter_to_hand(letter):
    if letter == "A" or letter == "X":
        return Hand.ROCK
    if letter == "B" or letter == "Y":
        return Hand.PAPER
    if letter == "C" or letter == "Z":
        return Hand.SCISSORS

def check_hands(playerA, playerB):
    if playerA == playerB:
        return Result.DRAW

    match playerB:
        case Hand.ROCK:
            if playerA == Hand.PAPER:
                    return Result.WIN
            elif playerA == Hand.SCISSORS:
                    return Result.LOSE
        case Hand.PAPER:
            if playerA == Hand.SCISSORS:
                    return Result.WIN
            elif playerA == Hand.ROCK:
                    return Result.LOSE
        case Hand.SCISSORS:
            if playerA == Hand.ROCK:
                    return Result.WIN
            elif playerA == Hand.PAPER:
                    return Result.LOSE

def play_round(round):
    round = round.split(" ")

    opponent = letter_to_hand(round[0])
    player = letter_to_hand(round[1])

    
    hand_points = player.value
    round_points = check_hands(player, opponent).value

    return hand_points + round_points

# Play RPS
total_score = 0
for round in input_data:
    total_score += play_round(round)
print("Total: " + str(total_score))