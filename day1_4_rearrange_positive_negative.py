#Rearrange positive and negative numbers with constant extra space
#https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/-->not exactly this question in web link 

import array_util

def rearrange_positive_negative(arr):
  n=len(arr)
  neg=0
  pos=n-1
  while(neg < pos):
    if(arr[neg]>0):
      temp =arr[pos]
      arr[pos]=arr[neg]
      arr[neg] = temp
      pos = pos-1
    else:
      neg = neg+1
  return arr


def main():
	arr = array_util.get_array()
	print("array before reaaragment of +ve and -ve : {}".format(arr))
	print("array after reaaragment of +ve and -ve : {}".format(rearrange_positive_negative(arr)))

if __name__ == "__main__": 
	print ("Executed directly")
	main()
else:
	print("Invoked from outside script")