""" Arithmetic Operators

"""
print("-------- Addition ----------")
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

print("-------- Subtraction ----------")

print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 + float2)

num = 20
flt = 10.5
print(num - flt)

print("-------- Multiplication  ----------")

print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)

print(10.2 * 3)

print("-------- Divide  ----------")

print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)

print("-------- Floor Division  ----------")

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

print("-------- Modulo   ----------")

print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

print("-------- Precedence  ----------")
# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication

print("-------- Parentheses   ----------")

print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))