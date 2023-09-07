n = int(input())
print("? 1 2",flush=True)
x = int(input())
print("? 2 3",flush=True)
y = int(input())
print("? 1 3",flush=True)
z = int(input())
a = (x - y + z) // 2
b = (y - z + x) // 2
c = (y + z - x) // 2
A = f"! {a} {b} {c}"
for i in range(4,n+1):
    print(f"? 1 {i}",flush=True)
    s = int(input())
    A += f" {s-a}"
print(A)