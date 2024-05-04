import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


list_sizes = [1000, 500, 10]
list_types = ['sorted', 'reverse_sorted', 'partially_sorted', 'unsorted']
lists = {}


for size in list_sizes:
    sorted_list = list(range(size))
    reverse_sorted_list = sorted_list[::-1]
    partially_sorted_list = sorted_list[:size//2] + random.sample(sorted_list[size//2:], size//2)
    unsorted_list = random.sample(range(size), size)
    
    lists[f'sorted_{size}'] = sorted_list
    lists[f'reverse_sorted_{size}'] = reverse_sorted_list
    lists[f'partially_sorted_{size}'] = partially_sorted_list
    lists[f'unsorted_{size}'] = unsorted_list


print(f"{'Тип':<20} | {'Кількість':<10} | {'Час (секунди)':<15}")
print('-' * 50)


for name, arr in lists.items():
    type_name, size = name.rsplit('_', 1)
    exec_time = timeit.timeit(f'merge_sort({arr})', globals=globals(), number=1)
    print(f"{type_name:<20} | {size:<10} | {exec_time:<15.6f}")
