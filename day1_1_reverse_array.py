#Write a program to reverse an array
#https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
import array_util

def reverse_array(arr):
	n=len(arr)
	for i in range(0,n//2):         #note there is a // here to get int o/p 
			temp = arr[i]
			arr[i] = arr[n-i-1]
			arr[n-i-1] = temp
	return arr

def reverse_with_slicing(arr):
	return arr[len(arr)::-1]

def main():
	arr = array_util.get_array()
	print("array before reversal : {} ".format(arr))
	print("array after reversal : {}".format(reverse_array(arr)))
	print(arr)
	print("array after reversal : {}".format(reverse_with_slicing(arr)))

if __name__ == "__main__": 
	print ("Executed directly")
	main()
else:
	print("Invoked from outside script")
