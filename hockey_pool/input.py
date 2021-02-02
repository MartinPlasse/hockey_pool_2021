n = int(input("How many values would you like to take?"))
sum = 0

while n < 0:
    n = int(input("I said how many... n can only take a positive value, try again"))

for i in range(0, n, 1):
    val = int(input("Input value: "))
    sum += val

print(sum)
