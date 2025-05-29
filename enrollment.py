import enrollement_db as db
import enrollment_utility as util
import enrollment_table_display as display
students = {}
courses = {}
enrolled = {}
quizzes = {}


class Student:
    def __init__(self, student_id, fname, lname, address):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.address = address

    def name(self):
        return f"{self.fname} {self.lname}"
    
    def __str__(self):
        return f"{self.student_id}: {self.fname} {self.lname}, Address: {self.address}"

class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

    def __str__(self):
        return f"{self.course_id}: {self.course_name}, Instructor: {self.instructor}"
    
class Enrollment:
    def __init__(self, student_id, course_ids : list):
        self.student_id = student_id
        self.course_ids = course_ids

    def __str__(self):
        return f"Student ID: {self.student_id}, Course ID: {self.course_id}"

class Quiz:
    def __init__(self, quiz_id, quiz_title, student_id, course_id, score):
        self.quiz_id = quiz_id
        self.quiz_title = quiz_title
        self.student_id = student_id
        self.course_id = course_id
        self.score = score

    def __str__(self):
        return f"Quiz ID: {self.quiz_id}, Title: {self.quiz_title}, Student ID: {self.student_id}, Course ID: {self.course_id}, Score: {self.score}"


def main_menu():
    while True:
        util.clear_screen()
        util.set_cursor_coordinate(10,5)
        print("Student Management System".upper())
        util.set_cursor_coordinate(10,6)
        print("-" * 25)
        util.set_cursor_coordinate(10,7)
        print("[1] Manage Students")
        util.set_cursor_coordinate(10,8)
        print("[2] Manage Courses")
        util.set_cursor_coordinate(10,9)
        print("[3] Manage Enrollments")
        util.set_cursor_coordinate(10,10)
        print("[4] Manage Quizzes")
        util.set_cursor_coordinate(10,11)
        print("[5] Exit")
        util.set_cursor_coordinate(10,12)
        print("-" * 25)
        util.set_cursor_coordinate(10,13)
        choice = input("Enter your choice: ")
        if util.validate_choice(choice, 10):
            if choice == '1':
                manage_students()
            elif choice == '2':
                manage_courses()
            elif choice == '3':
                manage_enrollments()
            elif choice == '4':
                manage_quizzes()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")
                main_menu()

