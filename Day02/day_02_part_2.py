from enum import Enum

input_raw = open("Day02/day_02_input.txt", "r")
input_data = input_raw.read().splitlines()

Hand = Enum("Hand", ['ROCK', 'PAPER', 'SCISSORS'])
class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def letter_to_result(letter):
    if letter == "X":
        return Result.LOSE
    if letter == "Y":
        return Result.DRAW
    if letter == "Z":
        return Result.WIN

def letter_to_hand(letter):
    if letter == "A":
        return Hand.ROCK
    if letter == "B":
        return Hand.PAPER
    if letter == "C":
        return Hand.SCISSORS

def get_desired_hand(result, opponent):
    if result == Result.DRAW:
        return opponent

    match result:
        case Result.LOSE:
            match opponent:
                case Hand.ROCK:
                    return Hand.SCISSORS
                case Hand.PAPER:
                    return Hand.ROCK
                case Hand.SCISSORS:
                    return Hand.PAPER
        case Result.WIN:
            match opponent:
                case Hand.ROCK:
                    return Hand.PAPER
                case Hand.PAPER:
                    return Hand.SCISSORS
                case Hand.SCISSORS:
                    return Hand.ROCK

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
    result = letter_to_result(round[1])
    player_hand = get_desired_hand(result, opponent)

    round_points = check_hands(player_hand, opponent)

    return round_points.value + player_hand.value

# Play RPS
total_score = 0
for round in input_data:
    total_score += play_round(round)
print("Total: " + str(total_score))