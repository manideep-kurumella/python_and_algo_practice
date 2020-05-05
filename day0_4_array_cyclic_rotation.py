#https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/
#Program to cyclically rotate an array by one
#Given an array, cyclically rotate the array clockwise by one.

def rotate_cyclic(array):
    length = len(array)
    temp = array[length-1]
    for i in range(length-1,0,-1):
        array[i] = array[i-1]
    array[0] = temp


print("Enter array elements")
array = [int(i) for i in input().split()]
print("array before rotation : ",array)
rotate_cyclic(array)
print("array after rotation : ",array)