from typing import List, Dict, Tuple


def main():
    play1_pos = 6
    play2_pos = 7
    play1_total = 0
    play2_total = 0
    dice = 0
    play1_wins = 0
    play2_wins = 0
    while play1_total < 21 and play2_total < 21:
        dice_move, dice = roll_dice(dice)
        play1_pos = (play1_pos + dice_move) % 10
        if play1_pos == 0:
            play1_pos = 10
        play1_total += play1_pos
        if play1_total >= 21:
            play1_wins += 1
            break
        dice_move, dice = roll_dice(dice)
        play2_pos = (play2_pos + dice_move) % 10
        if play2_pos == 0:
            play2_pos = 10
        play2_total += play2_pos
        if play2_total >= 21:
            play2_wins += 1
            break


def roll_dice(dice):
    total = 0
    for x in range(3):
        if dice < 100:
            dice += 1
        else:
            dice = 1
        total += dice
    return total, dice

if __name__ == "__main__":
    main()
    