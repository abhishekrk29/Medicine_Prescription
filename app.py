
import cx_Oracle

def adddiseaseandmedicines(diseasename, medicine1, medicine2=None, medicine3=None, medicine4=None, medicine5=None, medicine6=None, medicine7=None, medicine8=None, medicine9=None):
    conn = cx_Oracle.connect("Abhi/Abhi@xe")
    cursor = conn.cursor()
    sql = f"insert into medicineinfo values('{diseasename}','{medicine1}','{medicine2}','{medicine3}','{medicine4}','{medicine5}','{medicine6}','{medicine7}','{medicine8}','{medicine9}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def adddiseaseandsymptoms(diseasename, symptom1, symptom2=None, symptom3=None, symptom4=None, symptom5=None, symptom6=None, symptom7=None, symptom8=None, symptom9=None):
    conn = cx_Oracle.connect("Abhi/Abhi@xe")
    cursor = conn.cursor()
    sql = f"insert into diseaseinfo values('{diseasename}','{symptom1}','{symptom2}','{symptom3}','{symptom4}','{symptom5}','{symptom6}','{symptom7}','{symptom8}','{symptom9}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/adminpannelui', methods=['GET', 'POST'])
def adminpannelui():
     username = {'name': 'Abhishek'}
     return render_template("adminpannelui.html",user=username)


@app.route('/adminshowdatabase', methods=['GET', 'POST'])
def adminshowdatabase():
     username = {'name': 'Abhishek'}
     return render_template("adminshowdatabase.html", user=username)

@app.route('/doctorui', methods=['GET', 'POST'])
def doctorui():
     return render_template("doctorui.html")


@app.route('/adminadddatabase', methods=['GET', 'POST'])
def adminadddatabase():
     username = {'name': 'Abhishek'}
     return render_template("adminadddatabase.html", user=username)


@app.route('/adminmanageuser', methods=['GET', 'POST'])
def adminmanageuser():
     username = {'name': 'Abhishek'}
     return render_template("adminmanageuser.html", user=username)


@app.route('/adminupdatedatabase', methods=['GET', 'POST'])
def adminupdatedatabase():
     username = {'name': 'Abhishek'}
     return render_template("adminupdatedatabase.html", user=username)


@app.route('/admindeletedatabase', methods=['GET', 'POST'])
def admindeletedatabase():
     username = {'name': 'Abhishek'}
     return render_template("admindeletedatabase.html", user=username)


