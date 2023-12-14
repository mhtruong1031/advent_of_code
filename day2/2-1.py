import re

def is_valid_game(line: str) -> bool:
    colors      = ['red', 'green', 'blue']
    color_max   = [12, 13, 14]
    rolls       = re.split('; |, ', line[line.index(":")+2:])

    for roll in rolls:
        for idx, color in enumerate(colors):
            if color in roll and color_max[idx] < int(roll[:roll.index(' ')]):
                return False
    
    return True


def main() -> None:
    id_sum = 0

    with open('game_data.txt') as f:
        for line in f.readlines():
            if is_valid_game(line):
                id_sum += int(line[5:line.index(":")])

    print(id_sum)


if __name__ == '__main__':
    main()