def is_prime(func):
    def wrapper(*args):
        prime_num = func(*args)
        if prime_num % 2 == 0:
            if prime_num == 2:
                print("Простое число")
            else:
                print("Составное число")
        d = 3
        while d * d <= prime_num and prime_num % d != 0:
            d += 2
        if d * d > prime_num:
            print("Простое число")
        else:
            print('Составное число')
        return prime_num
    return wrapper


@is_prime
def sum_three(*args):
    suma = sum(args)
    return suma


numb = sum_three(0, 0, 124211)
print(numb)