import pymysql as sql

def getcon():
    con=sql.connect(host='localhost',port=3306,user='root',password='R@vilove1',database='ducat')
    return con

def create_table():
    try:
        con=getcon()
        cur=con.cursor()
        cur.execute("create table students(stu_id int(2) primary key,stu_name text(50),stu_mob text(10),stu_email text(50),stu_course text(20),reg_date date,course_fee int(2),amount int(2))")
        con.commit()
        con.close()
        print('table created...')
    except:
        print('table already exists')


def getnextid():
    con=getcon()
    cur=con.cursor()
    cur.execute("select max(stu_id) from students")
    sid=cur.fetchone()[0]
    if(sid==None):
        sid=1001
        return sid
    else:
        sid=sid+1
        return sid
    con.close()
    



