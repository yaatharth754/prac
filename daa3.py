n = int(input("Enter the number of items: "))

items = []

for i in range(n):
    weight, profit = map(int, input().split())
    ratio = profit / weight
    items.append((weight, profit, ratio))

capacity = int(input("Enter the capacity of the knapsack: "))

items.sort(key=lambda x: x[2], reverse=True)

totalProfit = 0

for weight, profit, ratio in items:
    if weight <= capacity:
        totalProfit += profit
        capacity -= weight
    else:
        totalProfit += ratio * capacity
        break

print("Maximum Profit:", totalProfit)

# 3
# 10 60
# 20 100
# 30 120
# 50
