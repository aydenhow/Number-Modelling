# negative_fibonacci.py #
# Models Negative Fibonacci sequence and plots.
# F(n) = F(n-2) - F(n-1) and F(n) = F(n-1) - F(n-2)

from matplotlib import pyplot as plt

start = input("Enter number of Negative Fibonacci numbers to generate: ")
values = [1, -1]
rev_values = [1, 1]
current = 1

if start.isdigit():
    count = int(start)
else:
    print("Invalid input! Please enter an integer...")
    exit()

while count > 2:
    values.append(values[-2] - values[-1])
    rev_values.append(rev_values[-1] - rev_values[-2])
    count -= 1

print("Values: " + str(values))

plt.figure(figsize=(10, 6))
plt.plot(range(len(values)), values)
plt.xlabel("Sequence Number")
plt.ylabel('Value')
plt.title(" F(n) = F(n-2) - F(n-1)")
plt.show()
plt.clf()

plt.figure(figsize=(10, 6))
plt.plot(range(len(rev_values)), rev_values)
plt.xlabel("Sequence Number")
plt.ylabel('Value')
plt.title(" F(n) = F(n-1) - F(n-2)")
plt.show()
