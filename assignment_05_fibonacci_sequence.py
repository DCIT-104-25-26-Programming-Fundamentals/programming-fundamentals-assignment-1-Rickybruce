# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
 
def fibonacci_seq(num) :
    seq = []
    for i in range(num) :
        if i == 0:
            seq.append(0)
        elif i == 1:
            seq.append(1)
        else :
            seq.append(seq[i-2]+seq[i-1])

    return seq

def check_for_fib(fib_num) :
    if fib_num < 0:
        return False

    a, b = 0, 1
    if fib_num == 0:
        return True
    while b < fib_num:
        a, b = b, a + b
    return b == fib_num


def main() :
    num = int(input("How many terms? "))
    if num <= 0:
        print("Number must be a positive non zero integer")
        return

    fib_seq = fibonacci_seq(num)
    print("Fibonacci seq:", " ".join(map(str, fib_seq)))

    fib_num = int(input("Enter a number to check: "))
    if check_for_fib(fib_num):
        print(f"{fib_num} is a Fibonacci number.")
    else:
        print(f"{fib_num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
