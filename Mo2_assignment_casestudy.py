"""
Name: Sakhawat Islam
Mo2_assignment_casestudy.py
A simple application to accept student names and GPAs, then determine if they qualify for the Dean's List or Honor Roll based on specific GPA thresholds.
"""

def process_students():
    """
    Main function to continuously prompt for student records and determine awards.
    """
    while True:
        # Ask for and accept a student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

        # Quit processing student records if the last name entered is 'ZZZ'
        if last_name.upper() == 'ZZZ':
            break

        # Ask for and accept a student's first name
        first_name = input("Enter student's first name: ")

        while True:
            try:
                # Ask for and accept the student's GPA as a float
                gpa_input = input(f"Enter {first_name} {last_name}'s GPA: ")
                gpa = float(gpa_input)
                break  # Exit the inner loop if input is a valid float
            except ValueError:
                print("Invalid input. Please enter a numerical value for GPA.")

        # Test if the student's GPA is 3.5 or greater
        if gpa >= 3.5:
            # If so, print a message saying that the student has made the Dean's List
            print(f"{first_name} {last_name} has made the Dean's List!")
        # Test if the student's GPA is 3.25 or greater
        elif gpa >= 3.25:
            # If so, print a message saying that the student has made the Honor Roll
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} does not qualify for an award this semester.")

        print("-" * 20)  # Print a separator for better readability


if __name__ == "__main__":
    process_students()
