"""calc.py: A simple Python calculator."""

import sys

def add_all(nums):
    return sum(nums)

def multiply_all(nums):
    return reduce(lambda a, b:a * b, nums)

if __name__ == '__main__':
    command = sys.argv[1]
    nums = map(float, sys.argv[2:])
    if command == 'add':
        print(add_all(nums))
    elif command =='multiply':
        print(multiply_all(nums))
    elif command =='min':
        print(min(nums))
    elif command =='max':
        print(max(nums))
    elif command == 'sum3':
        print(add_all(nums) + 3)
    elif command == 'sub6':
        print(add_all(nums) - 6)
    else:
        usage="calc.py incorrect bla 222"
        print(usage)
