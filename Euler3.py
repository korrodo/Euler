def largestPrimeFactor(number):
    prime = 0
    i = 2

    while i <= number/i:
        if number%i == 0:
            prime = i
            number = number/i
        else:
            i = i+1
    if prime < number:
        prime = number

    print(prime)

largestPrimeFactor(600851475143)