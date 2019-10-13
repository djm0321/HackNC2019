import pymysql
import pymysql.cursors
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='SuperStrongPWD17', db='userdata', cursorclass=pymysql.cursors.DictCursor)


def checkUsername(userName, pwd, rows, cur):
    goodName = True
    for row in rows:
        if row["user"].lower() == userName.lower():
            print("Username " + row['user'] + " is unavailable")
            goodName = False
    if goodName:
        print("Username " + userName + " is available")
        insertData(userName, pwd, 10000, cur)

def insertData(user, pwd, money, cur):
    insert = "INSERT INTO username (user, pwd, money) VALUES (%s, %s, %s)"
    putIn = (user, pwd, money)
    cur.execute(insert, putIn)
    print("test")
        
        
    
    