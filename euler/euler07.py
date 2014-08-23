def is_prime(number):
    counter = 2
    while counter**2 <= number:
        if number % counter == 0:
            return False
        counter += 1
    return True

not_found = True
counter = 0
i = 2
while not_found:
    if is_prime(i):
        counter += 1
        print(counter,".",i)
    if counter == 10001:
        not_found = False
    else:
        i += 1

print(i)