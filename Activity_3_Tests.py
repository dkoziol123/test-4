# python3
# David Koziol
# ISQA 3900 9.9.2020

def display_title():
    print("Welcome to the Grade Calculator \n")

def get_total_points():
    points_1 = int(input("Enter the total score (0-1000): "))
    if points_1 >= 0 and points_1 <= 1000:
        print(" ", points_1)
    else:
        print("You must enter integer values >= 0 and <= 1000. Try again.")
    return points_1

def get_letterGrade(averageEarned):
    print("test")

def main():
    display_title()
    total_points = get_total_points()
    averageEarned = total_points / 1000 * 100
    print("You earned an average of "+ str(averageEarned) + "%")







if __name__ == "__main__":
    main()