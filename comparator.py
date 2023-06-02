from random import randint
from coktailshaker import sort_coktail_shaker
from combsort import sort_combsort
from mergesort import give_merge_sort

my_unsorted_list = [randint(-20, 20) for _ in range(20)]

print(f"Unsorted list : {my_unsorted_list}")

# Result for Coktail Shaker Sort :
coktail_sorted_list, coktail_counter = sort_coktail_shaker(my_unsorted_list) 
print(f"Coktail shaker : {coktail_sorted_list} with {coktail_counter} iterations")

# Result for Comb Sort :
comb_sorted_list, comb_iteration = sort_combsort(my_unsorted_list) 
print(f"With comb sort : {comb_sorted_list} with {comb_iteration} iterations")

# Result for Merge Sort :
merge_sorted_list, subdivisions_count = give_merge_sort(my_unsorted_list) 
print(f"With merge sort : {merge_sorted_list} with {subdivisions_count} subdivisions")