# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def Sum(nums):
    total = 0
    for x in nums:
        total += x
    return total


def Average(n, nums):
    average = Sum(nums) / n
    return average


def Maximum(nums):
    maximum = nums[0]
    for x in nums:
        if x > maximum:
            maximum = x
    return maximum


def Minimum(nums):
    minimum = nums[0]
    for x in nums:
        if x < minimum:
            minimum = x
    return minimum


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Number must be a positive non-zero integer")
        return

    nums = []
    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        nums.append(num)

    print("\nResults:")
    print(f"Sum:     {Sum(nums)}")
    print(f"Average: {Average(n, nums)}")
    print(f"Maximum: {Maximum(nums)}")
    print(f"Minimum: {Minimum(nums)}")


if __name__ == "__main__":
    main()