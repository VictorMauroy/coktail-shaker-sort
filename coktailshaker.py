from random import randint

my_unsorted_list = [randint(-20, 20) for _ in range(20)]

def sort_coktail_shaker(list_to_sort:list) -> list :
    """Sort a given list with the coktail shaker algorithm and give back the result
    
    Returns:
        list: the sorted list
    """
    has_switched = True
    sorted_list = list_to_sort.copy()
    start_index = 0
    end_index = len(sorted_list) - 1 # "list length -1 because we check at index+1
    
    while(has_switched) :
        has_switched = False

        # Ascending check to move the greater value to the end
        for i in range(start_index, end_index) :
            if(sorted_list[i] > sorted_list[i+1]) :
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                has_switched = True
        end_index -= 1
        
        # Descending check to move the lower value to the start
            # Range : start from end_i and end with start_i - 1 (because the end value is excluded)
            # step = -1 to check in a decreased order
        for i in range(end_index, start_index - 1, -1) : 
            if(sorted_list[i] > sorted_list[i+1]) :
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                has_switched = True
        start_index += 1
    return sorted_list

print(f"Unsorted list : {my_unsorted_list}")
print(f"SORTED list : {sort_coktail_shaker(my_unsorted_list)}")