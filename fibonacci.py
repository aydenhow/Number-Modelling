# fibonacci.py #
# Models Fibonacci sequence and plots.

from matplotlib import pyplot as plt

start = input("Enter number of Fibonacci numbers to generate: ")
values = [1, 1]
current = 1

if start.isdigit():
    count = int(start)
else:
    print("Invalid input! Please enter an integer...")
    exit()

while count > 2:
    values.append(values[-1] + values[-2])
    count -= 1

print("Values: " + str(values))

plt.figure(figsize=(10, 6))
plt.plot(range(len(values)), values)
plt.xlabel("Sequence Number")
plt.ylabel('Value')
plt.title(str(start) + " Fibonacci Sequence Values")
plt.show()
