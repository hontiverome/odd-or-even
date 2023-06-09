# **PROGRAM 1**
# Write a python program that reads a text file named numbers.txt that contain 20 integers.
# The program will create two other text file; 
# The first text file will be named even.txt that will contain all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt

# read and write the input and output files
import time
with open("numbers.txt", "r") as integer_file, open ("even.txt", "w") as even_file, open ("odd.txt", "w") as odd_file:
    contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)\n"))
    while True:
        if contents=='y':
            # put the numbers from the read file into a list and convert it into integers
            integers=[lines.strip() for lines in integer_file]
            integer_list=[int(j) for j in integers]
            print(integer_list)
            break
        elif contents=='n':
            integers=[lines.strip() for lines in integer_file]
            integer_list=[int(j) for j in integers]
            break
        else:
            print("invalid")
            contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)\n"))
            continue
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
                print("You chose even.")
                time.sleep(0.5)
                even_result=("Here is the even list.\n")
                for i in range(len(even_result)):
                    print(even_result[i], end='', flush=True)
                    time.sleep(0.1)
                for line in even_file:
                    print(line.strip().rjust(25)+'\n')
                print('__________________________________________________________________________________________________')
            elif print_response=='odd':
                print("You chose odd.")
                time.sleep(0.5)
                even_result=("Here is the odd list.\n")
                for i in range(len(even_result)):
                    print(even_result[i], end='', flush=True)
                    time.sleep(0.1)
                for line in odd_file:
                    print(line.strip().rjust(25)+'\n')
                print('__________________________________________________________________________________________________')
            elif print_response=='exit':
                print("\nThank you.")
                exit()
            else:
                print("Invalid")
                print("____________________________________________________________________________________________________")
        elif response=='n':
            print("\nThank you.")
            exit()
        else:
            print("Invalid")
            print("____________________________________________________________________________________________________")
   
# HONTIVEROS, JEROME ANDREI O. 
# BSCPE 1-5