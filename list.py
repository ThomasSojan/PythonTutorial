numbers = [10,20,30,90,2,19]
large = numbers[0]
for number in numbers:
    if number > large:
        large = number
print(large)

numbers.append(30)
print(numbers)

numbers.insert(5,10)
print(numbers)

numbers.remove(2)
print(numbers)

print(numbers.count(10))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

list2 = numbers.copy()
list2.append(999)
print(list2)

