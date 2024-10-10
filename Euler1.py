def multiplesOf3or5(num):
    i = 0
    sum = 0
    while i < num:
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
        i = i + 1
    print(sum)
multiplesOf3or5(1000)