# conjecture.py #
# Models Collatz or 3n + 1 conjecture.
# Starting value given by input. Graphs iterations until 1 is reached and saves plot to .png

from random import randint
from matplotlib import pyplot as plt

start = input("Enter starting value or R for random: ").upper()
values = []

if start.isdigit():
    current = int(start)
elif start == 'R':
    current = randint(0, 10**9)
    start = current   #To fix graph title only.
else:
    print("Invalid input! Please enter an integer...")
    exit()

while values.count(1) <= 0:
    values.append(current)
    if current % 2 == 0:
        current = current / 2
    else:
        current = 3 * current + 1
print("Values: " + str(values))
print("Iteration to reach one: " + str(len(values)))

plt.figure(figsize=(10, 6))
plt.plot(range(len(values)), values)
plt.xlabel("Iteration Number")
plt.ylabel('Value')
plt.title("Collatz Conjecture with Starting Value " + str(start))
plt.savefig("collatz_conjecture_" + str(start) + ".png")
plt.show()
