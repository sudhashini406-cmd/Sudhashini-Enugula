a = int(input("Enter a: "))

if a % 2 == 0:
    last = a - 1
else:
    last = a

result = []
for num in range(1, last + 1, 2):
    result.append(num)

print(result)
