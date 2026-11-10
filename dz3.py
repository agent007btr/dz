s = [29, 10, 14, 37, 13]
print("Исходный:", s)
n = len(s)
for i in range(n):
    m = i
    for j in range(i + 1, n):
        if s[j] < s[m]:
            m = j
    s[i], s[m] = s[m], s[i]
    print( s)
print("Результат:", s)