import mysql.connector

mysqle=mysql.connector.connect(host="localhost",user="root",password="fuck2O2O",db ="student_db")
cur=mysqle.cursor()

def register(tuples):
    cur.execute("INSERT INTO userlogin(name, email, username, password) VALUES (%s, %s, %s, %s)",tuples)
    mysqle.commit()
    
def login(username):
    result = cur.execute("SELECT * FROM userlogin WHERE username = %s", [username])
    return cur.fetchall()

def collegelist(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    elif dashboard == "dept":
        cur.execute("SELECT * FROM department")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

#Student DB  
def read(dashboard):
    if dashboard == "stud":
        cur.execute("SELECT * FROM students")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    elif dashboard == "dept":
        cur.execute("SELECT * FROM department")
    else:
        cur.execute("SELECT * FROM college")
    return cur.fetchall()

def delete(id):
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    mysqle.commit()

def edit(tuples):
    cur.execute("UPDATE students SET id=%s, idno=%s, firstname=%s, lastname=%s, gender=%s, year=%s, course=%s, department=%s, college=%s where id=%s",tuples)
    mysqle.commit()

def addStudent(tuples):
    for i in tuples:
        print(i)
    cur.execute("INSERT INTO students(idno, firstname, lastname, gender, year, course, department, college) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",tuples)
    mysqle.commit()

#College DB 
def readCollege(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    elif dashboard == "dept":
        cur.execute("SELECT * FROM department")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCollege(college_code):
    cur.execute("DELETE FROM college WHERE college_code = %s", [college_code])
    mysqle.commit()

def editCollege(tuples):
    cur.execute("UPDATE college SET college_code=%s, college_name=%s where college_code=%s",tuples)
    mysqle.commit()

def addCollege(tuples):
    cur.execute("INSERT INTO college(college_code, college_name) VALUES(%s, %s)",tuples)
    mysqle.commit()

#Department DB
def readDepartment(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    elif dashboard == "dept":
        cur.execute("SELECT * FROM department")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteDepartments(department_name):
    cur.execute("DELETE FROM department WHERE department_name = %s", [department_name])
    mysqle.commit()

def editDepartments(tuples):
    cur.execute("UPDATE department SET department_name=%s, college_code=%s where department_name=%s",tuples)
    mysqle.commit()

def addDepartment(tuples):
    cur.execute("INSERT INTO department(department_name, college_code) VALUES(%s, %s)",tuples)
    mysqle.commit()

#Courses DB
def readCourse(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    elif dashboard == "dept":
        cur.execute("SELECT * FROM department")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCourse(course_code):
    cur.execute("DELETE FROM course WHERE course_code = %s", [course_code])
    mysqle.commit()

def editCourse(tuples):
    cur.execute("UPDATE course SET course_code=%s, course_name=%s, college_code=%s, department_name=%s where course_code=%s",tuples)
    mysqle.commit()

def addCourse(tuples):
    cur.execute("INSERT INTO course(course_code,course_name,college_code,department_name) VALUES(%s, %s, %s, %s)",tuples)
    mysqle.commit()
