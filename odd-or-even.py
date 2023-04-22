# Write a python program that reads a text file named numbers.txt that contain 20 integers.
# The program will create two other text file; 
# The first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt

# read and write the input and output files
with open("numbers.txt", "r") as number_file, open ("even.txt", "w") as even_file, open ("odd.txt", "w") as odd_file:
    # put the numbers from the read file into a list and convert it into integers
    integers=list(int(number_file.split()))
    print(integers)