def manage_students():
    while True:
        util.clear_screen()
        util.set_cursor_coordinate(10,5)
        print("Manage Students".upper())
        util.set_cursor_coordinate(10,6)
        print("-"*25)
        util.set_cursor_coordinate(10,7)
        print("[1] Add Student")
        util.set_cursor_coordinate(10,8)
        print("[2] Update Student")
        util.set_cursor_coordinate(10,9)
        print("[3] Delete Student")
        util.set_cursor_coordinate(10,10)
        print("[4] View Students")
        util.set_cursor_coordinate(10,11)
        print("[5] Back to Main Menu")
        util.set_cursor_coordinate(10,12)
        print("-"*25)
        util.set_cursor_coordinate(10,13)
        choice = input("Enter choice: ")

        if util.validate_choice(choice, 5):
            if choice == '1':
                while True:
                    util.clear_screen()
                    display.all_students_table_display(students)
                    print("\nAdd New Student [Leave fields blank to exit]".upper())
                    print("-" * 85)
                    print()
                    student_id = input("Student ID: ")
                    if student_id in students:
                        print("Student ID already exists. Please try again.")
                        input("\nPress Enter to continue...")
                        continue
                    if not student_id.strip():
                        break
                    
                    while True:
                        util.clear_screen()
                        util.set_cursor_coordinate(10,5)
                        print("Add New Student".upper())
                        util.set_cursor_coordinate(10,6)
                        print("-" * 25)

                        util.set_cursor_coordinate(10,7)
                        print("Student ID :", student_id)
                        util.set_cursor_coordinate(10,8)
                        print("First Name :")
                        util.set_cursor_coordinate(10,9)
                        print("Last Name  :")
                        util.set_cursor_coordinate(10,10)
                        print("Address    :")
                        util.set_cursor_coordinate(10,11)
                        print("-" * 25)

                        util.set_cursor_coordinate(23,8)
                        fname = input()
                        util.set_cursor_coordinate(23,9)
                        lname = input()
                        util.set_cursor_coordinate(23,10)
                        address = input()

                        
                        if not all(field.strip() for field in [fname, lname, address]):
                            util.set_cursor_coordinate(10,13)
                            confirm = input("All fields are required, Do you want to try again? (y/n): ").strip().lower()
                            
                            if confirm == 'y':
                                continue
                            elif confirm == 'n':
                                break
                            else:
                                util.set_cursor_coordinate(10,14)
                                print("Invalid input.")
                                util.set_cursor_coordinate(10,15)
                                input("Press Enter to continue...")
 
                        students[student_id] = Student(student_id, fname, lname, address)
                        util.set_cursor_coordinate(10,13)
                        print(f"Student {fname} {lname} added successfully.")
                        db.save_student_csv(students)
                        util.set_cursor_coordinate(10,14)
                        input("Press Enter to continue...")
                        break                
            elif choice == '2':
                while True:
                    util.clear_screen()
                    display.all_students_table_display(students)
                    print()
                    print("Update Student Information [Leave fields blank to exit]".upper())
                    print("-" * 85)
                    print()

                    student_id = input("Student ID to update: ")
                    if not student_id.strip():
                        break

                    if student_id in students:
                        util.clear_screen()
                        print("Update Student Information [Leave fields blank to keep current data]\n".upper())
                        display.specific_student_table_display(students[student_id])
                        print()
                        print("First Name : ")
                        print("Last Name  : ")
                        print("Address    : ")

                        util.set_cursor_coordinate(14,7)
                        fname = input() or students[student_id].fname
                        if fname == students[student_id].fname:
                            util.set_cursor_coordinate(14,7)
                            print(students[student_id].fname)

                        util.set_cursor_coordinate(14,8)
                        lname = input() or students[student_id].lname
                        if lname == students[student_id].lname:
                            util.set_cursor_coordinate(14,8)
                            print(students[student_id].lname)

                        util.set_cursor_coordinate(14,9)
                        address = input() or students[student_id].address
                        if address == students[student_id].address:
                            util.set_cursor_coordinate(14,9)
                            print(students[student_id].address)

                        students[student_id].fname = fname
                        students[student_id].lname = lname
                        students[student_id].address = address
                        print(f"\nStudent {student_id} updated successfully.")
                        db.save_course_csv(students)
                    else:
                        print("Student not found.")

                    input("\nPress Enter to continue...")
            elif choice == '3':
                while True:
                    util.clear_screen()
                    display.all_students_table_display(students)
                    print("\nDelete Student [Leave fields blank to exit]".upper())
                    print("-" * 85)
                    student_id = input("\nStudent ID to delete: ")

                    if not student_id.strip():
                        break

                    if student_id in students:
                        util.clear_screen()
                    
                        display.specific_student_table_display(students[student_id])
                        print()
                        confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
                        if confirm == 'y':
                            del students[student_id]
                            print(f"Student {student_id} deleted successfully.")
                            db.save_student_csv(students)
                            input("\nPress Enter to continue...")
                        elif confirm == 'n':
                            print("Deletion cancelled.")
                            input("\nPress Enter to continue...")
                            continue
                        else:
                            print("Invalid input. Deletion cancelled.")
                            input("\nPress Enter to continue...")
                            continue
                    else:
                        print("Student not found.")
                        input("\nPress Enter to continue...")
            elif choice == '4':
                util.clear_screen()
                display.all_students_table_display(students)
                input("\nPress Enter to continue...")
            elif choice == '5':
                return
        
