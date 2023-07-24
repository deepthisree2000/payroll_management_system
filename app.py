# importing libraries
from employee_details import employee
from employee_details import salarycalculator
from flask import Flask,render_template,jsonify,request

# creating ojects
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee_signup',methods = ['GET','POST'])
def emp_signup():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        dptid = request.form.get('dptid')
        designation = request.form.get('designation')
        emailid = request.form.get('emailid')
        contact_no = request.form.get('contact_no')
        address = request.form.get('address')
        print(eid,ename,dptid)
        emp = employee()
        emp.empinsert(eid=eid,ename=ename,dptid=dptid,designation=designation,emailid=emailid,contact_no=contact_no,address=address)
        return render_template('message.html')
    else:
        return render_template('signup.html')
@app.route('/employees',methods = ['GET','POST'])
def show_employees():
    emp = employee()
    data = emp.show_employees()
    return render_template('showemployees.html',employees = data)

@app.route('/attendance',methods = ['GET','POST'])
def attendance():
    if request.method=='POST':
        dptid= request.form.get('dptid')
        dpt_name = request.form.get('dpt_name')
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        date= request.form.get('date')
        time_in = request.form.get('time_in')
        time_out = request.form.get('time_out')
        print(eid,ename,dptid)
        emp = employee()
        emp.attendance(dptid=dptid,dpt_name=dpt_name,eid=eid,ename=ename,date=date,time_in=time_in,time_out=time_out)
        return render_template('index.html')
    return render_template('attendance.html')
@app.route('/salary_details',methods = ['GET','POST'])
def salary_details():
    if request.method=='POST':
        eid=request.form.get('eid')
        dptid= request.form.get('dptid')
        account_number=request.form.get('account_number')
        PAN = request.form.get('PAN')
        Base_salary = request.form.get('Base_salary')
        emp = employee()
        emp.salary_details(eid=eid,dptid=dptid,account_number=account_number,PAN=PAN,Base_salary=Base_salary)
        return render_template('message.html')
    return render_template('enter_salary.html')
@app.route('/payroll_release',methods = ['GET','POST'])
def payroll_release():
     if request.method=='POST':
        eid = request.form.get("empid")
        sc = salarycalculator()
        total_salary = sc.salarycalculation(eid = int(eid))
        context = {'EmployeeID':eid,'TotalSalary':int(total_salary)}
        return render_template('showsalary.html',data = context)
     else:
       return render_template('enter_eid.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)

# creating object for class

#calling insert function
#emp.empinsert(eid=1,ename="Bhuvan",dptid=11,designation="Manager",emailid="bhuvan@gmail.com",contact_no=9876543210,address="Mumbai")
