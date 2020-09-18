# Author: John Sweetall jts6052@psu.edu  

def digit_sum(n):
  
  if n == 0:
    return 0 
  else:
    return (n % 10) + digit_sum(n//10)

def print_n(n):

  if n == 0:
    return 
  else:  
    print_n(n-1)

def run():

  numb = int(input("Enter an int: "))
  sum1 = digit_sum(numb)
  print(f"sum is {sum1}.")
  

if __name__ == "__main__":
  run()
