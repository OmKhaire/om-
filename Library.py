
n = int(input("Enter number of library members: "))

borrow = []


for i in range(n):
    x = int(input("Enter books borrowed by member {}: ".format(i + 1)))
    borrow.append(x)

total = 0
for i in borrow:
    total = total + i

average = total / n
print("Average books borrowed =", average)


highest = borrow[0]
lowest = borrow[0]

for i in borrow:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print("Highest borrow count =", highest)
print("Lowest borrow count =", lowest)


count = 0
for i in borrow:
    if i == 0:
        count = count + 1

print("Members who borrowed no books =", count)


mode = borrow[0]
max_count = 0

