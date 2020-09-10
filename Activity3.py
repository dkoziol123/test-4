# python3
# David Koziol
# ISQA 3900 9.9.2020

def display_title():
    # displays the title
    print("Welcome to the Grade Calculator \n")

def get_total_points():
    # stores and validates the score input
    points_1 = int(input("Enter the total score (0-1000): "))
    while points_1 < 0 or points_1 > 1000:
        print("You must enter integer values >= 0 and <= 1000. Try again.")
        points_1 = int(input("Enter the total score (0-1000): "))
    else:
        return points_1

def get_letterGrade(averageEarned):
    # assignes a letter grade based off of score
    if averageEarned >= 92.0 and averageEarned <= 100:
        averageEarned = 'A'
        return averageEarned
    if averageEarned >= 88.0 and averageEarned <= 91.99:
        averageEarned = 'B+'
        return averageEarned
    if averageEarned >= 82.0 and averageEarned <= 87.99:
        averageEarned = 'B'
        return averageEarned
    if averageEarned >= 78.0 and averageEarned <= 81.99:
        averageEarned = 'C+'
        return averageEarned
    if averageEarned >= 70.0 and averageEarned <= 77.99:
        averageEarned = 'C'
        return averageEarned
    if averageEarned >= 60.0 and averageEarned <= 69.99:
        averageEarned = 'D'
        return averageEarned
    if  averageEarned < 60.0 and averageEarned:
        averageEarned = 'F'
        return averageEarned



def main():
    # after the program completes it will use this while loop for validation
    oneMoreTime = 'y'
    while oneMoreTime.lower() == 'y':
        # takes in input using the functions within this program
        display_title()
        total_points = get_total_points()
        averageEarned = total_points / 1000 * 100
        letterGrade = get_letterGrade(averageEarned)
        print("You earned an average of " + f"{averageEarned:.1f}" + "%." + " Letter grade earned: " + letterGrade)
        print()
        # asks the user if they would like to run the program again
        oneMoreTime = input("Would you like to enter another score? (y/n)? \n")
        print()


if __name__ == "__main__":
    main()