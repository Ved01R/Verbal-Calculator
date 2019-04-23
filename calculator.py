while True:
    print("Welcome to my calculator! a.k.a My First Python Project.")
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        ...
    elif user_input == "subtract":
        ...
    elif user_input == "multiply":
        ...
    elif user_input == "divide":
        ...
    else:
       print("Unknown input")
       print('Try again')
       user_input = input(": ")
       if user_input == "yes":
               ...
       if user_input == "no":
               print("Thanks for using my calculator.")
               break
       else:
        print("Unknow input")
        print("Please type a number..")
        user_input = input(": ")
       if user_input == "yes":
        ...
       if user_input == "no":
               print("Thanks for using my calculator.")
               break
       else:
        print("Programe End....")
        print("You broke the calculator!")
        break

    if user_input == "add":
           num1 = float(input("Enter a number: "))
           num2 = float(input("Enter another number: "))
           result = str(num1 + num2)
           print("The answer is " + result)
           print("Do you want to try once again")
           user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Unknow input")
               print("Please type'Yes' or 'No'")
               user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Programe End....")
               print("You broke the calculator!")
               break

    if user_input == "subtract":
           num1 = float(input("Enter a number: "))
           num2 = float(input("Enter another number: "))
           result = str(num1 - num2)
           print("The answer is " + result)
           print("Do you want to try once again")
           user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Unknow input")
               print("Please type'Yes' or 'No'")
               user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Programe End....")
               print("You broke the calculator!")
               break 

    if user_input == "multiply":
           num1 = float(input("Enter a number: "))
           num2 = float(input("Enter another number: "))
           result = str(num1 * num2)
           print("The answer is " + result)
           print("Do you want to try once again")
           user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Unknow input")
               print("Please type'Yes' or 'No'")
               user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Programe End....")
               print("You broke the calculator!")
               break 

    if user_input == "divide":
           num1 = float(input("Enter a number: "))
           num2 = float(input("Enter another number: "))
           result = str(num1 / num2)
           print("The answer is " + result)
           print("Do you want to try once again")
           user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Unknow input")
               print("Please type'Yes' or 'No'")
               user_input = input(": ")
           if user_input == "yes":
               ...
           if user_input == "no":
               print("Thanks for using my calculator.")
               break
           else:
               print("Programe End....")
               print("You broke the calculator!")
               break
