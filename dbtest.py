# importing libraries
import sqlite3
# creating the connection
conn=sqlite3.connect('PMS.db')
# creating cursor for sql queries
cur = conn.cursor()

#cur.execute(f"CREATE TABLE employee_details(eid int primary key , ename varchar(45), dptid int , designation varchar(45), emailid varchar(45), contact_no longint ,address varchar(50))")
#cur.execute(f"CREATE TABLE salary_details( eid int,dptid int primary key ,account_number int,PAN varchar(15),Base_salary int,FOREIGN KEY (eid) REFERENCES employee_details(eid))")
#cur.execute(f"CREATE TABLE attendance(dptid int,dpt_name varchar(25),eid int,ename varchar(45),date datetime,time_in datetime,time_out datetime,FOREIGN KEY (eid) REFERENCES employee_details(eid),FOREIGN KEY (dptid) REFERENCES salary_details(dptid))")
#print(cur.fetchall())

#cur.execute(f"delete from employee_details")
#cur.execute(f"delete from attendance")
#cur.execute(f"delete from salary_details")
#conn.commit()
#conn.close()

from employee_details import salarycalculator
sc =salarycalculator()
sc.salarycalculation(eid=1)