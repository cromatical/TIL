n, m = map(int, input().split())

card_lst = []
for i in range(n):
    lst = list(map(int, input().split()))
    card_lst.append(lst)
    
print(card_lst)

max_lst = []

for cards in card_lst:
    max_lst.append(min(cards))
print(max(max_lst))