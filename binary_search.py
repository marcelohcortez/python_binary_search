import random
from list import listOfNumbers

def binary_search(list, target):
    low = 0 #set the low index
    high = len(list) -1 #set the high index
    
    midpoint = (low + high) // 2 #define the starting midpoint

    if high < low:
        print('\nThat number is not on the list\n')
        return
    elif list[midpoint] == target: #best case scenario, the target is in the middle of the list
        print(f'\nThe chosen number was in position {midpoint}')
        return
    elif target < list[midpoint]: #if the target is smaller than midpoint, set a new high and look in the left of the list
        return binary_search(list, target, low, midpoint-1)
    else: #if the target is higher than midpoint, set a new low and look in the right of the list
        return binary_search(list, target, midpoint+1, high)

if __name__ =='__main__':
    target = int(input('\nSelect a number from 1 to 50000 to search for: \n')) #receive the target from the user
    print(binary_search(listOfNumbers, target)) #print the return of the function
