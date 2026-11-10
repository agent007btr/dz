s = [2, 5, 8, 11, 14, 18, 21, 25, 30]
print("Список:", s)
x = 18
a = 0
b = len(s) - 1
r = -1
while a <= b:
    m = (a + b) // 2
    if s[m] == x:
        r = m
        break
    if s[m] < x:
        a = m + 1
    else:
        b = m - 1
print("Индекс", r)