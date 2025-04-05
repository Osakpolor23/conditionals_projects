# Define the main function
def main():
    input_time = input("Enter the time in 24hour format e.g 7:45, 14:20? ")
    hours = convert(input_time)

    # Apply the conditionals that check if it's time for a meal
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    # No else block because it's not meal time


def convert(time):
    # split the time parameter to hours and minute and convert to int
    hour, minute = map(int, time.split(":"))
    # return the summation of hours and minutes
    return hour + minute/60 


if __name__ == "__main__":
    main()

