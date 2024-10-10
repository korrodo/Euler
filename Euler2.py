def fiboEvenSum(n):
    fibo = [1,2]
    sum = 0
    while fibo [-1] < n:
        fibo.append(fibo[-1]+fibo[-2])
    for i in fibo:
        if i%2 == 0:
            sum = sum + i
    print(sum)

fiboEvenSum(4000000)