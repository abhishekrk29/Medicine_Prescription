import cx_Oracle
def DiseaseSuggestor(symptoms):
    try:
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cur = conn.cursor()
        sql = "select diseaseid, diseasename from dinfo where symptoms like :ID"
        cur.execute(sql, {'ID': '%'+symptoms+'%'})
        row = cur.fetchone()
        print("\n\nPatient may suffer from following Diseases:")
        li = []
        count = 0
        while row != None:
            li.append(row[0])
            count += 1
            print("%s" % row[1])
            row = cur.fetchone()
        MedicineSuggestor(li, count)
    except conn.DatabaseError as e:
        if conn:
            conn.rollback()
            print("Problem with SQL msg= :", e)
    finally:
        cur.close()
        conn.close()

def MedicineSuggestor(lx, c):
    try:
        conn = cx_Oracle.connect("Abhi/Abhi@xe")
        cur = conn.cursor()
        while c != 0:
            lx.reverse()
            x = lx.pop()
            conn.commit()
            sql0 = "select medicinename,medicinetype from minfo where diseaseID= :ID "
            cur.execute(sql0, {'ID': x})
            row = cur.fetchone()
            sql1 = "select diseasename from dinfo where diseaseID= :ID"
            cur.execute(sql1, {'ID': x})
            record = cur.fetchone()
            print("Suggested Medicine for: %s" % record[0])
            if row == None:
                print("No Information Available")
            else:
                while row != None:
                    print('MEDICINE NAME: %s ' %
                          row[0], 'MEDICNE TYPE: %s' % row[1])
                    row = cur.fetchone()
            c = c-1
    except conn.DatabaseError as e:
        if conn:
            conn.rollback()
            print("Not Proper Connection.Unable to view users! msg= :", e)
    finally:
        cur.close()
        conn.close()
        
sympt = input("ENter MUltiple Input:-").split(",")
for i in sympt:
    DiseaseSuggestor(i.capitalize())
print("Done")