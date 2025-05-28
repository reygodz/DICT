def specific_student_table_display(student):
    print(f"{'Student ID':<15} {'First Name':<20} {'Last Name':<20} {'Address':<30}")
    print("=" * 85)
    print(f"{student.student_id:<15} {student.fname:<20} {student.lname:<20} {student.address:<30}")

def all_students_table_display(students):
    if students:
        print("\nRegistered Students")
        print("=" * 85)
        print(f"{'Student ID':<15} {'First Name':<20} {'Last Name':<20} {'Address':<30}")
        print("=" * 85)
        for student in students.values():
            print(f"{student.student_id:<15} {student.fname:<20} {student.lname:<20} {student.address:<30}")
    else:
        print("No students registered.")

def specific_course_table_display(course):
    print(f"{'Course ID':<15} {'Course Name':<20} {'Instructor':<20}")
    print("=" * 85)
    print(f"{course.course_id:<15} {course.course_name:<20} {course.instructor:<20}")

def course_table_display(courses, title="Offered Course(s)"):
    if courses:
        print(title.upper())
        print("=" * 85)
        print(f"{'Course ID':<15} {'Course Name':<20} {'Instructor':<20}")
        print("=" * 85)
        for course in courses.values():
            print(f"{course.course_id:<15} {course.course_name:<20} {course.instructor:<20}")

    else:
        print("No courses available.")


def specific_enrolled_table_display(students, student_id, enrollment):
    print("=" * 85)
    print(f"{'ID':<10} {'Name':<25} {'Enrolled Courses'}")
    print("=" * 85)
    print(f"{students[student_id].student_id:<10} {students[student_id].fname +" "+ students[student_id].lname:<25} {', '.join(enrollment.course_ids)}")
    
def enrolled_table_display(enrolled, Enrollment, students, title="Enrolled Students"):
    if enrolled:
        print(title.upper())
        print("=" * 85)
        print(f"{'ID':<10} {'Name':<25} {'Enrolled Courses'}")
        print("=" * 85)

        for student_id, enrollment in enrolled.items():
            if enrollment and isinstance(enrollment, Enrollment):
                print(f"{students[student_id].student_id:<10} {students[student_id].fname +" "+ students[student_id].lname:<25} {', '.join(enrollment.course_ids)}")
    
    else:
        print("No enrollments found.")