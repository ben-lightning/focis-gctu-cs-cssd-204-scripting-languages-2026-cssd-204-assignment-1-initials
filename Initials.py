# File: initials.py
# Description: Prints stylized 12x10 block initials for BCL with specific spacing.
# Assignment Number: 1
#
# Name: Benedict Coffie-Long
# STUDENT ID: YOUR_STUDENT_ID
# Email: YOUR_EMAIL
# Grader: GRADER_NAME
#
# On my honor, Benedict Coffie-Long, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # This main function executes the stylized layout printing for the initials BCL.
    
    # 1. Blank line before the small initials
    print()

    # 2. Three periods followed by small capital initials
    print("...BCL")

    # 3. Blank line between small and large initials
    print()

    # 4. Large stylized letters (10 rows high, exactly 60 characters wide)
    print("...BBBBBBBBBB..........CCCCCCCCCC..........LL...............")
    print("...BB........B.........CC........CC........LL...............")
    print("...BB........B.........CC..................LL...............")
    print("...BBBBBBBBBB..........CC..................LL...............")
    print("...BBBBBBBBBB..........CC..................LL...............")
    print("...BB........B.........CC..................LL...............")
    print("...BB........B.........CC..................LL...............")
    print("...BB........B.........CC..................LL...............")
    print("...BB........B....**...CC........CC...**...LL.............**")
    print("...BBBBBBBBBB.....**....CCCCCCCCCC...**...LLLLLLLLLLLL....**")

    # 5. Blank line after the large letters
    print()


main()
