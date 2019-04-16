# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:26:53 2018

@author: your name here
"""
import dbinterface

menuString = """
Main Menu:
1.  Administrator
2.  Professor
3.  Student
4.  TA 
0.  Exit
"""
adminString = """
Administrator Menu:
    1. View Student 
    2. Delete Student 
    3. Update Student's Advisor 
    4. View Professor
    5. Delete Professor 
    6. Update Professor's Office Number 
    7. Update Course 
    8. View Course 
    9. Delete Course 
    10. View Lab Schedule 
    11. Update Lab Schedule 
    0. Exit
"""
profString = """
Professor Menu:
    1. View Student details as a Class Roster 
    2. Upate Student's Clicker 
    3. Update/Add grade 
    4. View Lab SChedule 
    0. Exit
"""
studentString = """
Student Menu:
    1. View Student 
    2. View Professor 
    3. View Lab Schedule 
    0. Exit
"""
taString = """
TA Menu:
    1. View Lab Schedule 
    2. Update Room Lab Schedule 
    0. Exit
"""
def adminfunction():
    while True:
        print(adminString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            dbinterface.viewStudent()
        elif (sel == 2):
            dbinterface.deleteStudent()
        elif (sel == 3):
            dbinterface.updateAdvisor()
        elif (sel == 4):
            dbinterface.viewProf()
        elif (sel == 5):
            dbinterface.deleteProfessor()
        elif (sel == 6):
            dbinterface.updateOfficeNum()
        elif (sel == 7):
            dbinterface.updateCourse()
        elif (sel == 8):
            dbinterface.viewCourse()
        elif (sel == 9):
            dbinterface.deleteCourse()
        elif (sel == 10):
            dbinterface.viewLabSchedule()
        elif (sel == 11):
            dbinterface.updateLabSchedule()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
    
def proffunction():
    while True:
        print(profString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            dbinterface.viewStudentDetails()
        elif (sel == 2):
            dbinterface.updateStudentClicker()
        elif (sel == 3):
            dbinterface.updateGrade()
        elif (sel == 4):
            dbinterface.viewLabSchedule()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")

def studentfunction():
    while True:
        print(studentString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            dbinterface.viewStudent()
        elif (sel == 2):
            dbinterface.viewProf()
        elif (sel == 3):
            dbinterface.viewLabSchedule()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")

def tafunction():
    while True:
        print(taString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            dbinterface.viewLabSchedule()
        elif (sel == 2):
            dbinterface.updateRoom()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
            
            
#def searchsubFunction():
#    dbinterface.searchCustomers()
    


def main():

    while True:
        print(menuString)
        sel = int(input("Menu Option >> "))
        if(sel == 1):
            adminfunction()
        elif(sel == 2):
            proffunction()
        elif(sel == 3):
            studentfunction()
        elif(sel == 4):
            tafunction()
        elif(sel == 0):
            # Exits the program
            break
        else:
            print("Unrecognized Command")
   
    
# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()