def manage_courses():
    while True:
        util.clear_screen()
        util.set_cursor_coordinate(10,5)
        print("Manage Courses".upper())
        util.set_cursor_coordinate(10,6)
        print("-"*25)
        util.set_cursor_coordinate(10,7)
        print("[1] Add Course")
        util.set_cursor_coordinate(10,8)
        print("[2] Update Course")
        util.set_cursor_coordinate(10,9)
        print("[3] Delete Course")
        util.set_cursor_coordinate(10,10)
        print("[4] View Courses")
        util.set_cursor_coordinate(10,11)
        print("[5] Back to Main Menu")
        util.set_cursor_coordinate(10,12)
        print("-"*25)
        util.set_cursor_coordinate(10,13)
        choice = input("Enter your choice: ")

        if util.validate_choice(choice, 5):
            if choice == '1':
                while True:
                    util.clear_screen()
                    display.course_table_display(courses)
                    print("\nAdd New Course [Leave fields blank to exit]".upper())
                    print("-" * 85)

                    course_id = input("Course ID: ")

                    if not course_id.strip():
                        break

                    if course_id in courses:
                        print("Course ID already exists. Please try again.")
                        input("\nPress Enter to continue...")
                        continue

                    while True:
                        util.clear_screen()
                        util.set_cursor_coordinate(10,5)
                        print("Add New Course".upper())
                        util.set_cursor_coordinate(10,6)
                        print("-" * 25)

                        util.set_cursor_coordinate(10,7)
                        print("ID         : ")

                        util.set_cursor_coordinate(10,8)
                        print("Name       : ")

                        util.set_cursor_coordinate(10,9)
                        print("Instructor : ")

                        util.set_cursor_coordinate(10,10)
                        print("-" * 25)

                        util.set_cursor_coordinate(23,7)
                        print(course_id)

                        util.set_cursor_coordinate(23,8)
                        course_name = input()

                        util.set_cursor_coordinate(23,9)
                        instructor = input()

                        if not all(field.strip() for field in [course_name, instructor]):
                            util.set_cursor_coordinate(10,13)
                            confirm = input("All fields are required, Do you want to try again? (y/n): ").strip().lower()
                            
                            if confirm == 'y':
                                continue
                            elif confirm == 'n':
                                break
                            else:
                                util.set_cursor_coordinate(10,14)
                                print("Invalid input.")
                                util.set_cursor_coordinate(10,15)
                                input("Press Enter to continue...")

                        courses[course_id] = Course(course_id, course_name, instructor)
                        util.set_cursor_coordinate(10,12)
                        print(f"Course {course_name} added successfully.")
                        db.save_course_csv(courses)
                        util.set_cursor_coordinate(10,13)
                        input("Press Enter to continue...")
                        break
                    
            elif choice == '2':
                while True:
                    util.clear_screen()

                    display.course_table_display(courses)
                    print()
                    print("Update Course Information [Leave fields blank to exit]".upper())
                    print("-" * 85)
                    print()

                    course_id = input("Course ID to update: ")
                    if not course_id.strip():
                            break
                    
                    if course_id in courses:
                        util.clear_screen()
                        print("Update Student Information [Leave fields blank to keep current data]\n".upper())    
                        display.specific_course_table_display(courses[course_id])
                        print()
                        print("Course Name     : ")
                        print("Instructor Name : ")

                        util.set_cursor_coordinate(19,7)
                        course_name = input() or courses[course_id].course_name
                        if course_name == courses[course_id].course_name:
                                util.set_cursor_coordinate(19,7)
                                print(courses[course_id].course_name)
                        
                        util.set_cursor_coordinate(19,8)
                        instructor = input() or courses[course_id].instructor
                        if instructor == courses[course_id].instructor:
                                util.set_cursor_coordinate(19,8)
                                print(courses[course_id].instructor)

                        courses[course_id].course_name = course_name
                        courses[course_id].instructor = instructor
                        print(f"Course {course_id} updated successfully.")
                        db.save_course_csv(courses)
                    else:
                        print("Course not found.")
                    
                    input("\nPress Enter to continue...")
            elif choice == '3':
                while True:
                    util.clear_screen()
                    display.course_table_display(courses)
                    print("\nDelete Course")
                    print("=" * 60)
                    course_id = input("Course ID to delete: ")
                    print()
                    if course_id in courses:
                        util.clear_screen()
                        display.specific_course_table_display(courses[course_id])
                        print("=" * 60)
                        confirm = input("Are you sure you want to delete this course? (yes/no): ").strip().lower()
                        if confirm == 'y':
                            del courses[course_id]
                            print(f"Course {course_id} deleted successfully.")
                            db.save_course_csv(courses)
                            input("\nPress Enter to continue...")
                            continue
                        elif confirm == 'n':
                            print("Deletion cancelled.")
                            input("\nPress Enter to continue...")
                            continue
                        else:
                            print("Invalid input. Deletion cancelled.")
                            input("\nPress Enter to continue...")
                            continue
                    else:
                        print("Course not found.")
                        input("\nPress Enter to continue...")
            elif choice == '4':
                util.clear_screen()
                display.course_table_display(courses)

                input("\nPress Enter to continue...")
            elif choice == '5':
                return     

