# Tyrei Diggs 2/26/2024
# CPSC 335 Project 1
# Purpose: Create an alternating algorithm that separates 1's and 0's

def leftRight(size, disk):
    """Algorithm goes from font end to back end until ones and zeros are separated."""
    for i in range(size):
    # Loop the same number of time as the size of the array
        for j in range(size-1):
        # starts at begining of array and goes to end
            if disk[j] > disk[j+1]:
                temp = disk[j]
                disk[j] = disk[j+1]
                disk[j+1] = temp
    return disk


def main():
    """ Create an array of Zeros and ones."""
    n = int(input("Input positive number for number of zeros/ones:"))
    zeros, ones = n, n
    disk = []

    for i in range(n):
        disk.append("1")
        disk.append("0")
    print(disk)

    print("Sorting this array of ones and zeros using the left-to-right algorithm.")
    leftRight(2*n, disk)
    print(disk)

main()

