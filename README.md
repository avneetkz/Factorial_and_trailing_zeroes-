# Factorial_and_trailing_zeroes-
This repository gives the factorial of number that is entered by user and shows the trailing zeroes present in its factorial. 

The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.

## what are trailing zeroes
‘Trailing zeroes’ is nothing else but the number of zeroes at the end. We can find the number of trailing zeroes in a number by repeatedly dividing it by 10 until its last digit becomes non-zero.

Example: factorial of 10= 10! = 10*9! = 10*9*8! =......= 10*9*8*7*6*5*4*3*2*1
                              = 3628800
              trailing zeroes = 3628800 % 10 == 0  count=1
                                362880 % 10 == 0   count=2
                                36288 % 10 != 0     
              trailing zeroes = 2
