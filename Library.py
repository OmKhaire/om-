n = int(input("Enter number of library members: "))

borrow = []
for i in range(n):
    x = int(input("Enter books borrowed by member " + str(i + 1) + ": "))
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

print("Frequency:")

for i in borrow:
    freq = 0
    for j in borrow:
        if i == j:
            freq = freq + 1
    print(i, "=", freq)

mode = borrow[0]
maxfreq = 0

for i in borrow:
    freq = 0
    for j in borrow:
        if i == j:
            freq = freq + 1
    if freq > maxfreq:
        maxfreq = freq
        mode = i

print("Mode =", mode)
print("Frequency of mode =", maxfreq)
