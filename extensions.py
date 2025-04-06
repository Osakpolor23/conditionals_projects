# define the main function
def main():
    # Ask for input, remove whitespaces and store in a variable
    user_input = input("Enter file name along with its extension (e.g cat.gif, document.pdf):  ").strip().lower()
    # check if the user_input has a period(".")
    if "." in user_input:
        # split into prefix and suffix part using the rightmost period(".") found
        file_prefix, file_suffix = user_input.rsplit(".", 1) # The rsplit(".", 1) split at the last period to separate the file.
        # check the file extension and output the appropriate media type using the file_suffix
        match file_suffix:
            case "gif":
                print("image/gif")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            # for any other file extension
            case _:
                print("application/octet-stream") # The default media type
    # If no period(".") is found, assume there is no extension
    else:
        print("application/octet-stream")

    

# call the main function
if __name__ == "__main__":
    main()

