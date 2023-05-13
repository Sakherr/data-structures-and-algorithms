def insertShiftArray(arr, val):
    mid = (len(arr) - 1) // 2  # Find the middle index of the input array
    arr_copy = [0] * len(arr)  # Create a new array of the same length as input array, filled with zeros
    for i in range(len(arr)):
        arr_copy[i] = arr[i]  # Copy each element of the input array to the new array
    for i in range(mid+1, len(arr)):
        arr[i] = arr_copy[i-1]  # Shift elements to the right by copying them from arr_copy
        arr[mid] = val  # Insert the new value at the middle index
    else:
        arr = [0] * (len(arr) + 1)  # Create a new array with an extra element
        for i in range(len(arr)):
            if i < mid+1:
                arr[i] = arr_copy[i]  # Copy elements from arr_copy to arr
            elif i == mid+1:
                arr[i] = val  # Insert the new value at the middle index
            else:
                arr[i] = arr_copy[i-1]  # Copy elements from arr_copy to arr
        arr[-1] = arr_copy[-1]  # Copy the last element from arr_copy to the last index of arr
    return arr  # Return the modified array

arr= [2,4,6,-8]  # Create an input array
val= 5  # Create a new value to be inserted
print(insertShiftArray(arr,val))  # Call the insertShiftArray function and print the result
