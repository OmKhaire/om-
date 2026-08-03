def Linear_Search():
    n = int(input("Enter number of Customer IDs: "))

    customer_ids = []

    for i in range(n):
        x = int(input(f"Enter customer ID {i + 1}: "))
        customer_ids.append(x)

    target_id = int(input("Enter the target ID: "))
    print("Customer IDs:", customer_ids)

    for i in range(n):
        if customer_ids[i] == target_id:
            print(f"Target ID found at index {i}")
            return

    print("Target ID not found.")


def Binary_Search():
    n = int(input("Enter number of Customer IDs: "))

    customer_ids = []

    for i in range(n):
        x = int(input(f"Enter customer ID {i + 1}: "))
        customer_ids.append(x)

    sorted_list = sorted(customer_ids)

    target_id = int(input("Enter the target ID: "))
    print("Sorted List:", sorted_list)

    start = 0
    end = n - 1
    found = False

    while start <= end:
        mid = (start + end) // 2

        if target_id == sorted_list[mid]:
            print(f"Target ID found at index {mid}")
            found = True
            break
        elif target_id < sorted_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if not found:
        print("Target ID not found.")


result = int(input("Enter 1 for Linear Search or 0 for Binary Search: "))

if result == 1:
    Linear_Search()
else:
    Binary_Search()



      