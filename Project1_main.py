# #A project which takes data of student name and Id then marks 
# # stored by them in every subjects, their total, average and pass or fail and report card.


#DISCLIMAR: This program doesnot uses file to add data so, data is not saved permanently. And after 
#each loop data recorded is cleared.

from datetime import date
today = date.today()
while True:
    print("***** WELCOME TO STUDENT MANAGEMENT SYSTEM *****")
    print("Option '1' for recording student data.")
    print("Option '2' for visiting report card of student.")
    print("Option '3' for viewing student data.")
    print("Option '4' for exiting the system.")
    print()

    #student name and id dictionary:
    students = {
        #name of student : id of student
        "David": 1233,
        "Thapa" : 4564
        }

    #student marks according to subject
    student_marks = {
        #name = [math, english, nepali, science, social]
        "David" : [88,87,89,78,90], #passed
        "Thapa" : [8,82,9,5,60]   #failed

    }


    option = int(input("Enter your option: "))

    #recording student data:
    if option == 1:
        name  = input("Enter name of the student: ")
        titled_name = name.title()
        id = int(input(f"Enter 4 digit ID number of student: "))
        print()

        #if student is already in the record:

        if titled_name in students:
            print(f"The student having name {titled_name} and ID no. {id} is already in record!")
            print(f"Enter 1 to update marks of the {titled_name}")
            print("Enter 2 to return to \'MAIN MENU\'")
            press = int(input("Enter option: "))

            #if user wants to udate the marks.
            if press == 1:
                marks  = []
                subjects = ["math", "english", "nepali", "science", "social"]
                print()
                for sub in subjects:
                    m1 = int(input(f"Update the mark of {sub}: "))
                    marks.append(m1)
            
                student_marks.update({titled_name : marks})

                print(f"{titled_name} marks has been updated sucessfully!")
                print()
            else:
                print("ENTERING TO MAIN MENU!.....")
                print()
        
        #if new student is being added: 

        else:
            #updating student name and id to student dictionary
            students.update({titled_name : id})
            print("Now lets add the marks!")
            print()


            #creating marks list and using loop to add vlaues in it, And updating it in student_marks dictionary.
            marks  = []
            subjects = ["math", "english", "nepali", "science", "social"]
            for sub in subjects:
                m1 = int(input(f"Enter the mark of {sub}: "))
                marks.append(m1)
            
            student_marks.update({titled_name : marks})

            print(f"{titled_name} marks added sucessfully!")
            print()

    elif option == 2:
        name  = input("Enter name of the student: ")
        titled_name = name.title()
        if titled_name in students:

            #creating a marks list and assigning its value by extracting it from student_marks dictionary
            marks = student_marks[titled_name]

            total = sum(marks)

            average = total/5

            #defining grade according to marks

            if (average>=90 and average<=100):
                Grade = "A"
            elif (average>=80 and average<=90):
                Grade = "B"
            elif (average>=70 and average<=80):
                Grade = "C"
            elif (average>=60 and average<=70):
                Grade = "D"
            else:
                Grade = "Fail"

            print()
            #Writing seperate letter for PASSED and FAILED ones
            if Grade == "A" or Grade == "B" or Grade == "c" or Grade == "D":
                Letter =f'''****** REPORT CARD*****
    CONGRATULATION! 
Mr/Mrs {titled_name} have sucessfully
Passed with {total} total marks!
And, has acieved "{Grade}" Grade!

Archived Date: {today}
'''

                print(Letter)
                print()
            
            else:
                Letter =f'''****** REPORT CARD*****
        SORRY! 
Mr/Mrs {titled_name} have failed!
with {total} total marks!
BETTER LUCK NEXT TIME!

Archived Date: {today}
'''
                
                print(Letter)
        else:
            print(f"{titled_name} is not in the system! Record him/her! ")
            print()
    
    elif option == 3:
        name  = input("Enter name of the student: ")
        titled_name = name.title()
        id = int(input("Enter 4 digit ID number of studnet: "))
        print()


        #extracting values of each subjects form student_marks dictionary.
        if titled_name in students:
            math = student_marks[titled_name][0]
            english = student_marks[titled_name][0]
            nepali = student_marks[titled_name][0]
            science = student_marks[titled_name][0]
            social = student_marks[titled_name][0]

            letter = f'''***** STUDENT DATA *****
            STUDENT NAME = {titled_name}
            ID NUMBER = {id}\n
            Marks obtained by {titled_name} are:
            Math = {math}
            English = {english}
            Nepali = {nepali}
            Science = {science}
            Social = {social}'''

            print(letter)
            print()
        else:
            print(f"{titled_name} not recorded in the system! Record him/her! ")
            print()

        
    elif option == 4:
        print("EXITING THE SYSTEM..........")
        exit()

    else:
        print("INVALID OPTIOTION! Try Again!")
    


#note: if user add new student and want's view his or her data, it will not show because the 
#data was stored temporarily. And it is lost when loop runs again!



        


