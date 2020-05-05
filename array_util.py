

def get_array():
  n=int(input("enter the length of the array: "))
  if(isinstance(n,int) and n<=0):
    return None
  arr=list(int(num) for num in input("Enter the integer list elements : ").strip().split(' '))[:n]
  return arr