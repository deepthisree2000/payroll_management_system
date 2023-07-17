# importing libraries
import sqlite3
# creating the connection
conn=sqlite3.connect('PMS.db')
# creating cursor for sql queries
cur = conn.cursor()

class employee:
    def empinsert(self,**k):
        cur.execute(f'''insert into employee_details values
                    ({k['eid']},"{k['ename']}",
                    {k['dptid']},"{k['designation']}","{k['emailid']}",{k['contact_no']},
                    "{k['address']}")''')
        conn.commit()
        print("Data has been inserted successfully")