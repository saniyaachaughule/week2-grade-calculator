# Saniya Choughule
# Week 2 Project
# Student Grade Calculator

# Function to calculate grade and comment based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A", "Excellent!"
    elif average >= 80:
        return "B", "Very Good!"
    elif average >= 70:
        return "C", "Good"
    elif average >= 60:
        return "D", "Need Improvements"
    else:
        return "F", "Failed"


# Function to validate marks entered by the user
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            # Check if marks are within valid range
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Display program title
print("=" * 50)
print("STUDENT GRADE CALCULATOR")
print("=" * 50)

# Get number of students with validation
while True:
    try:
        num_students = int(input("Enter number of students: "))

        if num_students > 0:
            break

        print("Enter a positive number.")

    except ValueError:
        print("Invalid input.")


# Lists to store student data
student_names = []
student_results = []


# Collect student information
for i in range(num_students):

    print(f"\nStudent {i+1}")

    # Get student name
    name = input("Enter student name: ")

    # Get marks for three subjects
    math = get_valid_marks("Math")
    science = get_valid_marks("Science")
    english = get_valid_marks("English")

    # Calculate average marks
    average = (math + science + english) / 3

    # Determine grade and comment
    grade, comment = calculate_grade(average)

    # Store student name
    student_names.append(name)

    # Store student results in dictionary
    student_results.append({
        "average": average,
        "grade": grade,
        "comment": comment
    })


# Display results table
print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)

print(f"{'Name':<20} {'Average':<10} {'Grade':<10} {'Comment'}")
print("-" * 70)

for i in range(num_students):

    print(
        f"{student_names[i]:<20}"
        f"{student_results[i]['average']:<10.1f}"
        f"{student_results[i]['grade']:<10}"
        f"{student_results[i]['comment']}"
    )


# Create list of averages for statistics
averages = []

for result in student_results:
    averages.append(result["average"])

# Calculate class statistics
class_average = sum(averages) / len(averages)
highest = max(averages)
lowest = min(averages)

# Display statistics
print("\nClass Statistics")
print(f"Class Average: {class_average:.1f}")
print(f"Highest Average: {highest:.1f}")
print(f"Lowest Average: {lowest:.1f}")


# Search for a student by name
search = input("\nEnter student name to search: ")

found = False

for i in range(len(student_names)):

    if student_names[i].lower() == search.lower():

        print("\nStudent Found")
        print("Name:", student_names[i])
        print("Average:", round(student_results[i]["average"], 1))
        print("Grade:", student_results[i]["grade"])

        found = True
        break

# Display message if student not found
if not found:
    print("Student not found.")


# Save results to a text file
with open("results.txt", "w") as file:

    file.write("STUDENT RESULTS\n\n")

    for i in range(len(student_names)):

        file.write(
            f"{student_names[i]} - "
            f"{student_results[i]['average']:.1f} - "
            f"{student_results[i]['grade']}\n"
        )

# Confirmation message
print("\nResults saved to results.txt")