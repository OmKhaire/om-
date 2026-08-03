n = int(input("Enter number of Customer ids: "))

customer_ids = []


for i in range(n):
    x = int(input("Enter customer id {}: ".format(i + 1)))
    customer_ids.append(x)

target_id=int(input("Enter the target id: "))
print(customer_ids)

for i in range(0,n):
    if(customer_ids[i] == target_id):
        print(f"Target id Found {i}")
        break
       
       