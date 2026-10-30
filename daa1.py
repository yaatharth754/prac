def recur(n, steps):
    steps[0] += 1

    if n <= 1:
        return n

    return recur(n - 1, steps) + recur(n - 2, steps)


def nonrecur(n):
    steps = 0
    a = 0
    b = 1

    for i in range(2, n + 1):
        steps += 1
        c = a + b
        a = b
        b = c

    return (a if n == 0 else b), steps


n = int(input("Enter a number: "))

recursive_steps = [0]
recursive_result = recur(n, recursive_steps)

nonrecursive_result, nonrecursive_steps = nonrecur(n)

print("\nRecursive Fibonacci:", recursive_result)
print("Recursive Steps:", recursive_steps[0])

print("\nNon-recursive Fibonacci:", nonrecursive_result)
print("Non-recursive Steps:", nonrecursive_steps)