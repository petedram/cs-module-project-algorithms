'''
Input: a List of integers
Returns: a List of integers
'''

'''
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
'''

def product_of_all_other_numbers(arr):
    # Your code here

    result_list = []
    for num in arr:
        i=0
        multiplied_list = []

        while i < len(arr):
            if i == arr.index(num):
                pass #pass if the index of num is current (what if dup values?)
            else:
                #add num to multiplication array
                multiplied_list.append(arr[i])
                print(f'adding {arr[i]} for multiplication later ')
            i+=1
        
        #multiply the list
        print(f'multiplied list is {multiplied_list}')
        result = 1
        for item in multiplied_list:
            result = result * item
            print(result)
        
        result_value = result

        #append to result
        result_list.append(result_value)
        print(f'result value for this item is {result_value}')

    return result_list



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
