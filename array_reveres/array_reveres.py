def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element " + str(i+1) + ": "))
    arr.append(element)

print("Original array: ", arr)
print("Reversed array: ", reverse_array(arr))







