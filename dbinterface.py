

# Database User Interface
#
# Note that these functions contain input and output
# such as print() and input(), but do NOT contain any 
# actual database code. The database is handled by 
# a separate class.


from musicdb import MusicDB

# Create a database object that will handle all the DB stuff.
dbobj = MusicDB()

def viewStudent():
    name = input("Enter the student ID: ")
    result = dbobj.viewStudent(name)
    for row in result:
        print(row)
        
def updateAdvisor():
    name = input("Enter the student ID: ")
    advisorID = input("Enter the new advisor ID: ")
    dbobj.updateStudentAdvisor(name, advisorID)
    print()
    
def viewProf():
    cur = dbobj.viewProf()
    result = cur.fetchall()
    for row in result:
        print(row)
        
def updateOfficeNum():
    idNum = input("Enter the professor ID: ")
    officenum = input("Enter the new office number: ")
    dbobj.updateProfOfficeNum(idNum, officenum)
    print()
    
def updateCourse():
    courseID = input("Enter the Course ID: ")
    newProf = input("Enter the new professor ID: ")
    dbobj.updateCourse(courseID, newProf)
    print()
    
def viewCourse():
    name = input("Enter the course ID: ")
    result = dbobj.viewCourse(name)    
    for row in result:
        print(row)
        
def viewLabSchedule():
    courseID = input("Enter course ID: ")
    semester = input("Enter the semester: ")
    year = input ("Enter the year: ")
    result = dbobj.viewLabSchedule(courseID, semester, year)
    for row in result:
        print(row)
        
def updateLabSchedule():
    courseID = input("Enter the courseID: ")
    semester = input("Enter the semester: ")
    year = input("Enter the year: ")
    day = input("Enter the day: ")
    time = input("Enter the time: ")
    roomNum = input("Enter the room number: ")
    newDay = input("Enter the new day: ")
    newTime = input("Enter the new time: ")
    check = dbobj.selectIf(semester, year, newDay, newTime, roomNum)
    if (check < 1):
        result = dbobj.updateLabSchedule(newDay, newTime, courseID, semester, year, day, time, roomNum)
        for row in result:
            print(row)
    else:
        print("There is another class at that time")
        
def viewStudentDetails():
    courseID = input("Enter the Course ID: ")
    result = dbobj.viewStudentDetails(courseID)
    for row in result:
        print(row)
        
def updateStudentClicker():
    clickerID = input("Enter the new clicker ID: ")
    studentID = input("Enter the studentID: ")
    dbobj.updateClicker(clickerID, studentID)
    print()
        
def updateGrade():
    courseID = input("Enter the course ID: ")
    studentID = input("Enter the Student ID: ")
    grade = input("Enter the new grade: ")
    dbobj.addGrade(grade, studentID, courseID)
    print()

def viewallProf():
    lastName = input("Enter the professor's last name: ")
    dbobj.viewAllProf(lastName)
    print()
        
def updateRoom():
    courseID = input("Enter the course ID: ")
    semester = input("Enter the semester: ")
    year = input("Enter the year: ")
    day = input("Enter the day: ")
    roomNum = input("Enter the new room number: ")
    dbobj.updateRoomLab(roomNum, courseID, semester, year, day)
    print()
        
def deleteStudent():
    clarkID = input("Enter studnet ID of the student you want to delete: ")
    dbobj.deleteStudent(clarkID)
    print()
    
def deleteProfessor():
    clarkID = input("Enter the clark ID of the professor you want to delete: ")
    dbobj.deleteProf(clarkID)
    print()
    
def deleteCourse():
    courseID = input("Enter the course ID of the course you want to delete: ")
    dbobj.deleteCourse(courseID)
    print()
     
     
     
    
     
     
    