def manage_enrollments():
    while True:
        util.clear_screen()
        util.set_cursor_coordinate(10,5)
        print("Manage Enrollments".upper())
        util.set_cursor_coordinate(10,6)
        print("-"*25)
        util.set_cursor_coordinate(10,7)
        print("[1] Enroll Course")
        util.set_cursor_coordinate(10,8)
        print("[2] Drop Course")
        util.set_cursor_coordinate(10,9)
        print("[3] Masterlist")
        util.set_cursor_coordinate(10,10)
        print("[4] Filter")
        util.set_cursor_coordinate(10,11)
        print("[5] Back to Main Menu")
        util.set_cursor_coordinate(10,12)
        print("-"*25)
        util.set_cursor_coordinate(10,13)
        choice = input("Enter your choice: ")

        if util.validate_choice(choice, 5):
            if choice == '1':
                while True:
                    util.clear_screen()
                    display.all_students_table_display(students)
                    print()
                    print("\nEnroll Student in Course [Leave fields blank to exit]")
                    print("-" * 60)
                    print()
                    student_id = input("Student ID: ")
                    if not student_id.strip():
                        break

                    if student_id not in students:
                        print("Student not found.")
                        input("\nPress Enter to continue...")
                        continue

                    while True:
                        util.clear_screen()
                        print("Student Details")
                        print("=" * 85)
                        display.specific_student_table_display(students[student_id])
                        print()

                        # Create a dictionary of courses the student is NOT enrolled in
                        student_enrollment = enrolled.get(student_id)
                        enrolled_courses = student_enrollment.course_ids if student_enrollment else []
                        available_courses = {cid: cname for cid, cname in courses.items() if cid not in enrolled_courses}
                        if not available_courses:
                            print("No available courses for enrollment.")
                            input("\nPress Enter to continue...")
                            break

                        display.course_table_display(available_courses, "Available Course(s)")
                        print()
                        print("Select a course to enroll in [Leave field blank to exit]")
                        print("-" * 85)
                        course_id = input("Course ID: ")
                        if not course_id.strip():
                            break

                        if course_id not in courses:
                            print("Course not found.")
                            input("\nPress Enter to continue...")
                            continue

                        if course_id in enrolled_courses:
                            print(f"Student {students[student_id].fname} {students[student_id].lname} is already enrolled in {courses[course_id].course_name}.")
                            input("\nPress Enter to continue...")
                            continue

                        if student_id not in enrolled:
                            enrolled[student_id] = Enrollment(student_id, [course_id])
                        else:
                            enrolled[student_id].course_ids.append(course_id)
                    
                        print(f"\nStudent {students[student_id].fname} {students[student_id].lname} is enrolled in {courses[course_id].course_name} successfully.")
                        db.save_enrolled_csv(enrolled)
                        input("\nPress Enter to continue...")
                        
            elif choice == '2':
                while True:
                    util.clear_screen()
                    display.enrolled_table_display(enrolled, Enrollment, students)
                    print("\nDrop Course".upper())
                    print("-" * 85)
                    print()
                    student_id = input("Select Student ID: ")

                    if not student_id.strip():
                        break

                    if student_id in enrolled:
                        while True:
                            util.clear_screen()
                            display.specific_enrolled_table_display(students, student_id, enrolled[student_id])
                            print()
                            course_id = input("Select Course ID to drop [Leave field blank to cancel]: ")

                            if not course_id.strip():
                                break

                            if course_id in enrolled[student_id].course_ids:
                                enrolled[student_id].course_ids.remove(course_id)
                                print(f"Course {course_id} removed from student {student_id}'s enrollment.")

                                if not enrolled[student_id].course_ids:
                                    del enrolled[student_id]
                                    print(f"Student {student_id} dropped all course and will be removed from the enrolled student list.")
                                    

                                db.save_enrolled_csv(enrolled)
                                input("\nPress Enter to continue...")
                        
                            else:
                                print(f"Course {course_id} not found in student {student_id}'s enrollment.")
                                input("\nPress Enter to continue...")
                    else:
                        print("No enrollments found for this student.")
                        input("\nPress Enter to continue...")

            elif choice == '3':
                util.clear_screen()
                display.enrolled_table_display(enrolled, Enrollment, students)

                input("\nPress Enter to continue...")
            elif choice == '4':
                while True:
                    util.clear_screen()

                    util.set_cursor_coordinate(10,5)
                    print("Filter by [Leave field blank to exit]".upper())
                    util.set_cursor_coordinate(10,6)
                    print("-"*25)
                    util.set_cursor_coordinate(10,7)
                    print("[1] Course")
                    util.set_cursor_coordinate(10,8)
                    print("[2] Student")
                    util.set_cursor_coordinate(10,9)
                    print("-"*25)
                    util.set_cursor_coordinate(10,10)
                    choice = input("Enter your choice: ")

                    if not choice.strip():
                        break

                    if util.validate_choice(choice, 2):
                        if choice == '1':
                            while True:
                                util.clear_screen()
                                display.course_table_display(courses)
                                print()
                                print("View enrolled student by course".upper())
                                print("-" * 85)
                                course_id = input("Course ID: ")
                                if not course_id.strip():
                                    break
                                    
                                if course_id in courses:
                                    util.clear_screen()
                                    found = False
                                    print(f"\nStudents enrolled in {course_id}")
                                    print()
                                    print(f"{'ID':<10} {'Name':<25}")
                                    print("=" * 35)
                                    for student_id, enrollment in enrolled.items():
                                        if course_id in enrollment.course_ids:
                                            student = students[student_id]
                                            print(f"{student.student_id:<10} {student.fname + " "+ student.lname:<25}")
                                            found = True
                                    if not found:
                                        print("No students enrolled in this course.\n")
                                    
                                    input("\nPress Enter to continue...")
                                else:
                                    print("Course not found.")
                                    input("\nPress Enter to continue...")
                                
                        elif choice == '2':
                            while True:
                                util.clear_screen()
                                display.all_students_table_display(students)
                                print("\nView enrolled courses by student".upper())
                                print("-" * 85)
                                student_id = input("Student ID: ")
                                if not student_id.strip():
                                    break

                                if student_id in students:
                                    util.clear_screen()
                                    found = False
                                    print(f"\nCourses enrolled by {students[student_id].name()}")
                                    print()
                                    print(f"{'Course ID':<15} {'Course Name':<25} {'Instructor':<20}")
                                    print("=" * 60)
                                    if student_id in enrolled:
                                        for course_id in enrolled[student_id].course_ids:
                                            course = courses[course_id]
                                            print(f"{course.course_id:<15} {course.course_name:<25} {course.instructor:<20}")
                                            found = True
                                    if not found:
                                        print("No courses enrolled by this student.\n")
                                        
                                    input("\nPress Enter to continue...")
                                else:
                                    print("Student not found.")
                                    input("\nPress Enter to continue...")

            elif choice == '5':
                return

