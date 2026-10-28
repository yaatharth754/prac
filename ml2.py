
# Initialize parameters
cur_x = 2
rate = 0.01
precision = 0.000001
max_iters = 10000
iters = 0

# Function and its derivative
f = lambda x: (x + 3)**2
df = lambda x: 2 * (x + 3)

# Gradient Descent
while iters < max_iters:
    prev_x = cur_x
    cur_x = cur_x - rate * df(prev_x)
    iters += 1

    if abs(cur_x - prev_x) < precision:
        break

print("The local minimum occurs at", cur_x)
print("Minimum value is", f(cur_x))
print("Iterations:", iters)
