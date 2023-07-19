# importing libraries
import sqlite3
# creating the connection


class employee:
    def empinsert(self,**k):
        conn=sqlite3.connect('PMS.db')
        # creating cursor for sql queries
        cur = conn.cursor()
        cur.execute(f'''insert into employee_details values
                    ({k['eid']},"{k['ename']}",
                    {k['dptid']},"{k['designation']}","{k['emailid']}",{k['contact_no']},
                    "{k['address']}")''')
        conn.commit()
        print("Data has been inserted successfully")
    def show_employees(self):
        conn = sqlite3.connect('PMS.db')
        cur = conn.cursor()
        cur.execute("select * from employee_details")
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
        return data
    def attendance(self,**k):
        conn=sqlite3.connect('PMS.db')
        # creating cursor for sql queries
        cur = conn.cursor()
        cur.execute(f'''insert into attendance values
                    ({k['dptid']},"{k['dpt_name']}",
                    {k['eid']},"{k['ename']}","{k['date']}","{k['time_in']}",
                    "{k['time_out']}")''')
        conn.commit()
        print("Data has been inserted successfully")
    def salary_details(self,**k):
        conn=sqlite3.connect('PMS.db')
        cur = conn.cursor()
        cur.execute(f'''insert into salary_details values
                    ({k['eid']},{k['dptid']},
                    {k['account_number']},"{k['PAN']}",{k['Base_salary']})''')
        conn.commit()
        print("Data has been inserted successfully")