def manage_quizzes():
    while True:
        util.clear_screen()
        util.set_cursor_coordinate(10,5)
        print("Manage Quizzes".upper())
        util.set_cursor_coordinate(10,6)
        print("-"*25)
        util.set_cursor_coordinate(10,7)
        print("[1] Add Quiz")
        util.set_cursor_coordinate(10,8)
        print("[2] View Quizzes")
        util.set_cursor_coordinate(10,9)
        print("[3] Filter Quizzes by Course")
        util.set_cursor_coordinate(10,10)
        print("[4] Compute Grade")
        util.set_cursor_coordinate(10,11)
        print("[5] Back to Main Menu")
        util.set_cursor_coordinate(10,12)
        print("-"*25)
        util.set_cursor_coordinate(10,13)
        choice = input("Enter your choice: ")

        if util.validate_choice(choice, 5):
            if choice == '1':
                while True:
                    util.clear_screen()

                    display.course_table_display(courses)
                    print()
                    print("Add New Quiz [Leave fields blank to cancel]")
                    print("-" * 85)
                    print()

                    print("Course ID  :")
                    print("Quiz Title :")

                    util.set_cursor_coordinate(14, 20)
                    course_id = input()

                    if not course_id.strip():
                        break  

                    if course_id not in courses:
                        util.set_cursor_coordinate(0, 23)
                        print("Course not found.")
                        util.set_cursor_coordinate(0, 24)
                        input("Press Enter to continue...")
                        continue
                    
                    util.set_cursor_coordinate(14, 21)
                    quiz_title = input()
                    
                    if not quiz_title.strip():
                        break                  

                    
                    
                    temp_quiz = []
                    while True:
                        util.clear_screen()
                        print("=" * 85)
                        print("Quiz Title: ",quiz_title)
                        print("Course: ",courses[course_id].course_name)
                        print("=" * 85)
                        print()

                        
                        
                        print(f"{'ID:':<10} {'Name:':<25} {'Score'}")
                        print("=" * 85)
                        for quiz_id, quiz in quizzes.items():
                            if quiz.quiz_title == quiz_title and quiz.course_id == course_id:
                                print(f"{quiz.student_id:<10} {students[quiz.student_id].name():<25} {quiz.score}")
                        
                    
                        print()

                        student_id = input("Student ID: ")

                        if not student_id.strip():
                            break

                        if student_id not in students:
                            print("Student not found.")
                            input("\nPress Enter to continue...")
                            continue

                        if student_id in temp_quiz:
                            print("Already add score for this student.")
                            input("\nPress Enter to continue...")
                            continue

                        try:
                            score = float(input("Score: "))
                            if score < 0 or score > 100:
                                print("Score must be between 0 and 100.")
                                input("\nPress Enter to continue...")
                                continue
                        except ValueError:
                            print("Invalid score. Please enter a numeric value.")
                            input("\nPress Enter to continue...")
                            continue

                        while True:
                            quiz_id = util.generate_random_id()
                            if not quiz_id in quizzes:
                                quizzes[quiz_id] = Quiz(quiz_id, quiz_title, student_id, course_id, score)
                                temp_quiz.append(student_id)
                                break
                        
                        print(f"Student score for quiz {quiz_title} added successfully.")
                        db.save_quizzes_csv(quizzes)
                        input("\nPress Enter to continue...")
                    
            elif choice == '2':
                util.clear_screen()
                if quizzes:
                    print("Quizzes")
                    print("=" * 85)
                    print(f"{'Title':<15} {'ID':<10} {'Name:':<25} {'Course ID':<15} {'Score'}")
                    print("=" * 85)
                    for quiz_id, quiz in quizzes.items():
                        print(f"{quiz.quiz_title:<15} {students[quiz.student_id].student_id:<10} {students[quiz.student_id].fname +" "+ students[quiz.student_id].lname:<25} {quiz.course_id:<15} {quiz.score}")
                else:
                    print("No quizzes available.")
                input("\nPress Enter to continue...")
            elif choice == '3':
                while True:
                    util.clear_screen()
                    display.course_table_display(courses)
                    print("\nFilter Quizzes by Course [Leave fields blank to cancel]")
                    print("-" * 85)

                    print()
                    
                    course_id = input("Course ID : ")
                    if not course_id.strip():
                        break  

                    if course_id not in courses:
                        print("Course not found.")
                        input("Press Enter to continue...")
                        continue

                    if course_id in courses:
                        while True:
                            util.clear_screen()
                            found = False
                            print(f"\nQuizzes for Course {course_id} - {courses[course_id].course_name} [Leave field blank to cancel]")
                            print()
                            print(f"{'Quiz Title':<15} {'ID':<10} {'Name':<25} {'Score'}")
                            print("=" * 85)
                            available_quiz_title = []
                            has_quiz = False
                            for quiz_id, quiz in quizzes.items():
                                if quiz.course_id == course_id:
                                    print(f"{quiz.quiz_title:<15} {quiz.student_id:<10} {students[quiz.student_id].name():<25} {quiz.score}")
                                    available_quiz_title.append(quiz.quiz_title)
                                    has_quiz = True

                            if not has_quiz:
                                print("No quiz added to this course.")
                                input("\nPress Enter to continue...")
                                break
                            
                            print()
                            selected_quiz_title = input("Quiz title : ")
                            
                            if not selected_quiz_title.strip():
                                break
                            
                            if selected_quiz_title not in available_quiz_title:
                                print("Selected quiz title not found")
                                input("\nPress Enter to continue...")
                                continue

                            threshold = input("Threshold  : ")  

                            if not threshold.strip():
                                threshold = 0
                            else:
                                threshold = int(threshold)
                            
                            util.clear_screen()

                            print(f"{courses[course_id].course_name.upper()}, Quiz: {selected_quiz_title}")
                            if threshold > 0:
                                print(f"Student who got score equal or greater to {threshold}.")

                            print("=" * 85)
                            print(f"{'Quiz Title':<20} {'Student Name':<25} {'Score':<10}")
                            print("=" * 85)
                            
                            for quiz_id, quiz in quizzes.items():
                                if not quiz.score >= threshold:
                                    continue
                                if quiz.course_id == course_id and selected_quiz_title == quiz.quiz_title:
                                    student = students[quiz.student_id]
                                    print(f"{quiz.quiz_title:<20} {student.fname + ' ' + student.lname:<25} {quiz.score:<10}")
                                    found = True
                            

                            if not found:
                                print("No student got the score threshold.")
                                
                            input("\nPress Enter to continue...") 
                    else:
                        print("No data to display.")
                        input("\nPress Enter to continue...")
            elif choice == '4':
                while True:
                    util.clear_screen()
                    display.course_table_display(courses)
                    print("\nCompute Average, Lowest, and Highest Scores by Course [Leave fields blank to exit]")
                    print("-" * 85)
                    course_id = input("Course ID: ")

                    if not course_id.strip():
                        break  

                    if course_id in courses:
                        while True:
                            util.clear_screen()
                            print(f"Computing statistical report for {courses[course_id].course_name} [Leave field blank to cancel]")
                            print()
                            total_score = 0
                            quiz_count = 0
                            lowest_score = float('inf')
                            highest_score = float('-inf')
                            lowest_student = None
                            highest_student = None
                            available_quiz_title = []
                            has_quiz = False
                            print(f"{'Quiz Title':<15} {'ID':<10} {'Name':<25} {'Score'}")
                            print("=" * 85)
                            for quiz_id, quiz in quizzes.items():
                                if quiz.course_id == course_id:
                                    print(f"{quiz.quiz_title:<15} {quiz.student_id:<10} {students[quiz.student_id].name():<25} {quiz.score}")
                                    available_quiz_title.append(quiz.quiz_title)
                                    has_quiz = True

                            if not has_quiz:
                                print("No quiz added to this course.")
                                input("\nPress Enter to continue...")
                                break


                            print()
                            selected_quiz_title = input("Select quiz title: ")

                            if not selected_quiz_title.strip():
                                break
                            
                            if selected_quiz_title not in available_quiz_title:
                                print("Selected quiz title not found")
                                input("\nPress Enter to continue...")
                                continue


                            for quiz in quizzes.values():
                                if quiz.course_id == course_id and quiz.quiz_title == selected_quiz_title:
                                    total_score += quiz.score
                                    quiz_count += 1
                                    if quiz.score < lowest_score:
                                        lowest_score = quiz.score
                                        lowest_student = quiz.student_id
                                    if quiz.score > highest_score:
                                        highest_score = quiz.score
                                        highest_student = quiz.student_id

                            if quiz_count > 0:
                                average_score = total_score / quiz_count
                                print(f"\nStatistics for course {course_id} ({courses[course_id].course_name}) quiz {selected_quiz_title}\n")
                                print(f"Average Score: {average_score:.2f}")
                                print(f"Lowest Score : {lowest_score:.2f} ({students[lowest_student].name()})")
                                print(f"Highest Score: {highest_score:.2f} ({students[highest_student].name()})")
                            else:
                                print(f"No quizzes found for course {course_id}.")
                                
                            input("\nPress Enter to continue...")
                    else:
                        print("No data to display.")
                        input("\nPress Enter to continue...")
            elif choice == '5':
                return

