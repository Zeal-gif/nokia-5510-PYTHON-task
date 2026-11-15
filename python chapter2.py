python chaptter 2
    
    
    
# 2.1
x = 2, y = 3, x + y = 5 
total = x + y
 print('x=', x)
 print('value of', x, '+', x, 'is', (x+x))
print (‘x=’)
print(x+y,(y+x)

#2.4
print('Addition', 27.5 + 2)
print('Subtraction', 27.5 - 2)
print('multiplication', 27.5 * 2)
print('division', 27.5 / 2)
print('floor division', 27.5 // 2)
print('exponentiation', 27.5 ** 2)

#2.5
pi = 3.14159
r = 2
Area = pi * r**2
diameter = 2 * r
Circumference = 2 * pi * r

Print('Area', Area)
Print('Diameter', diameter)
Print('Circumference', Circumference)

#2.6
number = int(input('Enter any number'))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#2.7 
number = 1024

if number % 4 == 0:
    print("number is a multiple of 4")

if number % 2 == 0:
    print("number is a multiple of 2")
    
 #2.8
print("number \t Square \t Cube")
for number in range(0, 6):
    Square = number ** 2
    Cube = number ** 3
    print(number, "\t", Square, "\t", Cube)

#2.9
print('B', ord('B'))          
print('C', ord('C'))        
print('D', ord('D'))          
print('b', ord('b'))          
print('c', ord('c'))
print('d', ord('d'))
print('0', ord('0'))
print('1', ord('1'))
print('2', ord('2'))         
print('space', ord(' '))
print('$', ord('$'))


#2.10
user_number1 = int(input("Enter first Integer"))
user_number2 = int(input("Enter second Integer"))
user_number3 = int(input("Enter third Integer"))

Sum = number1 + number2 + number3
Average = Sum / 3
product = number1 * number2 * number3
Smallest = min(number1, number2, number3)
largest = max(number1, number2, number3)

print(f"Sum, {Sum}\n product {product},\n Smallest {Smallest}\n, largest, {largest}")

#2.11
User_A = int(input("Enter Five digit number"))

digit1 = number // 10000
digit2 = number % 10000 // 1000
digit3 = number % 10000 // 100
digit4 = number % 10000 // 10
digit5 = number % 10000

print(digit1, (" "), digit2, (" "), digit3, (" "), digit4, (" "), digit5)

#2.12
principal = 10000
rate = 0.07

amount_for_10 = p(1+r)**10
amount_for_20 = p(1+r)**20
amount_for_30 = p(1+r)**30

print(amount for 10)
print(amount for 20)
print(amount for 30)

#2.13
Number = 5 ** 10
print("5 to the power of 10:", Number)

number = 5 ** 100
print("5 to the power of 100:", number)

number = 5 ** 1000
print("5 to the power of 1000:", number)

Number = 5 ** 10000
print("5 to the power of 10000:", Number)

#2.14
User_age = int(input("Enter your age"))
Maximum_heart_rate = 220 - age
lower_target = Maximum_heart_rate * 0.50
upper_target = Maximum_heart_rate * 0.85

print("maximum heart rate:", maximum heart rate)
print("lower target:", lower target)
print("upper target:", upper target)

#2.15
digit1 = float(input("Enter first number"))
digit2 = float(input("Enter Second number"))
digit3 = float(input("Enter third number"))

if digit1 > digit2:
    temp = digit1
    digit1 = digit2
    digit2 = temp

if digit2 > digit3:
    temp = digit2
    digit2 = digit3
    digit3 = temp

if digit1 > digit2:
    temp = digit1
    digit1 = digit2
    digit2 = temp

print("number in ascending order:")   
    
    
    
    
    
    








