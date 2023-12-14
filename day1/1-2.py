def get_value(line: str) -> tuple:
    nums         = '1234567890'
    nums_in_line = []
    num_text = {
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9',
        'zero' : '0'
    }

    for idx, char in enumerate(line):
        if char in nums:
            nums_in_line.append(char)
        else:
            for key, value in num_text.items():
                if line[idx: idx+len(key)] == key:
                    nums_in_line.append(value)

    return nums_in_line[0] + nums_in_line[-1]

def main():
    calibration_sum = 0

    with open('callibration_lines.txt') as f:
        for line in f.readlines():
            calibration_sum += int(get_value(line))
    
    print(calibration_sum)
        
if __name__ == '__main__':
    main()