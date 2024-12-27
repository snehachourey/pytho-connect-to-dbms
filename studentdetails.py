import mysql.connector
import sys

mydb = mysql.connector.connect(host="localhost", username="root", password="root", database="studentdetails")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS studentin (name VARCHAR(20), surname VARCHAR(20), rollno VARCHAR(10))")
print("STUDENT INFORMATION SYSTEM")

def newstudent():
    query = "INSERT INTO studentin (name, surname, rollno) VALUES (%s, %s, %s)"
    name = input("Enter Your Name: ")
    surname = input("Enter Your Surname: ")
    rollnumber = input("Enter Your Rollnumber: ")
    values = (name, surname, rollnumber)
    mycursor.execute(query, values)
    mydb.commit()
    print("Student Added Successfully")

def Showstudent():
    query = "SELECT * FROM studentin"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    for i in mydata:
        print(i)

def ShowByname():
    query = "SELECT * FROM studentin WHERE name = %s"
    name = input("ENTER NAME OF STUDENT: ")
    value = (name,)
    mycursor.execute(query, value)
    mydata = mycursor.fetchall()
    if mydata:
        for i in mydata:
            print(i)
    else:
        print("No student found with that name")

def ShowBySurname():
    query = "SELECT * FROM studentin WHERE surname = %s"
    surname = input("ENTER SURNAME OF STUDENT: ")
    value = (surname,)
    mycursor.execute(query, value)
    mydata = mycursor.fetchall()
    for i in mydata:
        print(i)

def ShowByRollNumber():
    query = "SELECT * FROM studentin WHERE rollno = %s"
    rollno = input("ENTER ROLL NUMBER OF STUDENT: ")
    value = (rollno,)
    mycursor.execute(query, value)
    mydata = mycursor.fetchall()
    if mydata:
        for i in mydata:
            print(i)
    else:
        print("No student found with that roll number")

def UpdateStudent():
    query = "UPDATE studentin SET name = %s, surname = %s, rollno = %s WHERE rollno = %s"
    rollno = input("Enter Rollnumber of the student to update: ")
    new_name = input("Enter new name: ")
    new_surname = input("Enter new surname: ")
    new_rollno = input("Enter new rollnumber: ")
    values = (new_name, new_surname, new_rollno, rollno)
    mycursor.execute(query, values)
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Student details updated successfully")
    else:
        print("No student found with that rollnumber")

def DeleteStudent():
    query = "DELETE FROM studentin WHERE rollno = %s"
    rollno = input("Enter Rollnumber of the student to delete: ")
    value = (rollno,)
    mycursor.execute(query, value)
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Student deleted successfully")
    else:
        print("No student found with that rollnumber")

print("\nCHOOSE ANY ONE OPTION")
print("1. ADD NEW STUDENT")
print("2. SHOW ALL STUDENTS")
print("3. SHOW STUDENTS BY NAME")
print("4. SHOW STUDENTS BY SURNAME")
print("5. SHOW STUDENTS BY ROLL NUMBER")
print("6. UPDATE STUDENT DETAILS")
print("7. DELETE STUDENT")
print("8. EXIT")

opt = int(input("ENTER ANY OPTION: "))

if opt == 1:
    newstudent()
elif opt == 2:
    Showstudent()
elif opt == 3:
    ShowByname()
elif opt == 4:
    ShowBySurname()
elif opt == 5:
    ShowByRollNumber()
elif opt == 6:
    UpdateStudent()
elif opt == 7:
    DeleteStudent()
elif opt == 8:
    print("Exiting the program.")
    sys.exit()  # Properly terminate the program
else:
    print("Invalid Option")
