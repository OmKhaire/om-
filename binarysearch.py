n = int(input("Enter number of Customer ids: "))

customer_ids = []
for i in range(n):
    x = int(input(f"Enter customer id {i + 1}: "))
    customer_ids.append(x)

Sorted_list = sorted(customer_ids)

target_id = int(input("Enter the target id: "))
print("Sorted List:", Sorted_list)

start = 0
end = n - 1
found = False

while start <= end:
    mid = (start + end) // 2

    if target_id == Sorted_list[mid]:
        print(f"Target ID found at index {mid}")
        found = True
        break

    elif target_id < Sorted_list[mid]:
        end = mid - 1

    else:
        start = mid + 1

if not found:
    print("Target ID not found.")