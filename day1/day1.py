def get_value(line: str) -> tuple:
    nums = '1234567890'
    nums_in_line = list(filter(lambda char: char in nums, line))
    return nums_in_line[0] + nums_in_line[-1]



def main():
    calibration_sum = 0

    with open('day1.txt') as f:
        for line in f.readlines():
            calibration_sum += int(get_value(line))
    
    print(calibration_sum)
        


if __name__ == '__main__':
    main()