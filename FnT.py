# function of factorial 
def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)
 
 # function of trailing zeroes 
def trailing_zeroes(num):
    fac = factorial(num)
    count=0
    while(fac % 10 == 0):
        count += 1
        fac= fac/10
    return count 

# Driver code 
if __name__=="__main__":
    num=int(input("Enter a number to find its factorial: "))
    fac= factorial(num)
    print(f'The factorial of {num} is {fac}')
    trail= trailing_zeroes(num)
    print(f'Trailing zeroes in {fac} is {trail}')
