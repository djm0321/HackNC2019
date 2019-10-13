import pymysql
import pymysql.cursors
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='SuperStrongPWD17', db='userdata', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

def checkUsername(userName):
    cur.execute("SELECT user FROM usernames")