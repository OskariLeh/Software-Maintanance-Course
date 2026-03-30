import employee
import sqlite3
from tkinter import*

def test_category():
    root = Tk()
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    emp = employee.employeeClass(root)
    emp.var_name.set("Test employee")
    emp.var_emp_id.set("42")
    emp.add()
    cur.execute("select * from employee where name=?",("Test employee",))
    row=cur.fetchone()
    emp.var_emp_id.set(row[0])
    assert row[1] == "Test employee"

    emp.var_name.set("Test employee")
    emp.delete()
    
    cur.execute("select * from employee where name=?",("Test employee",))
    row=cur.fetchone()
    assert row == None
    cur.close()

