# take the input
num = int(input("Enter a number: "))

# defining a flag
flag = False

# all prime numbers are greater than 1
if num > 1:
    # checking for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, flag is set to true
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")