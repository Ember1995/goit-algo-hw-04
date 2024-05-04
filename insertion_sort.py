import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


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
    exec_time = timeit.timeit(f'insertion_sort({arr})', globals=globals(), number=1)
    print(f"{type_name:<20} | {size:<10} | {exec_time:<15.6f}")
