#Move all zeroes to end of array
#https://www.geeksforgeeks.org/move-zeroes-end-array/

import array_util

def rearrange_zero(arr):
  n=len(arr)
  min=0
  for i in range (1,n):
    if(arr[i]!= 0):
      continue
    else:
      arr[i] = arr[min]
      arr[min]=0
      min+=1
  return arr

def main():
	arr = array_util.get_array()
	print("array before reaaragment of Zeros: {}".format(arr))
	print("array after reaaragment of Zeros : {}".format(rearrange_zero(arr)))

if __name__ == "__main__": 
	print ("Executed directly")
	main()
else:
	print("Invoked from outside script")