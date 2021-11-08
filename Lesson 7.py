a = [1,2,3,5,6,2,8,5]
[int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(a)
print(counter)
