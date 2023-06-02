from random import randint

my_unsorted_list = [randint(-20, 20) for _ in range(20)]

def sort_combsort(list_to_sort:list) -> tuple :
    """Sort a given list with the comb sort algorithm and give back the result

    Returns:
        tuple: contains the sorted list and a counter of iteration
    """
    reduction_factor = 1.2857 # Where 1.2857 is supposed to be the best reduction factor
    interval =  len(list_to_sort)
    sorted_list = list_to_sort.copy()
    has_switched = True
    iteration = 0

    while interval > 1 or has_switched :
        has_switched = False
        interval = int(interval / reduction_factor)
        interval = 1 if interval < 1 else interval

        for i in range(0, len(sorted_list) - interval) :
            if sorted_list[i] > sorted_list[i+interval] :
                has_switched = True
                sorted_list[i], sorted_list[i+interval] = sorted_list[i+interval], sorted_list[i]
        iteration +=1
    result = (sorted_list, iteration)
    return result

"""print(f"Unsorted list : {my_unsorted_list}")
comb_sorted_list, comb_iteration = sort_combsort(my_unsorted_list) 
print(f"SORTED list (comb sort) : {comb_sorted_list} with {comb_iteration} iterations")"""