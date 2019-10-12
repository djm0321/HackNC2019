import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='')

cur = conn.cursor()
#sq = cur.execute("CREATE TABLE username (id INT NOT NULL AUTO_INCREMENT, user varchar(255), pass varchar(255) , money double, PRIMARY KEY (ID)  );")
val = "(0,'meterbeter5000','pigbeen','69')"
cur.execute("INSERT INTO username (id,user,pass,money) VALUES (%s,%s)")

tab = cur.execute("SELECT pass FROM username")
print(tab)
