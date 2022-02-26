# wiki: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def count_primes(number):
    if number == 0 and number == 1:
        return 0
    primes = [True] * number
    primes[0] = primes[1] = False
    for i in range(2, number):
        if primes[i]:
            for j in range(i * i, number, i):
                primes[j] = False
    return primes.count(True)

# (2 3 5 7) => 4
# count_primes(10)
