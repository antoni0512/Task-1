#from coll import sql,d
import mysql.connector
from mysql.connector import errors
class db():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root",password="",database="collegeuser")
        self.c = self.con.cursor()
        #self.c.execute("select * from student")
        self.sql = ("SELECT * FROM student WHERE id=1")
        #self.c.execute("select m1,m2,m3,m4,m5 from student where id = 1")
        #self.c.execute(self.sql)
    def menu(self):
        while True:
            print("Welcome")
            print("Press 1 to get user id")
            print("Press 2 to insert new user")
            print("Press 3 to delete user")
            print("Press 4 to get all user")
            print("Press 5 to update user")
            try:
                choice = int(input())
                if(choice==1):
                    self.id = int(input("Enter the id: "))
                    self.c.execute("SELECT * from student WHERE id=%s", (self.id,))
                    a = self.c.fetchall()
                    for i in a:
                        print(i)
                elif(choice==2):
                    id = int(input("Enter the id: "))
                    name = input("Enter name: ")
                    dept = input("Enter dept: ")
                    m1 = int(input("Enter the Mark1: "))
                    m2 = int(input("Enter the Mark2: "))
                    m3 = int(input("Enter the Mark3: "))
                    m4 = int(input("Enter the Mark4: "))
                    m5 = int(input("Enter the Mark5: "))
                    sql = ("INSERT INTO student(id,name,dept,m1,m2,m3,m4,m5,total,avg,grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

                    val = (id, name, dept,m1,m2,m3,m4,m5)
                    self.c.execute(sql,val)
                    self.con.commit()
                    self.con.close()
                elif(choice == 3):
                    Value = int(input("Type the id to be deleted: "))
                    self.c.execute("DELETE FROM student WHERE id=%s", (Value,))
                    self.con.commit()
                    self.con.close()
                elif(choice == 4):
                    for i in self.c:
                        print(i)
                    self.con.commit()
                    self.con.close()
                elif(choice == 5):
                    id = int(input("Enter the id: "))
                    name = input("Enter the name: ")
                    newdept = input("Enter the dept: ")
                    valueTOUpdateList = []
                    valueTOUpdateList.append(name)
                    valueTOUpdateList.append(newdept)
                    valueTOUpdateList.append(id)
                    valueTOUpdateTupple = tuple(valueTOUpdateList)
                    sql = ("UPDATE student SET name = %s, dept = %s WHERE id = %s")
                    self.c.execute(sql,valueTOUpdateTupple)
                    self.con.commit()
                    self.con.close()
                elif(choice == 6):
                    break
                else:
                    print("invalid")
            except Exception as e:
                print(e)
                print("Invalid details try again")
            
class Student(db):
    def showrecord(self):
        try:
            for i in self.c:
                print(i)
            self.c.close()
            self.con.close()
        except mysql.connector.Error as err:
            print(err)
    def total(self):
        try:
            self.c.execute(self.sql)
            for i in self.c:
                self.total = sum(list(i))
                print(self.total)
        except mysql.connector.Error as err:
            print(err)
    def avg(self):
        try:
            self.sql = ("SELECT avg FROM student WHERE id=1")
            self.c.execute(self.sql)
            for i in self.c:
                print(i)
        except mysql.connector.Error as err:
            print(err)
    def grade(self):
        try:
            self.sql = ("SELECT grade FROM student WHERE id=1")
            self.c.execute(self.sql)
            for i in self.c:
                print(i)
        except mysql.connector.Error as err:
            print(err)


s = db()
s.menu()
#s = Student()
#s.avg()
