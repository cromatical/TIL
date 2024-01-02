def merge_split(data_lst):
    if len(data_lst) == 1:
        return data_lst
    
    medium = int(len(data_lst) / 2)
    left = merge_split(data_lst[:medium])
    right = merge_split(data_lst[medium:])
    
    return merge(left, right)


def merge(left, right):
    left_idx = 0
    right_idx = 0
    sorted_lst = []
    
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] <= right[right_idx]:
            sorted_lst.append(left[left_idx])
            left_idx += 1
        else:
            sorted_lst.append(right[right_idx])
            right_idx += 1
    
    while len(left) > left_idx:
        sorted_lst.append(left[left_idx])
        left_idx += 1
        
    while len(right) > right_idx:
        sorted_lst.append(right[right_idx])
        right_idx += 1
    
    return sorted_lst 


if __name__== '__main__':
    print("테스트 코드")
    test_case = [[1, 9, 2, 3]]
    
    for test in test_case:
        print(test)
        sort_lst = merge_split(test)
        print(sort_lst)
    print()