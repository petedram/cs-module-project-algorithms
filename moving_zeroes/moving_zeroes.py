'''
Input: a List of integers
Returns: a List of integers
'''

#according to tests, we have to move zeros to the end of list

#for each item in array
#if zero
#remove it, everything else should shift down
#and add zero to end


def moving_zeroes(arr):
    # Your code here
    for num in arr:
        if num == 0:
            #remove, ensuring index is changed for each remaining
            arr.remove(num)
            #add to end
            arr.append(num)
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")