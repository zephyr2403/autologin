import lib.sqlite3 as sqlite3
import os, sys
from encryptor import Encryptor

'''
CHANGE WORKING DIRECTORY TO CURRENT FILE LOCATION
'''

if(os.path.dirname(sys.argv[0])==''):
    pass
else:
    os.chdir(os.path.dirname(sys.argv[0]))
'''
DATABASE CREATION AND CONNECTION
'''
sql_conn = sqlite3.connect('autologin.db')
cursor = sql_conn.cursor()
try:
    cursor.execute('CREATE TABLE users (username varchar(100) not null unique,password varchar(100) not null)')
except:
    pass 


'''
FUNCTION THAT EDITS THE ENTRY IN DATABASE
'''
def edit_entry(table,name,url,username,password,oldname):
    try:
        password = Encryptor().encrypt(password)
        cursor.execute('UPDATE %s SET name="%s", url="%s",username="%s",password="%s" WHERE name="%s"'%(table,name,url,username,password,oldname))
        sql_conn.commit()
        cursor.execute('SELECT * FROM %s'%(table))
        return cursor.fetchall()
    except:
        return 0


'''
FUNCTION THAT ADDS THE ENTRY IN DATABASE
'''
def new_entry(table,name,url,username,password):
    try:
        password = Encryptor().encrypt(password)
        print password
        cursor.execute("INSERT INTO %s VALUES ('%s','%s','%s','%s')"%(table,name,url,username,password))
        sql_conn.commit()
        cursor.execute("SELECT * FROM %s" % (table))
        return cursor.fetchall()
    except:
        return 0


'''
FUNCTION THAT ADDS NEW USER IN DATABASE
'''
def new_user(user,passwd):#function to create and insert new user in the database
    if len(user)==0 or len(passwd) ==0:
        return 0
    try:
        passwd = Encryptor().encrypt(passwd)
        cursor.execute("INSERT INTO users (username,password) VALUES ('%s','%s')"%(user,passwd))
        cursor.execute("CREATE TABLE %s (name varchar(100) not null unique,url varchar(5000) not null,username varchar(100) not null,password varchar(100) not null)"%(user))
        url='https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        cursor.execute("INSERT INTO %s VALUES ('Gmail','%s','Username.date@gmail.com','InsertPassword')"%(user,url))
        url='https://www.facebook.com/login.php'
        cursor.execute("INSERT INTO %s VALUES ('Facebook','%s','somename@domain.com','InsertPassword')"%(user,url))
        url='https://www.instagram.com/accounts/login/'
        cursor.execute("INSERT INTO %s VALUES ('Instagram','%s','Coolusername','InsertPassword')"%(user,url))
        url='https://www.linkedin.com/uas/login-submit'
        cursor.execute("INSERT INTO %s VALUES ('Linkedin','%s','Coolusername','InsertPassword')"%(user,url))
        sql_conn.commit()
        return 1
    except:
        return 0


'''
FUNCTION THAT PROVIDES AUTHENTICATION
'''
def log_in(user,passwd): #function to verify and login the user in the database
    
    cursor.execute('SELECT * FROM users WHERE username="%s"'%(user))
    detvar=cursor.fetchone()
    print detvar
    if(detvar == None or len(detvar[0])==0):
        return 0
    else:
        print detvar[1]
        if Encryptor().decrypt(str(detvar[1])) == passwd:
            cursor.execute("SELECT * FROM %s" % (user))
            return cursor.fetchall()
        else:
            return 0