#S.McDonald 11/20/2016
#exception_handing
#This program is modified from the 'Average of Numbers' program to include exceptions for any IOError's or ValueErrors


#define main
def main():
    try:
        #open the file numbers.txt
        #input
        #myfile is a file object
        myfile = open('numbers.txt', 'r') #open the file for reading

        #open the file for writing
        my_output_file = open('my_average.txt', 'w')

        total = 0 #start total count at 0

        #compute total and find average
        for line in myfile:
            total = total + int(line) #find the sum of all the numbers in the 'numbers.txt' file
            average = total / 10 #divide the sum of the numbers in the 'numbers.txt' file to find the average
            print(line, end="")

        #write to an output file
        my_output_file.write(str(average) + '\n')

        #close both files
        myfile.close()
        my_output_file.close()

    #exceptions
    except IOError:
        print("ERROR! AN IOError HAS OCCURED! CHECK FOR FILE PERMISSION AND/OR CHECK FILE LOCATION TO SEE IF FILE EXISTS!") #print this if an IOError occurs

    except ValueError:
        print("ERROR! A VALUE ERROR HAS OCCURED IN THE numbers.txt FILE! MAKE SURE ALL NUMBERS IN FILE ARE INTEGERS!") #print this if a ValueError occurs

    except:
        print("ERROR! AN ERROR HAS OCCURED!") #print this if any other error occurs

    else:
        print("\nThe average is: ", average) #else, print the average of all the numbers in the file

#call the main function
main()