def __init__():
    '''print("Initializing the Student Management System...")


    # Add dummy students
    s1 = Student("1111", "John", "Doe", "Tagbilaran City")
    s2 = Student("2222", "Jane", "Smith", "Calapen City")
    s3 = Student("3333", "Odette", "Johnson", "Clarin City")
    s4 = Student("4444", "Ruby", "Roger", "Tubigon City")
    s5 = Student("5555", "Juan", "Dela Cruz", "Loon City")

    students[s1.student_id] = s1
    students[s2.student_id] = s2
    students[s3.student_id] = s3
    students[s4.student_id] = s4
    students[s5.student_id] = s5


    # Add dummy courses
    c1 = Course("CS101", "Mathematics", "Dr. Wakwak")
    c2 = Course("CS102", "Science", "Prof. Proton")
    c3 = Course("CS103", "History", "Dr. Time")
    c4 = Course("CS104", "Art", "Ms. Canvas")
    courses[c1.course_id] = c1
    courses[c2.course_id] = c2
    courses[c3.course_id] = c3
    courses[c4.course_id] = c4

    # Add dummy enrollments
    e1 = Enrollment(s1.student_id, ["CS101", "CS102", "CS103"])
    e2 = Enrollment(s2.student_id, ["CS101", "CS104"])
    e3 = Enrollment(s3.student_id, ["CS102", "CS103", "CS104"])
    enrolled[s1.student_id] = e1
    enrolled[s2.student_id] = e2
    enrolled[s3.student_id] = e3

    q1 = Quiz(generate_random_id(), "Q1", s1.student_id, c1.course_id, 85)
    q2 = Quiz(generate_random_id(), "Q1", s2.student_id, c1.course_id, 90)
    q3 = Quiz(generate_random_id(), "Q1", s3.student_id, c1.course_id, 75)
    q4 = Quiz(generate_random_id(), "Q1", s1.student_id, c2.course_id, 80)
    q5 = Quiz(generate_random_id(), "Q1", s2.student_id, c2.course_id, 87)
    q6 = Quiz(generate_random_id(), "Q1", s3.student_id, c2.course_id, 90)
    q7 = Quiz(generate_random_id(), "Q1", s1.student_id, c3.course_id, 77)
    q8 = Quiz(generate_random_id(), "Q1", s2.student_id, c3.course_id, 88)
    q9 = Quiz(generate_random_id(), "Q1", s3.student_id, c3.course_id, 99)


    quizzes[q1.quiz_id] = q1
    quizzes[q2.quiz_id] = q2
    quizzes[q3.quiz_id] = q3
    quizzes[q4.quiz_id] = q4
    quizzes[q5.quiz_id] = q5
    quizzes[q6.quiz_id] = q6
    quizzes[q7.quiz_id] = q7
    quizzes[q8.quiz_id] = q8
    quizzes[q9.quiz_id] = q9
    '''


    
    db.load_csv(students, courses, enrolled, quizzes, Student, Course, Enrollment, Quiz )
    main_menu()


__init__()