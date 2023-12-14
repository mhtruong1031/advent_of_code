import re

def get_power(line: str) -> int:
    colors      = ['red', 'green', 'blue']
    color_max   = [0, 0, 0]
    rolls       = re.split('; |, ', line[line.index(":")+2:])

    for roll in rolls:
        for idx, color in enumerate(colors):
            if color in roll and int(roll[:roll.index(' ')]) > color_max[idx]:
                color_max[idx] = int(roll[:roll.index(' ')])
    
    return color_max[0]*color_max[1]*color_max[2]


def main() -> None:
    power_sum = 0

    with open('game_data.txt') as f:
        for line in f.readlines():
            power_sum += get_power(line)

    print(power_sum)


if __name__ == '__main__':
    main()