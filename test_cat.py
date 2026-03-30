import category
import sqlite3
from tkinter import*

def test_category():
    root = Tk()
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    cat = category.categoryClass(root)
    cat.var_name.set("Test Category")
    cat.add()
    cur.execute("select * from category where name=?",("Test Category",))
    row=cur.fetchone()
    cat.var_cat_id.set(row[0])
    assert row[1] == "Test Category"

    cat.var_name.set("Test Category")
    cat.delete()
    
    cur.execute("select * from category where name=?",("Test Category",))
    row=cur.fetchone()
    assert row == None
    cur.close()

