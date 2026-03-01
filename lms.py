import json

# ---------------------------
# Student Class
# ---------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

# ---------------------------
# Course Class
# ---------------------------
class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title

# ---------------------------
# LMS System Class
# ---------------------------
class LMS:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = {}

    # Add student
    def add_student(self, student_id, name):
        self.students[student_id] = Student(student_id, name)
        print("✅ Student added")

    # Add course
    def add_course(self, course_id, title):
        self.courses[course_id] = Course(course_id, title)
        print("✅ Course added")

    # Enroll student
    def enroll_student(self, student_id, course_id):
        if student_id not in self.students:
            print("❌ Student not found")
            return

        if course_id not in self.courses:
            print("❌ Course not found")
            return

        self.enrollments.setdefault(student_id, []).append(course_id)
        print("✅ Enrollment successful")

    # View enrollments
    def view_enrollments(self):
        for student_id, courses in self.enrollments.items():
            student_name = self.students[student_id].name
            print(f"\n{student_name} enrolled in:")
            for course_id in courses:
                print(" -", self.courses[course_id].title)

    # Save data to file
    def save_data(self):
        data = {
            "students": {sid: s.name for sid, s in self.students.items()},
            "courses": {cid: c.title for cid, c in self.courses.items()},
            "enrollments": self.enrollments
        }
        try:
            with open("lms_data.json", "w") as f:
                json.dump(data, f)
            print("💾 Data saved")
        except Exception as e:
            print("Error saving data:", e)

    # Load data from file
    def load_data(self):
        try:
            with open("lms_data.json", "r") as f:
                data = json.load(f)

            for sid, name in data["students"].items():
                self.students[sid] = Student(sid, name)

            for cid, title in data["courses"].items():
                self.courses[cid] = Course(cid, title)

            self.enrollments = data["enrollments"]
            print("📂 Data loaded")

        except FileNotFoundError:
            print("No previous data found")
        except Exception as e:
            print("Error loading data:", e)

# ---------------------------
# Menu System
# ---------------------------
def main():
    lms = LMS()
    lms.load_data()

    while True:
        print("\n===== LMS MENU =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student")
        print("4. View Enrollments")
        print("5. Save & Exit")

        choice = input("Choose: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            lms.add_student(sid, name)

        elif choice == "2":
            cid = input("Course ID: ")
            title = input("Course Title: ")
            lms.add_course(cid, title)

        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            lms.enroll_student(sid, cid)

        elif choice == "4":
            lms.view_enrollments()

        elif choice == "5":
            lms.save_data()
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()