# MSCS532_Assignment5

## Quick Sort
* This is both deterministic and randomized versions of Quicksort.
* Partitation function will select the parvot based on random_pivot flag
* When random_pivot is True; it will select randomized version of Quicksort 
* When False, it will use deterministic version of Quicksort(Always last element as pivot)
* This implementation will run Quicksort algorithm on different sizes of datasets.
* [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400] arry sizes
* This implementation will run on different types of array; random, sorted, reverse sorted.
* This implementation will run both deterministic and randomized versions of Quicksort.
* This version will create a graph of time vs array sizes for all types array and both versions of Quicksort.
* To run this on your local machine, these are the libaries required:
    * matplotlib.pyplot
    * numpy
    * python v 3.6 or higher
* To run open terminal and run
**python3 quicksort.py**
