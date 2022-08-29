num = int (input("How many fibonnaci numbers do you want? "))

x = 1

if num == 0:
    fib = []
elif num == 1:
    fib = [1]
elif num == 2:
    fib = [1,1]
elif num > 2:
    fib = [1,1]
    while x < (num - 1):
        fib.append(fib[x]+fib[x-1])
        x +=1
    print(fib)
