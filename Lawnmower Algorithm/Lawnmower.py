# Tyrei Diggs 2/26/2024
# CPSC 335 Project 1
# Purpose: Create an alternating algorithm that separates 1's and 0's

def lawnmower(size, disk):
    """Algorithm sorts the array like a lawnmower cuts grass."""
    for x in range(int(size / 2)-1):
        for i in range(size-1):
            if disk[i] > disk[i + 1]:
                temp = disk[i]
                disk[i] = disk[i + 1]
                disk[i + 1] = temp
        print(disk)
        for j in range(size-1, 0, -1):
            if disk[j] < disk[j-1]:
                temp = disk[j]
                disk[j] = disk[j-1]
                disk[j-1] = temp
        print(disk)
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

    print("Sorting this array of ones and zeros using the lawnmower algorithm.")
    lawnmower(2*n, disk)
    print(disk)

main()

