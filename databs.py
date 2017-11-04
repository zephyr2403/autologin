import MySQLdb as mdb
sql_conn = mdb.connect('localhost','root','1234567','autologin')
cursor = sql_conn.cursor()
cursor.execute('use autologin')


def new_user(user,passwd):#function to create and insert new user in the database
    try:
        print 'yes'
        cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(user,passwd))
        print 'yes'
        cursor.execute("CREATE TABLE %s (name varchar(100),url varchar(5000),username varchar(100),password varchar(100))"%(user))
        print 'yes'
        url='https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        cursor.execute("INSERT INTO %s VALUES ('Gmail','%s','InsertUsername','InsertPassword')"%(user,url))
        sql_conn.commit()
        return 1
    except:
        return 0

def log_in(user,passwd): #function to verify and login the user in the database
    cursor.execute('SELECT * FROM users WHERE username="%s" AND password="%s" '%(user,passwd))
    detvar=cursor.fetchone()
    if(detvar==None):
        return 0
    else:
        cursor.execute("SELECT * FROM %s" % (user))
        return cursor.fetchall()
