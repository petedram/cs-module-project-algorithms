'''
Input: a List of integers where every int except one shows up twice
Returns: an integer



- if shows up twice, ignore
- count occurances of each item, if count is 1, return that



'''
def single_number(arr):
    # Your code here

    for item in arr:
        i = 0
        count = 0
        while i < len(arr):
            if item == arr[i]:
                count+=1
            i+=1

        if count == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")