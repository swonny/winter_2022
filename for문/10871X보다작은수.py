n,x = map(int, input().split())
arr = []
for i in range(n):
    a = int(input())
    if(a<x):
        arr.append(a)

print(arr)
