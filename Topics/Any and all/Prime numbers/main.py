prime_numbers = []
for n in range(2, 1000):
    if all([n % x for x in range(2, n - 1)]):
        prime_numbers.append(n)
# print(prime_numbers)
