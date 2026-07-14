num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))


print("============================================================")
print("                 SIMPLE CALCULATOR")
print("============================================================")

print(f"First Number        : {num1}")
print(f"Second Number       : {num2}")

print("------------------------------------------------------------")
print("Arithmetic Operations")
print("------------------------------------------------------------")

print(f"Addition            : {num1+num2}")
print(f"Subtraction         : {num1-num2}")
print(f"Multiplication      : {num1*num2}")
print(f"Division            : {num1/num2}")
print(f"Floor Division      : {num1//num2}")
print(f"Modulus             : {num1%num2}")
print(f"Exponentiation      : {num1**num2}")

print("------------------------------------------------------------")
print("Assignment Operators")
print("------------------------------------------------------------")

print(f"Initial Value       : {num1}")

print(f"After += 5          : {num1+5}")
print(f"After -= 2          : {num1-2}")
print(f"After *= 2          : {num1*2}")
print(f"After /= 2          : {num1/2}")
print(f"After //= 3         : {num1//3}")
print(f"After %= 2          : {num1%2}")
print(f"After **= 3         : {num1**3}")

print("------------------------------------------------------------")
print("Comparison Operators")
print("------------------------------------------------------------")

print(f"25 == 6             : {25==6}")
print(f"25 != 6             : {25 !=6}")
print(f"25 > 6              : {25>6}")
print(f"25 < 6              : {25<6}")
print(f"25 >= 6             : {25 >= 6}")
print(f"25 <= 6             : {25 <=6}")

print("------------------------------------------------------------")
print("Operator Precedence")
print("------------------------------------------------------------")

print(f"10 + 5 * 2          : {10+5*2}")
print(f"(10 + 5) * 2        : {(10+5)*2}")
print(f"2 ** 3 + 4          : {2 ** 3 +4}")
print(f"(2 + 3) ** 2        : {(2 + 3) ** 2}")

print("============================================================")