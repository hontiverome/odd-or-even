# Write a python program that reads a text file named numbers.txt that contain 20 integers.
# The program will create two other text file; 
# The first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt

# read and write the input and output files
with open("numbers.txt", "r") as integer_file, open ("even.txt", "w") as even_file, open ("odd.txt", "w") as odd_file:
    # put the numbers from the read file into a list and convert it into integers
    integers=[line.strip() for line in integer_file]
    integer_list=[int(j) for j in integers]
    # iterate the list
    for num in integer_list:
    # identify whether integer is even or odd using mod
    # if odd, write it to "odd.txt" file
        if num%2==1:
            odd_file.write(str(num)+"\n")
    # if even, write it to "even.txt" file
        else:
            even_file.write(str(num)+"\n")

# HONTIVEROS, JEROME ANDREI O. 
# BSCPE 1-5