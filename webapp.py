from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
import s_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Programs Offered
@app.route('/programs')
def programs():
    return render_template('programs.html')

# College/Course Page
@app.route('/collegelist')
def collegelist():
    return render_template('collegelist.html', college=s_db.collegelist("coll"),course=s_db.collegelist("crs"),department=s_db.collegelist("dept"))

# Department Page
@app.route('/deptlist')
def deptlist():
    return render_template('deptlist.html', college=s_db.collegelist("coll"),course=s_db.collegelist("crs"),department=s_db.collegelist("dept"))

# Second Department Page
@app.route('/deptlistsec')
def deptlistsec():
    return render_template('deptlistsec.html', college=s_db.collegelist("coll"),course=s_db.collegelist("crs"),department=s_db.collegelist("dept"))
    
# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=7, max=50)])
    username = StringField('Username', [validators.Length(min=7, max=25)])
    email = StringField('Email', [validators.Length(min=7, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        tuples=(name,email,username,password) 
        s_db.register(tuples)
        flash('You are now registered and can log in', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        result = s_db.login(username)
        if len(result) > 0:
            # Get stored hash
            password=result[0][4]
            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard/Search
@app.route ('/dashboard')
@app.route ('/search_student', methods = ['POST', 'GET'])
def dashboard():
    data=s_db.read("stud")
    if request.method == 'POST':
        newdata = []
        for y in data:
            for z in y:
                if z == request.form['searchbar']:
                    newdata.append (y)
                    break
        data = newdata
    return render_template('dashboard.html', students=data,college=s_db.read("asasdsda"),course=s_db.read("crs"),department=s_db.read("dept"))
 
# Edit Student
@app.route('/edit_student', methods = ['POST','GET'])
def edit_student():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        Id = request.form['Id']
        idno = request.form['idno']
        firstname = request.form['firstname']
        gender = request.form['gender']
        lastname = request.form['lastname']
        year = request.form['year']
        course = request.form.get('course') 
        s_db.cur.execute("select * from course where course_code = %s",(course,))
        department=s_db.cur.fetchall()
        s_db.cur.execute("select * from department where department_name = %s",(department[0][3],))
        department=s_db.cur.fetchall()
        s_db.cur.execute("select * from college where college_code = %s",(department[0][1],))
        college=s_db.cur.fetchall()
        tuples=(Id,idno,firstname,lastname,gender,year,course,department[0][0],college[0][0],Id)  
        s_db.edit(tuples)
    return redirect(url_for('dashboard'))

# Delete Student
@app.route('/delete_student/<string:id>', methods=['POST','GET'])
def delete_student(id):
    s_db.delete(id)
    flash('Student Deleted', 'success')
    return redirect(url_for('dashboard'))

# Add Student
@app.route('/add_student', methods=['POST','GET'])
def add_student():
    if request.method == 'POST':
        flash('Student Data Created', 'success')
        idno = request.form['idno']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        year = request.form['year']
        course = request.form['course']
        s_db.cur.execute("select * from course where course_code = %s",(course,))
        department=s_db.cur.fetchall()
        s_db.cur.execute("select * from department where department_name = %s",(department[0][3],))
        department=s_db.cur.fetchall()
        s_db.cur.execute("select * from college where college_code = %s",(department[0][1],))
        college=s_db.cur.fetchall()
        tuples=(idno,firstname,lastname,gender,year,course,department[0][0],college[0][0]) 
        s_db.addStudent(tuples)
    return redirect(url_for('dashboard'))

# Colleges/Search
@app.route('/colleges')
@app.route ('/search_college', methods = ['POST', 'GET'])
def colleges():
    data=s_db.readCollege("coll")
    if request.method == 'POST':
        newdata = []
        for y in data:
            for z in y:
                if z == request.form['searchbar']:
                    newdata.append (y)
                    break
        data = newdata
    return render_template('colleges.html', college=data,student=s_db.read("asasdsda"),course=s_db.read("crs"),department=s_db.read("dept"))

# Delete College
@app.route('/delete_college/<string:college_code>', methods=['POST','GET'])
def delete_college(college_code):
    s_db.deleteCollege(college_code)
    flash('College Deleted', 'success')
    return redirect(url_for('colleges'))

# Edit College
@app.route('/edit_college', methods = ['POST','GET'])
def edit_college():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        college_code_old = request.form['college_code_old']
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        tuples=(college_code,college_name,college_code_old)
        s_db.editCollege(tuples)
    return redirect(url_for('colleges'))

# Add College
@app.route('/add_college', methods=['POST','GET'])
def add_college():
    if request.method == 'POST':
        flash('College Data Created', 'success')
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        tuples=(college_code,college_name) 
        s_db.addCollege(tuples)
    return redirect(url_for('colleges'))

# Departments/Search
@app.route('/departments')
@app.route ('/search_department', methods = ['POST', 'GET'])
def departments():
    data=s_db.readDepartment("dept")
    if request.method == 'POST':
        newdata = []
        for y in data:
            for z in y:
                if z == request.form['searchbar']:
                    newdata.append (y)
                    break
        data = newdata
    return render_template('departments.html', department=data,student=s_db.read("asasdsda"),course=s_db.read("crs"),college=s_db.read("coll"))

# Delete Departments
@app.route('/delete_departments/<string:department_name>', methods=['POST','GET'])
def delete_departments(department_name):
    s_db.deleteDepartments(department_name)
    flash('Department Deleted', 'success')
    return redirect(url_for('departments'))  

# Edit Departments
@app.route('/edit_departments', methods = ['POST','GET'])
def edit_departments():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        department_name_old = request.form.get('department_name_old')
        department_name = request.form['department_name']
        college_code = request.form.get('college_code')
        tuples=(department_name,college_code,department_name_old)
        s_db.editDepartments(tuples)
    return redirect(url_for('departments'))

# Add Departments
@app.route('/add_department', methods=['POST','GET'])
def add_department():
    if request.method == 'POST':
        flash('Department Data Created', 'success')
        department_name = request.form['department_name']
        college_code = request.form['college_code']  
        tuples=(department_name,college_code) 
        s_db.addDepartment(tuples)
    return redirect(url_for('departments'))

# Courses/Search
@app.route('/courses')
@app.route ('/search_courses', methods = ['POST', 'GET'])
def courses():
    data=s_db.readCourse("crs")
    if request.method == 'POST':
        newdata = []
        for y in data:
            for z in y:
                if z == request.form['searchbar']:
                    newdata.append (y)
                    break
        data = newdata
    return render_template('courses.html', course=data,student=s_db.read("stud"),department=s_db.read("dept"),college=s_db.read("coll"))

# Delete Courses
@app.route('/delete_courses/<string:course_code>', methods=['POST','GET'])
def delete_courses(course_code):
    s_db.deleteCourse(course_code)
    flash('Course Deleted', 'success')
    return redirect(url_for('courses')) 

# Edit Courses
@app.route('/edit_courses', methods = ['POST','GET'])
def edit_courses():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        course_code_old = request.form['course_code_old']
        course_code = request.form['course_code']
        course_name = request.form['course_name'] 
        department_name = request.form['department_name']
        college_code = request.form.get('college_code')
        s_db.cur.execute("select * from department where department_name = %s",(department_name,))
        department=s_db.cur.fetchall() 
        s_db.cur.execute("select * from college where college_code = %s",(department[0][1],))
        college_code=s_db.cur.fetchall()
        tuples=(course_code,course_name,college_code[0][0],department_name,course_code_old) 
        s_db.editCourse(tuples)
    return redirect(url_for('courses'))

# Add Departments
@app.route('/add_courses', methods=['POST','GET'])
def add_courses():
    if request.method == 'POST':
        flash('Course Data Created', 'success')
        course_code = request.form['course_code']
        course_name = request.form['course_name'] 
        department_name = request.form['department_name']
        college_code = request.form.get('college_code')
        s_db.cur.execute("select * from department where department_name = %s",(department_name,))
        department=s_db.cur.fetchall() 
        s_db.cur.execute("select * from college where college_code = %s",(department[0][1],))
        college_code=s_db.cur.fetchall()
        tuples=(course_code,course_name,college_code[0][0],department_name) 
        s_db.addCourse(tuples)
    return redirect(url_for('courses'))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
