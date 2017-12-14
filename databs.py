import MySQLdb as mdb
sql_conn = mdb.connect('localhost','root','1234567','autologin')
cursor = sql_conn.cursor()
cursor.execute('use autologin')

def edit_entry(table,name,url,username,password,oldname):
    #try:
        cursor.execute('UPDATE %s SET name="%s", url="%s",username="%s",password="%s" WHERE name="%s"'%(table,name,url,username,password,oldname))
        sql_conn.commit()
        cursor.execute('SELECT * FROM %s'%(table))
        return cursor.fetchall()
    #except:
        return 0

def new_entry(table,name,url,username,password):
    try:
        cursor.execute("INSERT INTO %s VALUES ('%s','%s','%s','%s')"%(table,name,url,username,password))
        sql_conn.commit()
        cursor.execute("SELECT * FROM %s" % (table))
        return cursor.fetchall()
    except:
        return 0

def new_user(user,passwd):#function to create and insert new user in the database
    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(user,passwd))
        cursor.execute("CREATE TABLE %s (name varchar(100) not null unique,url varchar(5000) not null,username varchar(100) not null,password varchar(100) not null)"%(user))
        url='https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        cursor.execute("INSERT INTO %s VALUES ('Gmail','%s','Username.date@gmail.com','InsertPassword')"%(user,url))
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
