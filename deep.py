# Define main()
def main():
    # Prompt the user for a response and handle case sensitivity
    Response = input("What is the Answer to the Great Question of Life, the Universe and Everything?  ").lower()
    # Handle leading/trailing whitespaces
    Response = Response.strip()
    # Check if the user's response matches any of the correct answers
    match Response:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        # Output "No" if no match was found
        case _:
            print("No")

# call the main function
if __name__ == "__main__":
    main()