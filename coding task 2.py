#1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#2
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(2024))
print(is_leap_year(2023))
print(is_leap_year(1900))
print(is_leap_year(2000))
#3
L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(L1==L2)
print(L1 is L2)
# == (checks whether the value are same) 
# is (checks whether both variables refer to the same object in memory)

#4
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)

#Section 2
#5
num = 2
count = 0

while count < 10:
    is_prime = True
    divisor = 2

    while divisor < num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(num)
        count += 1

    num += 1
#6
for i in range(1, 21):

    if i % 4 == 0:
        pass

    if i == 13:
        continue

    if i == 18:
        break

    print(i)
#7
grade = int(input("Enter your marks: "))

if grade >= 90:
    result = "A"
else:
    if grade >= 80:
        result = "B"
    else:
        if grade >= 70:
            result = "C"
        else:
            result = "Fail"

print("Grade:", result)
#8
num = int(input("Enter an integer: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#Section 3
#9
scores = [85, 92, 78, 95, 88, 95, 90]

highest = float('-inf')
second_highest = float('-inf')

for score in scores:

    if score > highest:
        second_highest = highest
        highest = score

    elif score > second_highest and score != highest:
        second_highest = score

print("Highest score:", highest)
print("Runner-up score:", second_highest)

#10
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)
#11
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:", common)
#12
my_tuple = (10, 20, 30)

try:
    my_tuple[1] = 50
except TypeError as e:
    print("Error:", e)
    
#Section 4
#13
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

#14
squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#15
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_data = {key: value for key, value in data.items() if value > 2}
print(new_data)
