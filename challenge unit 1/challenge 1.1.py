def recursive_factorial(n):
  if n == 1:
     return n
  else:
     return n*recursive_factorial(n-1)     

number = int(input("Enter the value: "))
print("The factorial of", number, "is", recursive_factorial(number))





