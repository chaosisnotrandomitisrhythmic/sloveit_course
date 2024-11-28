"""
# Day 1: Trebuchet?!

## Part A

The newly-improved calibration document consists of lines of text; each line 
originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and 
the last digit (in that order) to form a single two-digit number.

For example:
p1abc2 
qr3stu8vwx 
a1b2c3d4e5f 
treb7uchet

In this example, the calibration values of these four lines are:
- The first line's value is 12
- The second line's value is 38
- The third line's value is 15
- The fourth line's value is 77
Adding these together produces 142.
"""

from aocd import get_data, submit

def find_digits(text):
    numbers = [char for char in text if char.isdigit()]
    return int(numbers[0] + numbers[-1])

def find_solution(lines):
    return sum(find_digits(x) for x in lines)

def main():
    # Get data
    data = get_data(day=1, year=2023).split('\n')
    
    # Calculate solution
    answer = find_solution(data)
    print(answer)
    
    # Submit answer
    # submit(answer, part="a", day=1, year=2023)

if __name__ == "__main__":
    main()


