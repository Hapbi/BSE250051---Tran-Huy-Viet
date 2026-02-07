n = int(input("Nhập số n: "))

a, b = 0, 1
fibonacci = []

for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("Dãy Fibonacci:", fibonacci)