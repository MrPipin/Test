import random

number = random.randint(15, 30)

arr = list(range(5))

for num in arr:
    num = random.randint(15, 30)
    print(num)
    if num == 22:
        break
else:
    print("good")

print("Hello")