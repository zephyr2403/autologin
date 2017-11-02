import MySQLdb as mdb
sql_conn = mdb.connect('localhost','root','1234567','autologin')
cursor = sql_conn.cursor()
cursor.execute('use autologin')
def new_user(user,passwd):
    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(user,passwd))
        sql_conn.commit()
        return 1
    except:
        return 0

def log_in(user,passwd):
    cursor.execute('SELECT * FROM users WHERE username="%s" AND password="%s" '%(user,passwd))
    detvar=cursor.fetchone()
    if(detvar==None):
        return 0
    else:
        return detvar[1]
