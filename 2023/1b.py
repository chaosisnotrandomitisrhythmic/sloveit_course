"""
# Day 1: Trebuchet?!

## Part B

Your calculation isn't quite right. It looks like some of the digits are actually 
spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
also count as valid "digits".

For example:
In this example, the calibration values are:
- two1nine -> 29
- eightwothree -> 83
- abcone2threexyz -> 13
- xtwone3four -> 24
- 4nineeightseven2 -> 42
- zoneight234 -> 14
- 7pqrstsixteen -> 76

Adding these together produces 281.
"""

from aocd import get_data, submit

def get_number(text):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    numbers = []

    for i in range(len(text)):
        # solve the single digit case
        if text[i].isdigit():
            numbers.append(text[i])
        # solve the spelled out case
        for word, digit in number_map.items():
            if text[i:].startswith(word):
                numbers.append(digit)
    
    return int(numbers[0] + numbers[-1])

def find_solution(lines):
    return sum(get_number(x) for x in lines)

def main():
    # Get data
    data = get_data(day=1, year=2023).split('\n')
    
    # Calculate solution
    answer = find_solution(data)
    print(answer)
    
    # # Submit answer
    # submit(answer, part="b", day=1, year=2023)

if __name__ == "__main__":
    main()

