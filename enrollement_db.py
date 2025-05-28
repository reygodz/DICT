import csv

def load_csv(students, courses, enrolled, quizzes, Student, Course, Enrollment, Quiz):
    #global students, courses, enrolled, quizzes
    try:
        # Load students
        with open('students.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row['student_id']] = Student(row['student_id'], row['fname'], row['lname'], row['address'])

        # Load courses
        with open('courses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses[row['course_id']] = Course(row['course_id'], row['course_name'], row['instructor'])

        # Load enrollments
        with open('enrolled.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                enrolled[row['student_id']] = Enrollment(row['student_id'], row['course_ids'].split(','))

        # Load quizzes
        with open('quizzes.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                quizzes[row['quiz_id']] = Quiz(row['quiz_id'], row['quiz_title'], row['student_id'], row['course_id'], float(row['score']))
    except FileNotFoundError:
        print("Some CSV files are missing. Starting with empty data.")

def save_student_csv(students):
    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['student_id', 'fname', 'lname', 'address'])
        for student in students.values():
            writer.writerow([student.student_id, student.fname, student.lname, student.address])

def save_course_csv(courses):
    with open('courses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['course_id', 'course_name', 'instructor'])
        for course in courses.values():
            writer.writerow([course.course_id, course.course_name, course.instructor])

def save_enrolled_csv(enrolled):
    with open('enrolled.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['student_id', 'course_ids'])
        for enrollment in enrolled.values():
            writer.writerow([enrollment.student_id, ','.join(enrollment.course_ids)])

def save_quizzes_csv(quizzes):
    with open('quizzes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['quiz_id', 'quiz_title', 'student_id', 'course_id', 'score'])
        for quiz in quizzes.values():
            writer.writerow([quiz.quiz_id, quiz.quiz_title, quiz.student_id, quiz.course_id, quiz.score])
    