import pymysql
import pymysql.cursors
import users
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='SuperStrongPWD17', db='userdata', cursorclass=pymysql.cursors.DictCursor)
        

cur = conn.cursor()
# cur.execute("CREATE DATABASE userdata")
# sq = cur.execute("CREATE TABLE username (id INT NOT NULL AUTO_INCREMENT, user varchar(255), pwd varchar(255) , money double, PRIMARY KEY (ID)  );")
val = "(0,'meterbeter5000','pigbeen','69')"
cur.execute("INSERT INTO username (id, user, pwd, money) VALUES (1, 'urmom', 'urMom', '69420')")
users.insertData('imsad', 'imsadder', 1231, cur)
tab = cur.execute("SELECT * FROM username")
rows = cur.fetchall()
users.checkUsername("urdad", "hehe", rows, cur)
tab = cur.execute("SELECT * FROM username")
rows = cur.fetchall()
for row in rows:
    print(row["user"], row["money"])

