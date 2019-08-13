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
n=1
for item in gen_primes():
    if n > 10000:
        print(item)
        break
    n+=1
