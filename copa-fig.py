n = int(input())
m = int(input())
fig = []
for c in range(m):
    f = int(input())
    if not f in fig:
        fig.append(f)

print(n-len(fig))