def largest_number(numbers):
    l = numbers[0]
    for number in numbers:
        if number > l:
            l = number
    return l        
