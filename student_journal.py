# from email import message
# import email
# from json import load
from tkinter import N, S
from students import Student, Athelete, Artist
import re
import logging

def main():
    welcome = "Welcome to the school system's student log!\n\n"
    logging.basicConfig(filename="Student_journal.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    print(welcome.upper())


    file_name = "students.csv"
    list_students = []
    list_students = load_students(file_name)                       # Loading..
    logging.info("Loading students into list_students list...")


    while True:
        student = insert_student()                                  # Inserting..
        if student == None:
            break
        logging.info("Inserting a new student...")
        list_students.append(student)
        print("All students in the school system")
        for studt in list_students:
            print(studt)


        save_students(file_name, list_students)                     # Saving..
        logging.info("Saved students to " + file_name)
        print("\n\n")


   # This function look for the file name and save the list of students into this csv file.      
def save_students(file_name, list_students):
    with open(file_name, "w") as fn:
        for student in list_students:
          if type(student) == Athelete:
             fn.write("Athelete," + student.full_name + "," + str(student.email) + "," + str(student.start_year) + ",\n")
          elif type(student) == Artist:
                fn.write("Artist," + student.full_lname + "," + str(student.email) + "," + str(student.start_year) + ",\n")
          else:
                pass

   # This function will look for a file name and return students into student list. 
def load_students(file_name):
     list_students = []
     with open(file_name, "r") as ff:
        for line in ff:
            info = line.split(',')
            if info[0] == "Athelete":
                Student = Athelete(info[1], info[2], info[3])
            elif info[0] == "Artist":
                Student = Artist(info[1], info[2], info[3])
            else:
                Student = None

            if Student != None:
                list_students.append(Student)

     return list_students



def insert_student() -> Student:
    print("\nPlease select the student type you want to register into the journal:")
    print("\tA) Athelete")
    print("\tB) Artist")
    print("\tC) Exit")
    # while true
    student_type = input("<<<||>>>").upper()

    # Break out of function if user wants to quit
    if student_type == "C":
        return None
        # while loop ends 

    while True:
        try:
            name = input("\nEnter student's name:\n>>>")
            check = re.search(',', name)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nCANNOT HAVE COMMAS IN NAME!\n")
            logging.error("Tried to enter a comma for name, trying again...")
        else:
            break

    while True:
        try:
           start_year = int(input("\nEnter student's age:\n>>>"))
        except ValueError as ve:
            print("\nCANNOT ENTER A STRING FOR YEAR! PLEASE ENTER AN INTEGER!\n")
            logging.error("Tried to enter a string for year, trying again...")
        else:
            break

    while True:   
        try:
            email = input("\nEnter student's email:\n>>>")
            check = re.search(',', email)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print(f"\nCANNOT HAVE COMMAS IN EMAIL!\n")
            logging.error(f"Tried to enter a comma for email, trying again...")
        else:
            break

    if student_type == "A":
        student = Athelete(name, email, start_year)
    elif student_type == "B":
        student = Artist(name, email, start_year)
    else:
        student = None

    return student


if __name__ == "__main__":
    main()