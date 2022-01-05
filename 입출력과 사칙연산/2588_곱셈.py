a = int(input())
b = input()
sum = 0
b.reverse()

for i in range(3):
    temp = int(b[i])*a
    print(temp)
    
    sum = temp*(10**i)