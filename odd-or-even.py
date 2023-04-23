# Write a python program that reads a text file named numbers.txt that contain 20 integers.
# The program will create two other text file; 
# The first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt

# read and write the input and output files
with open("numbers.txt", "r") as integer_file, open ("even.txt", "w") as even_file, open ("odd.txt", "w") as odd_file:
    contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)"))
    while True:
        if contents=='y':
            for line in integer_file:
                print(line.strip().rjust(25)+'\n')
                break
        elif contents=='n':
            break
        else:
            print("invalid")
            contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)"))
            continue
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
with open ("even.txt", "r") as even_file, open ("odd.txt", "r") as odd_file:
    response=str(input("\nWould you like to print out the contents of the text files? (y or n only):\n "))
    while True:
        if response=='y':
            print_response=str(input("\nWhat text file would you like to see? (even, odd, exit):\n "))
            if print_response=='even':
                for line in even_file:
                    print(line.strip().rjust(25)+'\n')
                    print('__________________________________________________________________________________________________')
            elif print_response=='odd':
                for line in odd_file:
                    print(line.strip().rjust(25)+'\n')
                    print('__________________________________________________________________________________________________')
            elif print_response=='exit':
                print("Thank you.")
                exit()
            else:
                print("Invalid")
                print("____________________________________________________________________________________________________")
   
# HONTIVEROS, JEROME ANDREI O. 
# BSCPE 1-5