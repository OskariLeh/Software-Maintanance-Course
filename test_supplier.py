import supplier
import sqlite3
from tkinter import*

def test_supplier():
    root = Tk()
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    sup = supplier.supplierClass(root)
    sup.var_name.set("Test sup")
    sup.var_sup_invoice.set("42")
    sup.var_contact.set("1234567890")
    sup.txt_desc.insert('1.0',"Test description")
    sup.add()

    cur.execute("select * from supplier where invoice=?",("42",))
    row=cur.fetchone()
    assert row[1] == "Test sup"
    sup.clear()
    sup.var_sup_invoice.set("42")
    sup.delete()

    cur.execute("select * from supplier where invoice=?",("42",))
    row=cur.fetchone()
    assert row == None
    
    cur.close()
