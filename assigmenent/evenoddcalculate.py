list1 = list(input("Enter No: "))

even_No = 0
odd_no = 0

for i in list1:
    if int(i) % 2 == 0:
        even_No = even_No + int(i)
    else:
        odd_no = odd_no + int(i)
print(even_No , odd_no)
