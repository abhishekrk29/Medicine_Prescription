#SIGN IN FUNCTION:
#VALIDATIONS REQUIRED!
import cx_Oracle
import getpass
import re
from datetime import date
from faker import *
from IPython.display import clear_output
def addDoctor():
    try:
        fake=faker()
        conn=cx_Oracle.connect("Admin/12345@localhost")
        cur=conn.cursor()
        print("Welcome to Medicine Prescriber")
        print("Sign Up for Doctor!\n")
        # DOCTOR INFORMATION:-
        DrID=fake.random_int(min=10000,max=50000)
        name=input("Name: \n")
        DrName="Dr. "+name
        passd=getpass.getpass(prompt="Enter Password:  ")
        word=getpass.getpass(prompt="Confirm Password: ")
        if passd!=word:
            print("Passwords didn't match.")
        else:
            print("Select Gender:")
            print("Press M for Male.")
            print("Press F for Female.")
            Gender=input()
            if Gender=='M' or Gender=='m':
                Gender="M"
            elif Gender=='F' or Gender=='f':
                Gender="F"
            else:
                print("Invalid Input")
            Age=int(input("Enter your Age: "))
            if Age>61 or Age<=21:
            print("Invalid Age please re-Enter Age")
            mob=input("Enter your Mobile Number: ")
            mobno= "+91"+mob
            x=checkMobileNumberExistence(mobno)
            if x==True:
                print("Exists")
                clear_output() #to clear output of cell
                #loginFunctioncall()
            else:
                pass
            email=input("Enter your email: ")
            x=checkEmailExistence(email)
            if x==True:
                print("Exists")
                clear_output()
                #LoginFunctioncall()
            else:
                pass
            nops=0
            doj=date.today()
            print(doj)
            LicenseNo=input("Enter your Doctor's License Number: ").upper()
            expert=input("Enter your Specialisation: ")
            status=0
            print("We have sent you a verification E-MAIL:- %s. Please share us your resume at: admin.medPrescriber@gmail.com." %email)
            #SQL Queries:
            #To change or alter the date format of oracle to "yyyy-mm-dd".
            query0="alter session set nls_date_format='yyyy-mm-dd'"  
            query1=f"insert into DoctorInfo values({DrID},'{DrName}','{Gender}',{Age},'{mobno}','{email}',{nops},'{doj}','{LicenseNo}','{password}','{expert}')"
            conn.commit()
            role="D"
            query2=f"insert into loginInfo values({DrID},'{password}','{email}',{status},'{mobno}','{role}')"
            cur.execute(query0)
            cur.execute(query1)
            cur.execute(query2)
            conn.commit()
            print("Registered Sucessfully!")
    except conn.DatabaseError as e:
        if conn:
            conn.rollback()
            print("ERROR WITH SQL!= :",e)
    finally:
        cur.close()
        conn.close() 