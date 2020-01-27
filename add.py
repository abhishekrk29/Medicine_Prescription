import cx_Oracle

def adddiseaseandmedicines(diseasename, medicine1, medicine2=None, medicine3=None, medicine4=None, medicine5=None, medicine6=None, medicine7=None, medicine8=None, medicine9=None):
    conn = cx_Oracle.connect("Abhi/Abhi@xe")
    cursor = conn.cursor()
    sql = f"insert into medicineinfo values('{diseasename}','{medicine1}','{medicine2}','{medicine3}','{medicine4}','{medicine5}','{medicine6}','{medicine7}','{medicine8}','{medicine9}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()

def adddiseaseandsymptoms(diseasename, symptom1, symptom2=None , symptom3=None, symptom4=None, symptom5=None, symptom6=None, symptom7=None, symptom8=None, symptom9=None):
    conn = cx_Oracle.connect("Abhi/Abhi@xe")
    cursor = conn.cursor()
    sql = f"insert into diseaseinfo values('{diseasename}','{symptom1}','{symptom2}','{symptom3}','{symptom4}','{symptom5}','{symptom6}','{symptom7}','{symptom8}','{symptom9}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()


adddiseaseandmedicines('COMMON FEVER', 'CHERICOFF SYRUP', 'CROCIN SYRUP', 'BENADRYL-A SYRUP', ' APRODINE TAB','SINAREST TAB', 'MUCINEX TAB')
adddiseaseandmedicines('CHOLERA', 'CROCIN TAB', 'SUMO TAB', 'COMBIFLAM TAB','BELADONA TAB')
adddiseaseandmedicines('JAUNDICE', 'CURVEDA LIVER LOYAL TAB', ' Allen A18 JAUNDICE SYRUP')
adddiseaseandmedicines('DIARRHOEA', 'LONOX TAB', 'Imodium A-D TAB', 'DAROLAC SACHET TAB','FLORA BC CAPSULE')
adddiseaseandmedicines('PNEUMONIA', 'MACOLITE SYRUP', 'TOXO MOX TAB','AMOXIL TAB')
print("Done")
