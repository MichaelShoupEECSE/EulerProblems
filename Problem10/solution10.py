#Prime number generator
#Using the Sieve of Erastothenes
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
#using the generator, it prints out the 10001 prime number
sum_primes=0
for item in gen_primes():
    if item > 2000000:
        print(sum_primes)
        break
    sum_primes += item
