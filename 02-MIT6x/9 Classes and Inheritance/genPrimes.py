########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: Jul 27, 2022
## Exercise: genPrimes
''' 
Write a generator, 'genPrimes', that returns the sequence of prime numbers on successive calls to its next() method:
2, 3, 5, 7, 11, ...

Have the generator keep a list of the primes it's generated. A candidate number x is prime if
(x % p) !=0 for all earlier primes p.
'''
########################################################################################################################

# Practice with Fibonacci
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

# genFib Examples
# fib = genFib()
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())

# for n in genFib():
#     print(n)









# Solution for genPrimes
def genPrimes():
    primes = []     # keep a list of primes
    x = 1
    
    while True:
        x += 1
        for p in primes:
                if x % p == 0:
                    break
        else:
                primes.append(x)
                yield x

primeGenerator = genPrimes()

# print(primeGenerator.__next__()) # prime 2
# print(primeGenerator.__next__()) # prime 3
# print(primeGenerator.__next__()) # prime 5
# print(primeGenerator.__next__()) # prime 7
# print(primeGenerator.__next__()) # prime 11
# print(primeGenerator.__next__()) # prime 13
# print(primeGenerator.__next__()) # prime 17
# print(primeGenerator.__next__()) # prime 19
# print(primeGenerator.__next__()) # prime 23

for n in genPrimes():
    print(n)


# print(foo.__next__())
# print(foo.__next__())
# print(foo.__next__())
# print(foo.__next__())
# print(foo.__next__())




