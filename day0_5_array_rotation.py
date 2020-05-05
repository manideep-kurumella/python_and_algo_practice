#https://www.geeksforgeeks.org/array-rotation/
#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
def euclid_gcd(a,b):
  if (a<=0 or b<=0):
    return 0
  while(a!=b):
    if(a>b):
      a=a-b
    else:
      b=b-a
  return a 

def leftRotate(arr,d):
  n=len(arr)
  d=d%n
  gcd = euclid_gcd(n,d)
  for i in range(gcd):
    temp = arr[i]
    j=i
    while(1):
      k=j+d
      if(k>=n):
        k = k-n
      if(k == i):
        break
      arr[j]=arr[k]
      j=k
    arr[j]=temp
  return arr

def main():
  '''print("Enter the array elements : ")
  arr = [int(i) for i in input().split()]
  n = len(arr)'''
  n=int(input("enter the length of the array: "))
  d=int(input("Enter the displacement:"))
  if(isinstance(n,int) and isinstance(d,int)):
    if(n<=0 or d<=0):
      print("Enter a valid input")
      return
  arr=list(int(num) for num in input("Enter the integer list elements ").strip().split(' '))[:n]
  print("integer list before rotation : {}".format(arr))
  print("integer array after rotating left by {} positions {}".format(d,leftRotate(arr,d)))

if __name__ == "__main__": 
    print ("Executed directly")
    main()
else: 
    print ("Imported this in another script")
    main()