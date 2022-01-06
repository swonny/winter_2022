import sys

# input = sys.stdin.readline()

for i in range(int(input())):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))