from enum import Enum

input_raw = open("Day02/day_02_input.txt", "r")
input_data = input_raw.read().splitlines()


test_data = ["A Y", "B X", "C Z"]

def letter_to_hand(letter):
    if letter == "A" or letter == "X":
        return Hand.ROCK
    if letter == "B" or letter == "Y":
        return Hand.PAPER
    if letter == "C" or letter == "Z":
        return Hand.SCISSORS

class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    LOSE = 0 # 0 points
    DRAW = 3 # 3 points
    WIN = 6 # 6 points


def play_round(round):
    round = round.split(" ")
    print(round)

    opponent = letter_to_hand(round[0])
    player = letter_to_hand(round[1])

    print (opponent)
    print (player)

    def check_win():
        if player == opponent:
            return Result.DRAW

        match player:
            case Hand.ROCK:
                match opponent:
                    case Hand.SCISSORS:
                        return Result.WIN
                    case Hand.PAPER:
                        return Result.LOSE
            case Hand.PAPER:
                match opponent:
                    case Hand.ROCK:
                        return Result.WIN
                    case Hand.SCISSORS:
                        return Result.LOSE
            case Hand.SCISSORS:
                match opponent:
                    case Hand.PAPER:
                        return Result.WIN
                    case Hand.ROCK:
                        return Result.LOSE

    hand_points = player.value
    round_points = check_win().value

    return hand_points + round_points

# Play Rock Paper Scissors
#
# Rules:
# Rock < Paper < Scissors < Rock
# A < B < C < A
# X < Y < Z < X
def play_RPS(data):
    score = 0
    for i, round in enumerate(data):
        result = play_round(round)
        score += result
        print("Round " + str(i+1) + " - " + str(result))
    return score

total_score = play_RPS(input_data)
print("Total: " + str(total_score))