from random import randint

my_unsorted_list = [randint(-20, 20) for _ in range(20)]
subdivisions = 0

def give_merge_sort(list_to_sort:list) -> tuple:
    """Invoke merge sort and give back the sorted list and the subdivision count

    Returns:
        tuple: sorted list and subdivision count
    """
    global subdivisions
    return (merge_sort(list_to_sort), subdivisions) 

def merge_sort(list_to_sort:list) -> list:
    """Recursively divide a given list until each of its elements are divided
    and merge them back progressively

    Returns:
        list: contains the sorted list
    """
    global subdivisions
    if len(list_to_sort) <= 1 :
        return list_to_sort
    else :
        # Use of List Slicing
        first_half = list_to_sort[:len(list_to_sort)//2] # take length/2 elements from the beginning
        second_half = list_to_sort[len(list_to_sort)//2:] # take length/2 elements from the end
        subdivisions += 1
        return merge(merge_sort(first_half), merge_sort(second_half))

def merge(list_A:list, list_B:list) -> list :
    """Merge two list if their size is one, else divide them again

    Returns:
        list: 
    """
    if not list_A :
        return list_B
    if not list_B :
        return list_A
    if list_A[0] <= list_B[0] :
        if len(list_A) == 1 :
            return list_A + list_B
        else :
            merged_list = [list_A[0]]
            merged_list += merge(
                list_A[1-len(list_A):],
                list_B
            )
            return merged_list
        
    else :
        if len(list_B) == 1 :
            return list_B + list_A
        else :
            merged_list = [list_B[0]]
            merged_list += merge(
                list_B[1-len(list_B):],
                list_A
            )
            return merged_list

"""print(f"Unsorted list : {my_unsorted_list}")
print(f"SORTED list : {merge_sort(my_unsorted_list)}")"""