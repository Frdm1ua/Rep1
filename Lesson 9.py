d = {}
for word in input().split():
    if word not in d:
        d[word] = 0
    else:
        d[word] += 1
        print(d[word])