@app.route('/signupsuccess', methods=['GET', 'POST'])
def signupsuccess():
    return render_template("signupsuccess.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        details = request.form
        fullname = details['fname']
        password1 = details['pword1']
        password2 = details['pword2']
        email=details['email']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select email from registeruser where email='{email}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return render_template('signupemailerror.html')
        elif (password1 != password2):           
            return render_template('signuppasserror.html')
        else: 
            cursor.execute(f"insert into registeruser values('{fullname}','{password1}','{email}')")
            conn.commit()
            cursor.close()
            return redirect(url_for('signupsuccess'))
    return render_template('signup.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        error=1
        details = request.form
        email = details['email']
        password = details['pword']
        if (email=='fcoolabhi@gmail.com' and password=='Abhi'):
            return redirect(url_for('adminpannelui'))
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql=f"select name,email,password from registeruser where email='{email}' and password='{password}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
             name=row[0]   
             username = {'name': f'{name}'}
             return redirect(url_for('doctorui'))
        else:
            return render_template('loginerror.html',error=error)
    return render_template('login.html')


@app.route('/adminadduser', methods=['GET', 'POST'])
def adminadduser():
    if request.method == "POST":
        details = request.form
        fullname = details['fname']
        password1 = details['pword1']
        password2 = details['pword2']
        email = details['email']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select email from registeruser where email='{email}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return "User Already Exist!!"
        else:    
            cursor.execute(f"insert into registeruser values('{fullname}','{password1}','{email}')")
            conn.commit()
            cursor.close()
            return render_template('adminmanageuser.html')
    return render_template('adminmanageuser.html')


@app.route('/adminupdateuser', methods=['GET', 'POST'])
def adminupdateuser():
    if request.method == "POST":
        details = request.form
        email1 = details['email1']
        fullname = details['fname']
        password1 = details['pword1']
        password2 = details['pword2']
        email2 = details['email2']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select email from registeruser where email='{email1}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
           cursor.execute(f"update registeruser set name='{fullname}',password='{password1}',email='{email2}' where email='{email1}'")
           conn.commit()
           cursor.close()
           return render_template('adminmanageuser.html')
    return render_template('adminmanageuser.html')

@app.route('/adminsearchuser', methods=['GET', 'POST'])
def adminsearchuser():
    if request.method == "POST":
        details = request.form
        email= details['email']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select * from registeruser where email='{email}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()
        if row:
            userd={'uname':f'{row[0]}','email':f'{row[2]}','password':f'{row[1]}'}            
            return render_template('adminsearchresult.html',user=userd)
    return render_template('adminmanageuser.html')

@app.route('/adminshowalluserresult', methods=['GET', 'POST'])
def adminshowalluserresult():
    if request.method == "POST":
        details = request.form
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select * from registeruser"
        cursor.execute(sql)
        row = cursor.fetchall()
        cursor.close()
        if row: 
            return render_template('adminshowalluserresult.html',user=row)
    return render_template('adminmanageuser.html')


@app.route('/admindeleteuser', methods=['GET', 'POST'])
def admindeleteuser():
    if request.method == "POST":
        details = request.form
        email = details['email']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select email from registeruser where email='{email}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            cursor.execute(f"delete from registeruser where email='{email}'")
            conn.commit()
            cursor.close()
            return render_template('adminmanageuser.html')
    return render_template('adminmanageuser.html')

@app.route('/adminadddatabasesuccessfully', methods=['GET', 'POST'])
def adminadddatabasesuccessfully():
    username = {'name': 'Abhishek'}
    if request.method == "POST":
        details = request.form
        diseasename = details['diseasename']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select diseasename from diseaseinfo where diseasename='{diseasename}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return "Disease Already Exist!!"
        symptom1 = details['symptom1']
        symptom2 = details['symptom2']
        symptom3 = details['symptom3']
        symptom4 = details['symptom4']
        symptom5 = details['symptom5']
        symptom6 = details['symptom6']
        symptom7 = details['symptom7']
        symptom8 = details['symptom8']
        symptom9 = details['symptom9']
        medicine1 = details['medicine1']
        medicine2 = details['medicine2']
        medicine3 = details['medicine3']
        medicine4 = details['medicine4']
        medicine5 = details['medicine5']
        medicine6 = details['medicine6']
        medicine7 = details['medicine7']
        medicine8 = details['medicine8']
        medicine9 = details['medicine9']
        adddiseaseandsymptoms(diseasename, symptom1, symptom2, symptom3, symptom4,
                            symptom5, symptom6, symptom7, symptom8, symptom9)
        adddiseaseandmedicines(diseasename, medicine1, medicine2, medicine3, medicine4,
                            medicine5, medicine6, medicine7, medicine8, medicine9)
        return render_template('adminadddatabasesuccessfully.html',user=username)
    return render_template('adminadddatabase.html',user=username)


@app.route('/adminshowdiseases', methods=['GET', 'POST'])
def adminshowdiseases():
     username = {'name': 'Abhishek'}
     conn = cx_Oracle.connect("Abhi/Abhi@xe")
     cursor = conn.cursor()
     sql = f"select * from diseaseinfo "
     cursor.execute(sql)
     row = cursor.fetchall()
     cursor.close()
     if row:
        return render_template("adminshowdiseases.html", user=username,data=row)
     else:
        return 'No Data Available!!'
     return render_template("adminshowdatabase.html",user=username)


@app.route('/adminshowmedicine', methods=['GET', 'POST'])
def adminshowmedicine():
     username = {'name': 'Abhishek'}
     conn = cx_Oracle.connect("Abhi/Abhi@xe")
     cursor = conn.cursor()
     sql = f"select * from medicineinfo "
     cursor.execute(sql)
     row = cursor.fetchall()
     cursor.close()
     if row:
        return render_template("adminshowmedicine.html", user=username, data=row)
     else:
         return 'No Data Available!!'   
     return render_template("adminshowdatabase.html", user=username)

@app.route('/adminupdatedisease', methods=['GET', 'POST'])
def adminupdatedisease():
    if request.method == "POST":
        details = request.form
        username = {'name': 'Abhishek'}
        diseasename = details['diseasename1']
        diseasename2 = details['diseasename2']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select diseasename from diseaseinfo where diseasename='{diseasename}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
           cursor.execute(f"update diseaseinfo set diseasename='{diseasename2}' where diseasename='{diseasename}' ")
           cursor.execute(f"update medicineinfo set diseasename='{diseasename2}' where diseasename='{diseasename}' ")
           conn.commit()
           cursor.close()
           return render_template('adminupdatediseasesuccessfully.html', user=username)
        else:
           return 'Disease Not Available in Database'
    return render_template("adminupdatedatabase.html", user=username)


@app.route('/admindeletedisease', methods=['GET', 'POST'])
def admindeletedisease():
    if request.method == "POST":
        details=request.form
        username={'name': 'Abhishek'}
        disease=details['disease']
        conn=cx_Oracle.connect("Abhi/Abhi@xe")
        cursor=conn.cursor()
        sql=f"select diseasename from diseaseinfo where diseasename='{disease}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            cursor.execute(f"delete from medicineinfo where diseasename='{disease}'")
            cursor.execute(f"delete from diseaseinfo where diseasename='{disease}'")
            conn.commit()
            cursor.close()
            return render_template('admindeletedatabasesuccessfully.html',user=username)
        else:
            return 'Disease Not Available in Database'    
    return render_template('adminmdeletedatabase.html',user=username)

@app.route('/prescribefordoctor', methods=['GET', 'POST'])
def prescribefordoctor():
    if request.method == "POST":
        details=request.form
        fname=details['fname']
        lname=details['lname']
        age=details['age']
        diseasename=details['diseasename']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select * from medicineinfo where diseasename='{diseasename}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return render_template('prescribefordoctor.html', row=row)
        else:
            return "Medicine Details is not Available in Database"
    return render_template('doctorui.html')    


@app.route('/prescribeforadmin', methods=['GET', 'POST'])
def prescribeforadmin():
    if request.method == "POST":
        username = {'name': 'Abhishek'}
        details = request.form
        fname = details['fname']
        lname = details['lname']
        age = details['age']
        diseasename = details['diseasename']
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cursor = conn.cursor()
        sql = f"select * from medicineinfo where diseasename='{diseasename}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return render_template('prescribeforadmin.html', row=row, user=username)
        else:
            return "Medicine Details is not Available in Database"    
    return render_template('adminpannelui.html',user=username)


@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    return render_template("forgotpassword.html")


if __name__ == '__main__':
    app.run( debug = True)
