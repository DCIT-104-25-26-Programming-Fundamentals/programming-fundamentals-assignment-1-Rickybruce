# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def addition(a, b) :
    print(f"Result: {a} + {b} = {a + b}")


def subtraction(a, b) :
    print(f"Result: {a} - {b} = {a - b}")


def multiplication(a, b) :
    print(f"Result: {a} * {b} = {a * b}")


def division(a, b) :
    if b == 0 :
        print("Error: Cannot divide by zero.")
    else :
        result = a / b
        print(f"Result: {a} / {b} = {result:.2f}")


def modulus(a, b) :
    if b == 0 :
        print("Error: Cannot divide by zero.")
    else :
        print(f"Result: {a} % {b} = {a % b}")


def exponentiation(a, b) :
    print(f"Result: {a} ** {b} = {a ** b}")


def main() :
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    o = int(input("Select an operation (1-7):"))

    while o != 7 :
        if 1 <= o <= 6 :
            N1 = int(input("Enter first number : "))
            N2 = int(input("Enter second number: "))
            if o == 1 :
                addition(N1,N2)
            elif o == 2 :
                subtraction(N1,N2)
            elif o == 3 :
                multiplication(N1,N2)
            elif o == 4 :
                division(N1,N2)
            elif o == 5 :
                modulus(N1,N2)
            elif o == 6 :
                exponentiation(N1,N2)
        else :
            print("Error : Invalid Input")

        o = int(input("Select an operation (1-7):"))

    print("Goodbye!")


if __name__ == "__main__":
    main()

