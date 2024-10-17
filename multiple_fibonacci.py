# multiple_fibonacci.py #
# Models modified Fibonacci sequence and plots.
# Triples: F(n) = F(n-3) + F(n-2) + F(n-1) and Quadruples: F(n) = F(n-4) + F(n-3) + F(n-2) + F(n-1)

from matplotlib import pyplot as plt

start = input("Enter number of Fibonacci numbers to generate: ")
values = [1, 1, 2]
quad_values = [1, 1, 2, 4]
current = 1

if start.isdigit():
    count = int(start)
else:
    print("Invalid input! Please enter an integer...")
    exit()

while count > 4:
    values.append(values[-1] + values[-2] + values[-3])
    quad_values.append(values[-1] + values[-2] + values[-3] + values[-4])
    count -= 1
if count == 4:
    values.append(values[-1] + values[-2] + values[-3])

plt.figure(figsize=(10, 6))
plt.plot(range(len(values)), values)
plt.plot(range(len(quad_values)), quad_values)
plt.xlabel("Sequence Number")
plt.ylabel('Value')
plt.title("Extended Fibonacci Sequence")
plt.legend(["Triples", "Quadruples"])
plt.show()
