# Define the main function
def main():
    # Prompt user for input
    user_input = input("Expression: ")
    # remove any extra whitespaces, split and store in a variable
    parts = user_input.strip().split()
    # check the components of parts if it exceeds 3
    if len(parts) != 3:
        print("invalid input!, please provide input in the format x y z (e.g 1 + 1). ")
        return
    # unpack the components into x, y and z
    x, y, z = parts
    # convert str to int
    x = int(x)
    z = int(z)
    # Perform the arithmetic operation based on the y operator
    if y == "+":
        print(float(x + z))
    elif y == "*":
        print(float(x * z))
    elif y == "-":
        print(float(x - z))
    elif y == "/":
        # check if z is not equal to zero
        if z != 0:
            print(float(x / z))
        # output an error message if z is zero
        else:
            print("Error: Division by zero is not allowed!")

# call the main function
if __name__ == "__main__":
    main()

    
