def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

numbers = [5, 4, 2, 7, 11, 15]
print(max)