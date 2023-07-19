# importing libraries
from employee_details import employee
from flask import Flask,render_template,jsonify

# creating ojects
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee_signup')
def emp_signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()


emp = employee()

# calling insert function
#emp.empinsert(eid=1,ename="Bhuvan",dptid=11,designation="Manager",emailid="bhuvan@gmail.com",contact_no=9876543210,address="Mumbai")
