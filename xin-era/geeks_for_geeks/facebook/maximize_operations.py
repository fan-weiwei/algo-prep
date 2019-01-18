"""
Given a string of numbers, the task is to find the maximum value from the string, you can add a ‘+’ or ‘*’ sign between any two numbers.
"""

def solution(string):
    result = 0
    for i in string:
        i = int(i)
        ## if i = 0 we always add it
        if i == 0:
            continue

        ## if we are stuck at zero or i = 1, add it
        if i == 1 or result == 0:
            result += i
        else:
            result *= i


    return result


if __name__ == '__main__':
    print(solution('123'))
    print(solution('0123'))
    print(solution('0321'))