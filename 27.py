f = open("")
s = f.readlines()
n = int(s[0])  # количество пар
summi = 0
d = 10**6
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    summi += max(x, y)
    if abs(x - y) % 3 != 0:
        d = min(d, abs(x - y))
if summi % 3 != 0:
    print(summi)
else:
    print(summi - d)
