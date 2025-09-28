# the program, in short, asks for 2 numbers to create a product variable and then asks for a perfect square number to add onto the product

# necessary for math.___ 
import math
# defines function
def func():
# asks for 2 numbers and 2 inputs
# will NOT work if you don't put 2 inputs because the number of variables & inputs need to match (it's the same thing as putting i and n as seperate variables)
    i,n = int(input("Give 2 numbers.\n")),int(input(""))
    product = i*n
    print(product)
    sq = int(input("Now give a square number:\n"))
    # checks square number validity
    sqr = math.sqrt(sq)
    # math.trunc truncates to 0 (rounds to the closest integer to 0 e.g 7.3 -> 7, -5.3 -> -5, it's helpful because it turns the float (decimal) into an integer)
    isqr = math.trunc(sqr)
    #if the truncation of the square root squared is equal to the square number, then it's a perfect square (best way i could explain)
    if isqr*isqr == sq:
        # uses f escape character to add the symbols + and = and prints it out
        print(f"{isqr} + {product} = {isqr+product}")
    else:
        print("Invalid root.")
        # if the square number is not a perfect square number then it makes you restart the whole program by returning it to the function
        return func();
#calls the function
func()
