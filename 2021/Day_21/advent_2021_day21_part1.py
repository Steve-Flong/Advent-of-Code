from typing import List, Dict, Tuple

def main():
    play1_pos = 6
    play2_pos = 7
    play1_total = 0
    play2_total = 0
    dice = 0
    rolls = 0
    while True:
        dice_move, dice = roll_dice(dice)
        play1_pos = (play1_pos + dice_move - 1) % 10 + 1
        play1_total += play1_pos
        rolls += 3
        if play1_total >= 1000:
            result = play2_total * rolls
            print(result)
            break
        dice_move, dice = roll_dice(dice)
        play2_pos = (play2_pos + dice_move - 1) % 10 + 1
        play2_total += play2_pos
        rolls += 3
        if play2_total >= 1000:
            result = play1_total * rolls
            print(result)
            break


def roll_dice(dice):
    total = 0
    for x in range(3):
        dice += 1 if dice < 100 else 1
        total += dice
    return total, dice

if __name__ == "__main__":
    main()
    