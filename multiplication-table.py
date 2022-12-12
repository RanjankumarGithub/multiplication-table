def multiplication_table_application(given_input):
    title="MULTIPLICATION TABLE APPLICATION" #title of the project
    print()
    print(title)
    #using for loop and range function to extract numbers from 2 to given input
    for num in range(2,given_input+1):
        print("______") #header line
        print()
        print("Multiplication Table of",num)
        print("______")
        print()
        #using for loop to extract numbers from 1 to 10
        for i in range(1, 11):
            #calculating the products
            product = num * i
            #printing the multiplication table using formatting
            print("{} x {} = {}".format(num,i,product))
#taking an integer input  from user
given_input = int(input("Enter the value :"))
#calling define user function
multiplication_table_application(given_input)