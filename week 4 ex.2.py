def ascii_code_collector():
    # read the user's input for a standard character
    character = input("Please enter a standard character: ")

    # check if a single input has been entered using len()
    if len(character) == 1:

        # if the length of the input is 1, determine the ASCII code using ord() and display it
        ascii_code = ord(character)
        print(f"The ASCII code for {character} is {ascii_code}.")
    else:
        print("Error: Please enter a single character.")

# call the function to test it
ascii_code_collector()
ascii_code_collector()
