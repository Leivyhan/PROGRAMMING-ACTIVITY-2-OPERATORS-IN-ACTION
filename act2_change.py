amount = int(input("Enter amount in pesos: "))

hundreds = amount // 100
remainder = amount % 100

twenties = remainder // 20
remainder = remainder % 20

fives = remainder // 5
remainder = remainder % 5

ones = remainder // 1

print(f"100 pesos: {hundreds}")
print(f"20 pesos: {twenties}")
print(f"5 pesos: {fives}")
print(f"1 peso: {ones}")