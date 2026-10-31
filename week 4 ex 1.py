print("program started......")

character=input("Please enter standard character: ")
if len(character)==1:
    ascii_code=ord(character)
    print(f"The ascii code for {character} is {ascii_code}")
else:
    print("Error:")
print("program ended")