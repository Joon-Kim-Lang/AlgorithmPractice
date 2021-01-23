n, m, k = map(int, input().split())
number = list(map(int, input().split()))

number.sort()

first = number[-1]
second= number[-2]

count = (m // (k+1)) * k
count += m % (k+1)

result = count * first
result += (m-count) * second

print(result)

