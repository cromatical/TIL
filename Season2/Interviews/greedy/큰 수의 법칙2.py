n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

fisrt_num = lst[n - 1]
second_num = lst[n - 2]
print(fisrt_num, second_num)

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        
        result += fisrt_num
        m -= 1
    
    if m == 0:
        break
    
    result += second_num
    m -= 1
    
print(result)    