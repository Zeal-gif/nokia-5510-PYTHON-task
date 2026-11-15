# 3.2
a = b = 7
print("a =", a, "\n =", b)

# 3.3
for row in range(10):
    print(row, end=" ")

# 3.4
for row in range(10):
    for column in range(10):
        print("@", end="")
    print()

# 3.6
medical_diagnosis = input("What is your problem? ")
had_it_before = input("Have you had the problem before? ")
if had_it_before == "yes":
    print("Well, you have it again")
else:
    print("Well, you have it now")

# 3.7
print("number \t square \t cube")
for number in range(5):
    square = number ** 2 
    cube = number ** 3
    print(number, "\t", square, "\t", cube)

# 3.8
total = 0
product = 1
for count in range(4):
    number = int(input("Enter a number: "))
    total += number
    product *= number 
    if count == 0:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

average = total / 4
print("Sum", total)
print("Average", average)
print("Product", product)
print("Smallest", smallest)
print("Largest", largest)

# 3.9
number = int(input("Enter 5 digit number: "))
divisor = 10000
while divisor >= 1: 
    digit = number // divisor
    print(digit, end=" ")
    number = number % divisor
    divisor = divisor // 10

# 3.12
number = int(input("Enter 5 digit number: "))
original = number
reverse = 0    
while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10      
print(original == reverse)

# 3.10
principal = 1000
rate = 0.07
for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(year, amount)
