#####  Discover the ith term of the Fibonacci sequence #####

n = int(input("type which term you want to find: "))
last=1
pen=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        term = last + pen
        pen = last
        last = term
        count += 1
    print(term)
