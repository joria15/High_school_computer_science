
def main():
    choice = input("Choose an option (1-4): ")
    if choice == "1":
    elif choice == "2":
    elif choice == "3":
    elif choice == "4":
    else:
            print("Invalid option. Please choose 1-4.")
    if __name__ == "__main__":
        main()

def eligibility():
    #part 1
    try:
        grade_level = int(input("Enter a grade_level from 9-12: "))
        attendance_percent = int(input("Enter a level from 0-100%: "))
        discplinary = (input("Disciplanary issues (yes/no): "))

        #part 2
        if not(discplinary == "no"):
            if grade_level > 11:
                if not(grade_level < 10 or attendance_percent < 85) or not(grade_level < 11 or attendance_percent < 80) or (grade_level == 12):
                    print("you can pariticipate even with displinary issues!")
                else:
                    print("no pariticipate")
            else:
                print("no participate")

        if not(grade_level < 10 or attendance_percent < 85) or not(grade_level < 11 or attendance_percent < 80) or (grade_level == 12):
                    print("you can pariticipate!")
        else:
             print("no pariticipate")       
    except ValueError:
        print("Invalid input!")

eligibility()
