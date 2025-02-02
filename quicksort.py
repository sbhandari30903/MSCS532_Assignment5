import sys
import random
import numpy as np
import time
import matplotlib.pyplot as plt 


# this function will select the parvot based on random_pivot flag
# when random_pivot is true; it will select use randomized version of Quicksort 
# when False, it will use deterministic version of Quicksort(Always last element as pivot)
def partitation(arr, left, right, random_pivot):
    if random_pivot:
        rand_int = random.randint(left, right)
        # palcing the pivot at the end
        arr[rand_int], arr[right] = arr[right], arr[rand_int]
    pivot_element = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot_element:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1    


# this quick sort will take random_pivot flag to select which version to run
# this quick sort will return the recursion depth
def quicksort(arr, left, right, random_pivot=True, depth=1):
    if left < right:
        pivot = partitation(arr, left, right, random_pivot)
        ld = quicksort(arr, left, pivot-1, random_pivot, depth+1)
        rd = quicksort(arr, pivot+1, right, random_pivot, depth+1)
        return max(ld, rd)
    return depth


# calculate time and depth of quicksort
def getdepthtime(arr, random_pivot):
    t1 = time.time()
    depth = quicksort(arr, 0, len(arr)-1, random_pivot, 1)
    t2 = time.time()
    return t2-t1, depth

    
def sort_array(random_pivot, np_arr_type="unsorted"):
    i = 1000
    time = []
    depth = []
    while i < 1000000:
        # for random array
        array_list = np.random.randint(1, 10000000, i).tolist()
        #to get sorted numpy array
        if np_arr_type == "reverse_sorted":
            array_list = np.arange(i, 0, -1).tolist()
        #to get reverse sorted numpy array
        elif np_arr_type == "sorted":
            array_list = np.arange(1, i+1).tolist()

        print(f"\nPrinting first 10 elements of {np_arr_type} array before and after of size: {i} when random_pivot is {random_pivot}") 
        print(array_list[:10]) 
        rt1, rd1 = getdepthtime(array_list, random_pivot)
        time.append(rt1)
        depth.append(rd1)
        print(array_list[:10]) 
        i *= 2
    return time, depth
    


if __name__ == "__main__": 
    # increase system recurssion depth to 1M
    sys.setrecursionlimit(1000000)
    
    arr_size = []
    i = 1000
    while i < 1000000:
        arr_size.append(i)
        i *= 2

    try:
        ###############################
        # Random pivot quick sort
        ###############################
        #sorts unsorted array of different sizes using randomized quick sort
        rand_time_randomized, rand_depth_randomized = sort_array(True, "unsorted")
        #sorts reverse sorted array of different sizes using randomized quick sort
        r_sorted_time_randomized, r_sorted_depth_randomized = sort_array(True, "reverse_sorted")
        #sorts sorted array of different sizes using randomized quick sort
        sorted_time_randomized, sorted_depth_randomized = sort_array(True, "sorted")

        ################################
        # deterministic pivot quick sort
        ################################
        #sorts unsorted array of different sizes using deterministic quick sort
        rand_time_deterministic, rand_depth_deterministic = sort_array(False, "unsorted")
        #sorts reverse sorted array of different sizes using deterministic quick sort
        r_sorted_time_deterministic, r_sorted_depth_deterministic = sort_array(False, "reverse_sorted")
        #sorts sorted array of different sizes using deterministic quick sort
        sorted_time_deterministic, sorted_depth_deterministic = sort_array(False, "sorted")

    except RecursionError:
        print("Reached maximum safe recursion depth.")
    
    plt.figure(figsize=(12,8))
    plt.plot(arr_size, rand_time_randomized, label='random pivot on unsorted array')
    plt.plot(arr_size, r_sorted_time_randomized, label='random pivot on r_sorted array')
    plt.plot(arr_size, sorted_time_randomized, label='random pivot on sorted array')

    plt.plot(arr_size, rand_time_deterministic, label='deterministic pivot on unsorted array')
    plt.plot(arr_size, r_sorted_time_deterministic, label='deterministic pivot on r_sorted array')
    plt.plot(arr_size, sorted_time_deterministic, label='deterministic pivot on sorted array')
    plt.xlabel('Array Size')
    plt.ylabel('Time taken')
    plt.title('Time taken - Random pivot Vs Last pivot')
    plt.legend()
    plt.savefig('quicksorttime.png')

    plt.figure(figsize=(12,8))
    plt.plot(arr_size, rand_depth_randomized, label='random pivot on unsorted array')
    plt.plot(arr_size, r_sorted_depth_randomized, label='random pivot on r_sorted array')
    plt.plot(arr_size, sorted_depth_randomized, label='random pivot on sorted array')

    plt.plot(arr_size, rand_depth_deterministic, label='random pivot on unsorted array')
    plt.plot(arr_size, r_sorted_depth_deterministic, label='random pivot on r_sorted array')
    plt.plot(arr_size, sorted_depth_deterministic, label='random pivot on sorted array')
    plt.xlabel('Array type')
    plt.ylabel('Rec Depth')
    plt.title('Recurssion depth - Random pivot Vs Last pivot')
    plt.legend()
    plt.savefig('quicksortdepth.png')
