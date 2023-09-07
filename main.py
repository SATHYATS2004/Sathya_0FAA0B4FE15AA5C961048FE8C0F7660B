# 1.1 implement a recursive function to calculate the factorial of given number.

"""
1! =1 A-1
2! =2 A-1!--->2 A- 1
3! =3 A-2!--->3 A-2 A- 1
.
.
10! =10 A-9!--->10 A- 9 A- 8 A-...A-1

Formula-n x (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1: 
    return 1
  else:
    return n*fact_rec(n-1)

number=int(input("Enter a value:"))
res=fact_rec(number)

print("The factorial of {} is {}".format(number,res))

