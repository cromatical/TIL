n, m ,k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst)

first_num = lst[0]
second_num = lst[1]
print(first_num, second_num)
result = 0

first_add_count = m // k
second_add_count = m % k
print(first_add_count , second_add_count)

for i in range(k * first_add_count):    
    result += first_num

for i in range(second_add_count):    
    result += second_num

print(result)