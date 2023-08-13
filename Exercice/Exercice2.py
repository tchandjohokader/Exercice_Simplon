def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


nb = 6
result = factorial(nb)

print(f"La factorielle de {nb} est {result}")
