largest = None
smallest = None

while True:
    num = input("Enter a number: ") # Recebe o número do usuário

    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
        smallest = num
    elif largest < num:
        largest = num
    elif smallest > num:
        smallest = num

# Print maximum and minimum
print("Maximum is", largest)
print("Minimum is", smallest)
