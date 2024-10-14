def palindromeProduct():
    answer = 0
    for i in range(100,999):
        for k in range(100,999):
            c = i*k
            product = str(c)
            if product == product[::-1]:
                if c > answer:
                    answer = c
    print(answer)

palindromeProduct()