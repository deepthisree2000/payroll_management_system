# importing libraries
import sqlite3
# creating the connection
conn=sqlite3.connect('PMS.db')
# creating cursor for sql queries
cur = conn.cursor()

#cur.execute(f"CREATE TABLE employee_details(eid int primary key , ename varchar(45), dptid int , designation varchar(45), emailid varchar(45), contact_no longint ,address varchar(50))")
#cur.execute(f"CREATE TABLE salary_details( eid int,dptid int primary key ,account_number int,PAN varchar(15),Base_salary int,FOREIGN KEY (eid) REFERENCES employee_details(eid))")
#cur.execute(f"CREATE TABLE attendance(dptid int,dpt_name varchar(25),eid int,ename varchar(45),date datetime,time_in datetime,time_out datetime,FOREIGN KEY (eid) REFERENCES employee_details(eid),FOREIGN KEY (dptid) REFERENCES salary_details(dptid))")
cur.execute("select * from employee_details")
#print(cur.fetchall())
data = []
for i in cur.fetchall():
    context = {}
    context['eid']=i[0]
    context['ename']=i[1]
    context['dptid']=i[2]
    context['designation']=i[3]
    context['emailid']=i[4]
    context['contact_no']=i[5]
    context['address']=i[6]
    data.append(context)
print(data)

from employee_details import employee

emp = employee()
emp.attendance(dptid=11,dpt_name='Accounts',eid=1,ename='Bhuvan',date='18-07-2023',time_in='8:00',time_out='18:00')


conn.commit()
conn.close()