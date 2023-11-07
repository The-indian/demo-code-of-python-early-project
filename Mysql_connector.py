#import mysql.connector
#mydb1 = mysql.connector.connect(
 # host="localhost",
 # user="root",
 # passwd="",
 # database="test"
  #)


 
 # first of all install pymysql as pip install pymysql

import pymysql
mydb1=pymysql.connect(user='root',password='',host='localhost',database='test')



def create_table():
    
    try:
        mycursor = mydb1.cursor()
        mycursor.execute("CREATE TABLE bill1 (my_id VARCHAR(10),name VARCHAR(30),amount varchar(30))")
        print("Table Created")
    except:
        print("Table Already Created")
        
def create_db():
    
    try:
        mycursor = mydb1.cursor()
        mycursor.execute("create database mydb1")
        print("Database Created")
    except:
        print("Databse  Already Created")
        
def use_db():
    
    try:
        mycursor = mydb1.cursor()
        mycursor.execute("use mydb1")
        print("Database Changed by user..")
    except:
        print("Databse not changed....")

def insert_table():
    
    try:

        print('Into the try block.....')
        mycursor = mydb1.cursor()
        my_id=input('New ID ')
        my_name=input('New name')
        amount=input('New Amount ')
        sql="insert into bill1 values(%s,%s,%s)"
        val=(my_id,my_name,amount)
        mycursor.execute(sql,val)
        mydb1.commit()
        print(mycursor.rowcount, "  New ...Record inserted.")
        
    except:
        print(" Sorry Record Not Inserted")


def search_data():
    use_db()
    mycursor=mydb1.cursor()
    print("Select the search criteria : ")
    print("1. by ID: ")
    print("2.  by Name : ")
    print("3. By Amount : ")
    print("4. All Details")
    ch=int(input("Enter the choice : "))

    if (ch==1):
        s=input("Enter ID : ")
        mycursor.execute("SELECT * FROM bill1")
        myresult = mycursor.fetchall()
        for x in myresult:
            if(x[0]==s):
                print(x)
                # Here zero for ID,1 for name ,2 for amount

        if(myresult):
            print(" Now No Record Found for ID: ",s)
            
    elif (ch==2):
        s=input("Enter  Name : ")
        mycursor.execute("SELECT * FROM bill1")
        myresult = mycursor.fetchall()
        for x in myresult:
            if(x[1]==s):
                print(x)
        if(myresult):
            print(" Now No Record Found for Sender Name: ",s)
            # Here zero for ID,1 for name ,2 for amount
            
    elif (ch==3):
        s=input("Enter amount : ")
        mycursor.execute("SELECT * FROM bill1")
        myresult = mycursor.fetchall()
        for x in myresult:
            if(x[2]==s):
                print(x)
        if(myresult):
            print(" Now No Record Found for Receiver Name: ",s)
            
    elif (ch==4):
        mycursor.execute("SELECT * FROM bill1")
        myresult = mycursor.fetchall()
        for x in myresult:
          print(x)
        if(myresult):
            print(" Now No Record Found !!")



def delete_data():
    
    try:

        print('Into the try block.....')
        use_db()
        mycursor = mydb1.cursor()
        #print(mycursor)
        my_id=input('  Enter id to delete  ')
        sql="delete from bill1 where my_id=%s"
        val=(my_id)
        mycursor.execute(sql,val)
        mydb1.commit()
        print(mycursor.rowcount, "  New ...Record deleted.")
        
    except:
        print(" Sorry Record Not Deleted")

ch=1
while ch==1:
    c=int(input('1. show connection \n 2. create database \n 3. Open Database \n \
4. create Table \n 5. insert Record \n 6. search data \n 7. delete record'))
    if c==1:
        print(mydb1)
    elif c==2:
        create_db()
    elif c==3:
        use_db()
    elif c==4:
        create_table()
    elif c==5:
        insert_table()
    elif c==6:
        search_data()
    elif c==7:
        delete_data()
    else:
        print('BYE BYE ')
        break
    ch=int(input('Enter  1 to continue or any other character to quit '))

    












