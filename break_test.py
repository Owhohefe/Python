listA = [30,11,21,13,42,35,6,7]

x = 0

while x < 1:
    number =int(input("Enter a number: "))

    for num in listA:
        if number == num:
            print("Number found as",num)
            x = x+1
            break
    else:
        print(number,"not found in list")
    
