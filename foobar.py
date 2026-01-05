def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

result = []

for n in range(100, 0, -1):
    if is_prime(n):
        continue  # Do not print prime numbers

    if n % 3 == 0 and n % 5 == 0:
        result.append("FooBar")
    elif n % 3 == 0:
        result.append("Foo")
    elif n % 5 == 0:
        result.append("Bar")
    else:
        result.append(str(n))

print(" ".join(result))
