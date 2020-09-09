# python3
# David Koziol
# ISQA 3900 9.9.2020

def display_title():
    print("Welcome to the Grade Calculator \n")

def get_total_points():
    points_1 = int(input("Enter the total score (0-1000): "))
    while points_1 < 0 or points_1 > 1000:
        print("You must enter integer values >= 0 and <= 1000. Try again.")
        points_1 = int(input("Enter the total score (0-1000): "))
    else:
        return points_1

def get_letterGrade(averageEarned):
    if averageEarned >= 92.0 and averageEarned <= 100:
        averageEarned = 'A'
    if averageEarned >= 88.0 and averageEarned <= 91.99:
        averageEarned = 'B+'
    if averageEarned >= 82.0 and averageEarned <= 87.99:
        averageEarned = 'B'
    if averageEarned >= 78.0 and averageEarned <= 81.99:
        averageEarned = 'C+'
    if averageEarned >= 70.0 and averageEarned <= 77.99:
        averageEarned = 'C'
    if averageEarned >= 60.0 and averageEarned <= 69.99:
        averageEarned = 'D'
    if  averageEarned < 60.0 and averageEarned:
        averageEarned = 'F'
        return averageEarned



def main():
    display_title()
    total_points = get_total_points()
    averageEarned = total_points / 1000 * 100
    letterGrade = get_letterGrade(averageEarned)
    print("You earned an average of " + str(averageEarned) + "%." + " Letter grade earned: " + letterGrade)

if __name__ == "__main__":
    main()