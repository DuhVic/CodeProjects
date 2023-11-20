number1 = 1537
def prime_factor(number2 : int):
    if number2 == 1 :
        return[1]
    A = 2
    factors = []
    while A**2 <= number2:
        if number2 % A == 0:
            factors.append(A)
            number2 //= A
        else:
            A += 1
    if number2 > 1:
        factors.append(number2)
    return(factors)
print("These are the prime factors: ")
print(prime_factor(number1))
