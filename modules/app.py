import large
numbers = []
limit = int(input('enter the limit'))
for number in range(1,limit):
    n = input(">>")
    numbers.append(n)
print(numbers)  

l = large.largest_number(numbers)

print(f'largest number is {l}')