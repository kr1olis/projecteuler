# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
sqrtnumber = int(number ** 0.5)
result = [x for x in range(sqrtnumber)]
for i in range(2,sqrtnumber):
    for j in range(2*i,sqrtnumber,i):
        result[j] = 0
primes = [x for x in result if result[x] != 0]
primes.reverse()
for i in range(len(primes)):
    if number % primes[i] == 0:
        answer = primes[i]
        break
print(answer)