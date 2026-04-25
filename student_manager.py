class StudentManager:
    def __init__(self, file_name="students.txt"):
        self.file_name=file_name

    def add_student(self):
        try:

            name=input("Enter Studetn Name: ")

            if not name.strip():
                print("Name cannot be empty")
                return
            
            with open(self.file_name, "a") as file:
                file.write(name + "\n")
            print(f"Student '{name}' added successfully!")

        except Exception as e:
            print(f"Error{e}")
    
    def view_students(self):
        try:

            with open(self.file_name, "r") as file:
                students=file.readlines()

                if students:
                    print("Students founded")
                    for i, student in enumerate(students, start=1):
                        print(f"{i}. {student.strip()}")

                else:
                    print(f"No students found")
            print("-"*50)

        except FileNotFoundError:
            print("no student record yet! please add student")

        except Exception as e:
            print(f"Error while reading {e}\n")

    def search_student(self):    
        try:

            name = input("Enter Student Name: ") 

            with open(self.file_name, "r") as f:
                students = f.readlines()

                for i, student  in enumerate(students, start= 1):

                    if student.strip() == name:
                        print(f"Student {name} found on position {i}")
                        break

                else:
                    print(f"{name} not found in student file")

        except FileNotFoundError:
            print("File could not found")

        except Exception as e:
            print(f"{e} occured!")

    def delete_student(self):
        try:

            name = input("Enter Student for deleting: ")

            with open(self.file_name, "r") as f:
                students = f.readlines()
            
            with open(self.file_name, "w") as f:
                deleted = False

                for s in students:

                    if s.strip() != name:
                        f.write(s)

                    else:
                        deleted = True

            if deleted:
                print(f"Student '{name}' deleted successfully!")

            else:
                print("Student not found.")

        except FileNotFoundError:
            print("File cound not found!")

        except Exception as e:
            print(f"{e} occured!")

def main():
    manager = StudentManager()

    while True:

        print("-"*50)
        print('Choose an option')
        print('1. Add Student')
        print('2. View Students')
        print('3. Search Student')
        print("4. Delete student")
        print('5. Exit')

        choice = input("\nEnter your choice(1/2/3/4/5): ")

        if choice == '1':
            manager.add_student()

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            manager.search_student()

        elif choice == '4':
            manager.delete_student()

        elif choice == '5':
            print('Exiting program. Goodbye!')
            break

        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main() 