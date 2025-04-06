# Define the function
def main():
    # prompt the user for the greeting
    greeting = input("Greeting:  ").strip().lower()
    # check the prefix the greeting starts with
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    # if the prefix starts with something else
    else:
        print("$100")


# call the main function
if __name__ == "__main__":
    main()
