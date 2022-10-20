d = int(input())
i = int(1)
r = int(0)
res = int(1)
while i<=d:
	n = int(input())
	r = r+n
	if r<1000000:
		res = res+1
	i = i+1
print(res)