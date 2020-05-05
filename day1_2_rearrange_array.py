#Rearrange an array such that arr[i] = i
#https://www.geeksforgeeks.org/rearrange-array-arri/

import array_util

def rearrange1(arr):
	n=len(arr)
	i=0
	while(i<n): 
		if(arr[i]>n or arr[i]< -1):
			print("Invalid array entry ....returning None")
			return None
		elif arr[i]== -1 or arr[i]== i :
			i=i+1
			continue
		else:
			temp = arr[arr[i]]
			arr[arr[i]] = arr[i]
			arr[i] =temp
	return arr

def main():
	arr = array_util.get_array()
	print("array before reaaragment : {}".format(arr))
	print("array after reaaragment : {}".format(rearrange1(arr)))

if __name__ == "__main__": 
	print ("Executed directly")
	main()
else:
	print("Invoked from outside script")